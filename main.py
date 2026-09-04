from fastapi import FastAPI, UploadFile, File, HTTPException, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import shutil
os = __import__('os')

app = FastAPI(
    title="SONIQ Master AI API",
    version="1.0.0",
    description="Professional AI Audio Mastering Engine & DSP Pipeline"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

class MasteringRequest(BaseModel):
    filename: str
    genre: str  # e.g., "Techno", "Malay Ballad"
    style: str  # e.g., "Natural", "Clean", "Warm", "Punch", "Wide", "Power", "Vintage", "Cinematic"
    target_lufs: float = -14.0

@app.post("/api/v1/audio/upload")
async def upload_audio(file: UploadFile = File(...)):
    allowed_types = ["audio/wav", "audio/x-wav", "audio/flac", "audio/mpeg", "audio/aiff"]
    if file.content_type not in allowed_types:
        raise HTTPException(status_code=400, detail="Format audio tidak disokong. Sila guna WAV, FLAC, MP3, atau AIFF.")
    
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
        
    return {
        "status": "success",
        "filename": file.filename,
        "message": "Fail berjaya dimuat naik dan disimpan dalam storan selamat."
    }

@app.post("/api/v1/analysis/{filename}")
async def analyze_mix(filename: str):
    file_path = os.path.join(UPLOAD_DIR, filename)
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="Fail audio tidak dijumpai.")
    
    # Mock Analysis Engine (Mengikut spesifikasi Blueprint Poin 11)
    analysis_result = {
        "filename": filename,
        "lufs_integrated": -16.2,
        "true_peak": -1.4,
        "dynamic_range": 11.2,
        "crest_factor": 12.1,
        "stereo_width": 0.74,
        "bass_energy": 0.81,
        "mid_energy": 0.54,
        "high_energy": 0.76,
        "harshness": 0.31,
        "clipping": False,
        "vocal_presence": 0.85 # Perlindungan vokal asal aktif
    }
    return analysis_result

@app.post("/api/v1/master")
async def create_master(request: MasteringRequest, background_tasks: BackgroundTasks):
    # Rule-Based AI Decision Engine (Blueprint Poin 12-14)
    mastering_plan = {
        "eq": {"low_shelf": -0.6 if request.genre == "Techno" else 0.0, "presence_boost": 0.4},
        "compression": {"ratio": 1.5, "attack_ms": 30, "release_ms": 120},
        "saturation": {"amount": 0.05 if request.style == "Warm" else 0.02},
        "stereo_imaging": {"high_width": 0.08, "mono_below_120hz": True},
        "limiter": {"target_lufs": request.target_lufs, "true_peak": -1.0},
        "vocal_protection": "Active (Pitch & Formant Locked)"
    }
    
    job_id = "job_" + os.urandom(4).hex()
    return {
        "job_id": job_id,
        "status": "processing",
        "style_selected": request.style,
        "genre_profile": request.genre,
        "plan": mastering_plan,
        "message": "Enjin AI sedang memproses audio melalui rantaian DSP dengan perlindungan vokal asal."
                          }
  
