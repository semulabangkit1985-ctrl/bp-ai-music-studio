import json
from pathlib import Path
from fastapi import APIRouter, Depends, File, Form, HTTPException, UploadFile
from sqlalchemy.orm import Session
from .db import get_db
from .models import User, AudioFile, MasterJob, CreditTransaction
from .schemas import RegisterIn, LoginIn, MasterIn
from .auth import hash_password, verify_password, create_token
from .config import settings

router = APIRouter()

@router.post("/auth/register")
def register(data: RegisterIn, db: Session = Depends(get_db)):
    if db.query(User).filter(User.email == data.email).first():
        raise HTTPException(409, "Email already registered")
    user = User(email=data.email, password_hash=hash_password(data.password), credits=3)
    db.add(user); db.commit(); db.refresh(user)
    return {"token": create_token(user.id), "user_id": user.id, "credits": user.credits}

@router.post("/auth/login")
def login(data: LoginIn, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == data.email).first()
    if not user or not verify_password(data.password, user.password_hash):
        raise HTTPException(401, "Invalid email or password")
    return {"token": create_token(user.id), "user_id": user.id, "credits": user.credits}

@router.post("/audio/upload")
async def upload_audio(
    user_id: int = Form(...),
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    allowed = {".wav", ".flac", ".mp3", ".aiff", ".aif"}
    suffix = Path(file.filename or "").suffix.lower()
    if suffix not in allowed:
        raise HTTPException(400, "Unsupported audio format")
    user_dir = Path(settings.storage_dir) / str(user_id)
    user_dir.mkdir(parents=True, exist_ok=True)
    dest = user_dir / f"{file.filename}"
    data = await file.read()
    if len(data) > 500 * 1024 * 1024:
        raise HTTPException(413, "File too large")
    dest.write_bytes(data)
    audio = AudioFile(user_id=user_id, filename=file.filename, path=str(dest))
    db.add(audio); db.commit(); db.refresh(audio)
    return {"audio_id": audio.id, "filename": audio.filename}

@router.post("/master")
def create_master(data: MasterIn, db: Session = Depends(get_db)):
    audio = db.get(AudioFile, data.audio_id)
    if not audio:
        raise HTTPException(404, "Audio not found")
    user = db.get(User, audio.user_id)
    if not user or user.credits < 1:
        raise HTTPException(402, "Not enough credits")
    user.credits -= 1
    job = MasterJob(audio_id=audio.id, style=data.style, status="queued")
    db.add(job)
    db.add(CreditTransaction(user_id=user.id, amount=-1, reason="master"))
    db.commit(); db.refresh(job)
    # Worker can pick queued jobs in production. For local MVP, call the worker command separately.
    return {"job_id": job.id, "status": job.status}

@router.get("/jobs/{job_id}")
def get_job(job_id: int, db: Session = Depends(get_db)):
    job = db.get(MasterJob, job_id)
    if not job:
        raise HTTPException(404, "Job not found")
    return {
        "id": job.id,
        "status": job.status,
        "output_path": job.output_path,
        "report": json.loads(job.report_json) if job.report_json else None
    }
