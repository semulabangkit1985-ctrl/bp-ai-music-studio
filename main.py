import os
import uuid
import numpy as np
from scipy.io import wavfile
from fastapi import FastAPI, UploadFile, File, BackgroundTasks, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/", StaticFiles(directory=".", html=True), name="static")


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Laluan untuk paparan web dan fail statik (index.html, imej, dll)
app.mount("/", StaticFiles(directory=".", html=True), name="static")

@app.post("/api/master")
async def master_audio(file: UploadFile = File(...), background_tasks: BackgroundTasks = None):
    job_id = str(uuid.uuid4())
    input_file = os.path.join(TEMP_DIR, f"input_{job_id}.wav")
    output_file = os.path.join(TEMP_DIR, f"master_{job_id}.wav")

    with open(input_file, "wb") as f:
        content = await file.read()
        f.write(content)

    background_tasks.add_task(process_mastering, input_file, output_file)
    return {"job_id": job_id}

@app.get("/api/download/{job_id}")
async def download_audio(job_id: str):
    output_file = os.path.join(TEMP_DIR, f"master_{job_id}.wav")
    if os.path.exists(output_file):
        return FileResponse(output_file, media_type="audio/wav", filename="mastered.wav")
    raise HTTPException(status_code=404, detail="Audio sedang diproses")
    
