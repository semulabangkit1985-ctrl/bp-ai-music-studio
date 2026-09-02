import os
import urllib.parse
import shutil
from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Direktori untuk menyimpan fail audio yang dimuat naik
UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

# Paparan Halaman Utama (index.html)
@app.get("/", response_class=HTMLResponse)
async def read_index():
    if os.path.exists("index.html"):
        with open("index.html", "r", encoding="utf-8") as f:
            return f.read()
    return "<h1>Fail index.html tidak dijumpai</h1>"

# Paparan Halaman Studio Konsol (effects.html)
@app.get("/effects", response_class=HTMLResponse)
async def read_effects():
    if os.path.exists("effects.html"):
        with open("effects.html", "r", encoding="utf-8") as f:
            return f.read()
    return "<h1>Fail effects.html tidak dijumpai</h1>"

# Laluan untuk memuat turun / memaparkan gambar latar belakang KL
@app.get("/kl.jpg.png")
async def get_background():
    if os.path.exists("kl.jpg.png"):
        return FileResponse("kl.jpg.png")
    raise HTTPException(status_code=404, detail="Background kl.jpg.png tidak dijumpai")

# Laluan untuk menerima fail audio (MP3 / WAV) yang dimuat naik
@app.post("/upload-audio")
async def upload_audio(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    encoded_filename = urllib.parse.quote(file.filename)
    return {
        "filename": file.filename,
        "url": f"/stream-audio/{encoded_filename}"
    }

# Laluan untuk penstriman atau memainkan fail audio
@app.get("/stream-audio/{filename}")
async def stream_audio(filename: str):
    decoded_filename = urllib.parse.unquote(filename)
    file_path = os.path.join(UPLOAD_DIR, decoded_filename)
    if os.path.exists(file_path):
        return FileResponse(file_path)
    raise HTTPException(status_code=404, detail="Fail audio tidak dijumpai")

# Laluan untuk memproses audio mengikut tetapan mastering pengguna
@app.post("/process-audio")
async def process_audio(
    filename: str = Form(...),
    style: str = Form(...),
    eq: float = Form(...),
    presence: float = Form(...),
    width: float = Form(...),
    dynamics: float = Form(...),
    trim: float = Form(...)
):
    file_path = os.path.join(UPLOAD_DIR, filename)
    if not os.path.exists(file_path):
        return {"error": "Fail audio asal tidak dijumpai"}
    
    # Di sini nanti kita boleh letak kod pustaka audio Python (seperti pydub) 
    # untuk ubah volume, EQ, atau kesan berdasarkan nilai slider yang dihantar.
    # Untuk permulaan, pelayan menerima tetapan ini dan mengembalikan semula fail untuk dimainkan.
    
    encoded_filename = urllib.parse.quote(filename)
    return {
        "message": f"Mastering berjaya dengan gaya {style}!",
        "url": f"/stream-audio/{encoded_filename}"
    }
    
