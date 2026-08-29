from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
import os

app = FastAPI()

@app.get("/")
def serve_index():
    if os.path.exists("index.html"):
        return FileResponse("index.html")
    return {"detail": "index.html not found"}

# Menyokong kedua-dua nama supaya tiada lagi ralat 'Not Found'
@app.get("/studio.html")
@app.get("/studioai.html")
def serve_studio():
    if os.path.exists("studioai.html"):
        return FileResponse("studioai.html")
    raise HTTPException(status_code=404, detail="studioai.html not found")

@app.get("/effects.html")
def serve_effects():
    if os.path.exists("effects.html"):
        return FileResponse("effects.html")
    raise HTTPException(status_code=404, detail="effects.html not found")

@app.get("/result.html")
def serve_result():
    if os.path.exists("result.html"):
        return FileResponse("result.html")
    raise HTTPException(status_code=404, detail="result.html not found")

@app.get("/Untitled design.png")
def serve_image():
    if os.path.exists("Untitled design.png"):
        return FileResponse("Untitled design.png")
    raise HTTPException(status_code=404, detail="Image not found")
    
