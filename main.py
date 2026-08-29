from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()

@app.get("/")
def serve_index():
    return FileResponse("index.html")

@app.get("/studioai.html")
def serve_studio():
    return FileResponse("studioai.html")

@app.get("/effects.html")
def serve_effects():
    return FileResponse("effects.html")

@app.get("/result.html")
def serve_result():
    return FileResponse("result.html")

@app.get("/Untitled design.png")
def serve_image():
    return FileResponse("Untitled design.png")
    
