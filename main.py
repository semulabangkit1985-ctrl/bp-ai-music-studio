import os
import uuid
import numpy as np
from scipy.io import wavfile
from fastapi import FastAPI, UploadFile, File, BackgroundTasks, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

TEMP_DIR = "/tmp/audio_processing"
os.makedirs(TEMP_DIR, exist_ok=True)

def process_mastering(input_path: str, output_path: str):
    sr, data = wavfile.read(input_path)
    
    if data.dtype == np.int16:
        float_data = data.astype(np.float32) / 32768.0
    else:
        float_data = data.astype(np.float32)

    gain = 1.4
    mastered = np.tanh(float_data * gain)
    
    output_data = (mastered * 32767).astype(np.int16)
    wavfile.write(output_path, sr, output_data)

    if os.path.exists(input_path):
        os.remove(input_path)

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
    
