from fastapi import FastAPI, UploadFile, File, Request, Form, HTTPException
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.templating import Jinja2Templates
import os
import shutil
import urllib.parse

app = FastAPI()

# Membaca fail HTML terus dari folder utama (root directory) GitHub
templates = Jinja2Templates(directory=".")

UPLOAD_DIR = "uploads"
STEMS_DIR = "separated"
os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(STEMS_DIR, exist_ok=True)

# Laluan untuk halaman utama (index.html)
@app.get("/", response_class=HTMLResponse)
def read_index(request: Request):
    return templates.TemplateResponse(request, "index.html")

# Laluan untuk halaman kesan bunyi (effects.html)
@app.get("/effects", response_class=HTMLResponse)
def read_effects(request: Request):
    return templates.TemplateResponse(request, "effects.html")

# Laluan untuk halaman keputusan (result.html)
@app.get("/result", response_class=HTMLResponse)
def read_result(request: Request):
    return templates.TemplateResponse(request, "result.html")

# Laluan untuk halaman studio AI (studioai.html)
@app.get("/studioai", response_class=HTMLResponse)
def read_studioai(request: Request):
    return templates.TemplateResponse(request, "studioai.html")

# Laluan khas yang bersih untuk imej latar belakang KL
@app.get("/kl-bg.jpeg")
def get_kl_bg():
    if os.path.exists("images (43.jpeg)"):
        return FileResponse("images (43.jpeg)")
    return {"error": "Background image not found"}

# Laluan untuk muat naik fail audio
@app.post("/upload-audio")
async def upload_audio(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_path, "wb+") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    encoded_filename = urllib.parse.quote(file.filename)
    return {
        "filename": file.filename, 
        "url": f"/stream-audio/{encoded_filename}"
    }

# Laluan untuk penstriman audio yang dimuat naik
@app.get("/stream-audio/{filename}")
def stream_audio(filename: str):
    decoded_filename = urllib.parse.unquote(filename)
    file_path = os.path.join(UPLOAD_DIR, decoded_filename)
    if os.path.exists(file_path):
        return FileResponse(file_path)
    return {"error": "Audio not found"}
    
