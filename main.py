from fastapi import FastAPI, UploadFile, File, Depends, Form, HTTPException
from fastapi.responses import HTMLResponse, FileResponse
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
import os
import shutil
import urllib.parse

# --- KONfigurasi Pangkalan Data SQLite ---
DATABASE_URL = "sqlite:///./database.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class UserDB(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, default="Boyz")
    email = Column(String, unique=True, index=True, default="boyz@bpstudio.com")
    profile_url = Column(String, default="network.bpstudio.com/users/boyz")

class ProjectDB(Base):
    __tablename__ = "projects"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), default=1)
    title = Column(String)
    filename = Column(String)
    release_date = Column(String, default="2026-09-05")
    isrc_code = Column(String, default="MY-BP2-26-00014")
    platforms = Column(String, default="Spotify, Apple Music")
    status = Column(String, default="Sedia dimainkan")

Base.metadata.create_all(bind=engine)

app = FastAPI()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Pastikan ada pengguna lalai dalam DB
def init_default_user():
    db = SessionLocal()
    user = db.query(UserDB).filter(UserDB.id == 1).first()
    if not user:
        db.add(UserDB(id=1, name="Boyz", email="boyz@bpstudio.com"))
        db.commit()
    db.close()

init_default_user()

@app.get("/images (43).jpeg")
def get_kl_bg():
    if os.path.exists("images (43).jpeg"):
        return FileResponse("images (43).jpeg")
    return {"error": "Background image not found"}

@app.post("/upload-audio")
async def upload_audio(file: UploadFile = File(...), db: Session = Depends(get_db)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_path, "wb+") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    encoded_filename = urllib.parse.quote(file.filename)
    
    # Simpan ke pangkalan data SQLite
    new_project = ProjectDB(
        title=file.filename,
        filename=file.filename,
        status="Sedia dimainkan"
    )
    db.add(new_project)
    db.commit()
    db.refresh(new_project)

    return {
        "filename": file.filename, 
        "url": f"/stream-audio/{encoded_filename}",
        "project_id": new_project.id
    }

@app.get("/stream-audio/{filename}")
def stream_audio(filename: str):
    decoded_filename = urllib.parse.unquote(filename)
    file_path = os.path.join(UPLOAD_DIR, decoded_filename)
    if os.path.exists(file_path):
        return FileResponse(file_path)
    return {"error": "Audio not found"}

@app.get("/download-stem/{filename}")
def download_stem(filename: str):
    decoded_filename = urllib.parse.unquote(filename)
    file_path = os.path.join(UPLOAD_DIR, decoded_filename)
    if os.path.exists(file_path):
        return FileResponse(file_path, media_type="application/octet-stream", filename=f"stem_{decoded_filename}")
    return {"error": "File not found"}

@app.post("/publish-project")
def publish_project(project_id: int = Form(...), release_date: str = Form(...), platforms: str = Form(...), db: Session = Depends(get_db)):
    project = db.query(ProjectDB).filter(ProjectDB.id == project_id).first()
    if project:
        project.release_date = release_date
        project.platforms = platforms
        project.status = "Dijadualkan untuk Edaran"
        db.commit()
        return {"success": True, "message": "Projek berjaya didaftarkan untuk edaran global!"}
    raise HTTPException(status_code=404, detail="Projek tidak dijumpai")

@app.get("/", response_class=HTMLResponse)
def main_page():
    return """
<!DOCTYPE html>
<html lang="ms">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>BP AI Music Studio</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700&family=Syne:wght@700;800&display=swap" rel="stylesheet">
    <script src="https://unpkg.com/wavesurfer.js@7/dist/wavesurfer.min.js"></script>
    
    <style>
        body {
            background: #090d16;
            color: #ffffff;
            font-family: 'Montserrat', sans-serif;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100dvh;
            overflow-x: hidden;
            -webkit-font-smoothing: antialiased;
        }

        .app-container {
            width: 100%;
            max-width: 480px;
            height: 100dvh;
            max-height: 100dvh;
            background: linear-gradient(135deg, rgba(15, 23, 42, 0.88) 0%, rgba(15, 23, 42, 0.95) 100%), url('/images (43).jpeg');
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            position: relative;
            display: flex;
            flex-direction: column;
            box-shadow: 0 0 40px rgba(0,0,0,0.7);
            box-sizing: border-box;
            margin: 0 auto;
            overflow: hidden;
        }

        .screen-overlay {
            flex: 1;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            padding: 20px;
            box-sizing: border-box;
            height: 100%;
            overflow-y: auto;
            text-align: center;
            gap: 16px;
        }

        .brand-logo {
            font-family: 'Syne', sans-serif;
            font-size: 16px;
            font-weight: 800;
            color: #2dd4bf;
            letter-spacing: 0.5px;
            margin-bottom: 4px;
            width: 100%;
            text-align: center;
        }

        .login-header {
            text-align: center;
            width: 100%;
        }

        .brand-logo-large {
            font-family: 'Syne', sans-serif;
            font-size: 22px;
            font-weight: 800;
            color: #ffffff;
            letter-spacing: 0.5px;
            margin-bottom: 6px;
            text-transform: uppercase;
        }

        .login-subtitle {
            font-size: 12px;
            color: #cbd5e1;
            margin-bottom: 20px;
        }

        .social-login-container {
            display: flex;
            justify-content: center;
            gap: 10px;
            margin-bottom: 16px;
            width: 100%;
        }

        .social-btn {
            flex: 1;
            max-width: 130px;
            background: rgba(15, 23, 42, 0.6);
            border: 1px solid rgba(255, 255, 255, 0.2);
            padding: 10px;
            border-radius: 30px;
            color: #ffffff;
            font-size: 12px;
            font-weight: 600;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 6px;
            cursor: pointer;
            backdrop-filter: blur(5px);
            transition: all 0.2s;
        }

        .social-btn:hover {
            border-color: #2dd4bf;
            background: rgba(45, 212, 191, 0.1);
        }

        .divider-text {
            text-align: center;
            font-size: 11px;
            color: #94a3b8;
            margin-bottom: 16px;
            width: 100%;
        }

        .wizard-header-container {
            width: 100%;
            display: flex;
            flex-direction: column;
            align-items: center;
        }

        .wizard-title {
            font-family: 'Syne', sans-serif;
            font-size: 20px;
            font-weight: 800;
            color: #ffffff;
            line-height: 1.2;
            margin-bottom: 4px;
            text-align: center;
            width: 100%;
        }

        .wizard-subtitle {
            font-size: 12px;
            color: #cbd5e1;
            line-height: 1.4;
            margin-bottom: 8px;
            text-align: center;
            width: 100%;
        }

        .wizard-body {
            width: 100%;
            max-width: 400px;
            max-height: 45vh;
            overflow-y: auto;
            padding: 4px;
            -webkit-overflow-scrolling: touch;
            display: flex;
            flex-direction: column;
            align-items: center;
        }

        .wizard-body::-webkit-scrollbar { width: 4px; }
        .wizard-body::-webkit-scrollbar-thumb { background: rgba(255, 255, 255, 0.2); border-radius: 4px; }

        .genre-category-title {
            font-size: 12px;
            font-weight: 700;
            color: #2dd4bf;
            margin: 12px 0 6px 0;
            letter-spacing: 0.3px;
            text-align: center;
            width: 100%;
        }

        .form-group {
            width: 100%;
            max-width: 360px;
            margin-bottom: 12px;
            display: flex;
            flex-direction: column;
            align-items: center;
        }

        .form-label {
            font-size: 12px;
            font-weight: 600;
            color: #e2e8f0;
            display: block;
            margin-bottom: 4px;
            text-align: center;
            width: 100%;
        }

        .form-input {
            background: rgba(15, 23, 42, 0.75);
            border: 1px solid rgba(255, 255, 255, 0.2);
            padding: 10px 14px;
            border-radius: 12px;
            width: 100%;
            color: #ffffff;
            font-size: 13px;
            box-sizing: border-box;
            outline: none;
            backdrop-filter: blur(5px);
            transition: border-color 0.2s;
            text-align: center;
        }

        .form-input:focus {
            border-color: #2dd4bf;
            box-shadow: 0 0 0 3px rgba(45, 212, 191, 0.2);
        }

        .url-helper {
            font-size: 11px;
            color: #34d399;
            margin-top: 4px;
            font-weight: 500;
            text-align: center;
            width: 100%;
        }

        .forgot-password {
            text-align: center;
            font-size: 12px;
            color: #38bdf8;
            margin-bottom: 16px;
            cursor: pointer;
            font-weight: 500;
            width: 100%;
        }

        .avatar-section {
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 14px;
            margin-top: 4px;
            width: 100%;
        }

        .avatar-circle {
            width: 55px;
            height: 55px;
            background: #65a30d;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            font-family: 'Syne', sans-serif;
            font-size: 22px;
            font-weight: 700;
            position: relative;
        }

        .avatar-badge {
            position: absolute;
            bottom: 0;
            right: 0;
            background: #0f172a;
            color: white;
            width: 20px;
            height: 20px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 10px;
            border: 2px solid white;
        }

        .landr-pill-cloud {
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            gap: 6px;
            width: 100%;
        }

        .landr-pill {
            background: rgba(15, 23, 42, 0.65);
            border: 1px solid rgba(255, 255, 255, 0.2);
            padding: 6px 12px;
            border-radius: 25px;
            font-size: 11px;
            font-weight: 500;
            color: #ffffff;
            cursor: pointer;
            transition: all 0.2s ease;
            user-select: none;
            backdrop-filter: blur(6px);
        }

        .landr-pill:hover {
            border-color: #2dd4bf;
            background: rgba(45, 212, 191, 0.15);
        }

        .landr-pill.active {
            background: #2dd4bf;
            border-color: #2dd4bf;
            color: #0f172a;
            font-weight: 700;
        }

        .wizard-footer {
            width: 100%;
            max-width: 360px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding-top: 10px;
            border-top: 1px solid rgba(255, 255, 255, 0.15);
            background: transparent;
        }

        .btn-text {
            background: none;
            border: none;
            color: #94a3b8;
            font-size: 12px;
            font-weight: 600;
            cursor: pointer;
        }

        .btn-primary {
            background: #2dd4bf;
            color: #0f172a;
            font-family: 'Syne', sans-serif;
            font-weight: 700;
            font-size: 12px;
            padding: 10px 22px;
            border-radius: 30px;
            border: none;
            cursor: pointer;
            box-shadow: 0 4px 12px rgba(45, 212, 191, 0.4);
            transition: all 0.2s;
        }

        .dashboard-container {
            background: transparent;
            color: #ffffff;
            flex: 1;
            display: flex;
            flex-direction: column;
            align-items: center;
            padding: 24px 20px;
            box-sizing: border-box;
            height: 100dvh;
            overflow-y: auto;
            text-align: center;
        }

        .dash-top-bar {
            display: flex;
            justify-content: center;
            align-items: center;
            margin-bottom: 16px;
            width: 100%;
        }

        .workspace-badge {
            display: flex;
            align-items: center;
            gap: 8px;
            font-weight: 600;
            font-size: 14px;
            color: #ffffff;
        }

        .project-card {
            background: rgba(15, 23, 42, 0.75);
            border: 1px solid rgba(255, 255, 255, 0.15);
            border-radius: 12px;
            padding: 14px;
            margin-bottom: 12px;
            cursor: pointer;
            backdrop-filter: blur(6px);
            width: 100%;
            max-width: 360px;
        }
        
        .project-card:hover { border-color: #2dd4bf; }

        .project-status {
            display: inline-flex;
            align-items: center;
            gap: 6px;
            background: rgba(16, 185, 129, 0.2);
            color: #34d399;
            padding: 3px 8px;
            border-radius: 20px;
            font-size: 11px;
            font-weight: 600;
            margin-top: 6px;
        }

        .upload-audio-box {
            border: 2px dashed #2dd4bf;
            border-radius: 12px;
            padding: 16px;
            text-align: center;
            color: #2dd4bf;
            font-size: 12px;
            font-weight: 600;
            cursor: pointer;
            background: rgba(15, 23, 42, 0.65);
            backdrop-filter: blur(5px);
            margin-bottom: 12px;
            width: 100%;
            max-width: 360px;
        }

        .waveform-box {
            background: rgba(15, 23, 42, 0.8);
            border: 1px solid rgba(255, 255, 255, 0.2);
            border-radius: 14px;
            padding: 14px;
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 8px;
            margin-bottom: 10px;
            backdrop-filter: blur(8px);
            width: 100%;
            max-width: 360px;
        }

        #waveform {
            width: 100%;
            margin: 6px 0;
        }

        .control-btn-main {
            background: #2dd4bf;
            color: #0f172a;
            width: 40px;
            height: 40px;
            border-radius: 50%;
            border: none;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 14px;
            cursor: pointer;
            box-shadow: 0 4px 12px rgba(45, 212, 191, 0.4);
        }

        .stem-item {
            background: rgba(15, 23, 42, 0.75);
            border: 1px solid rgba(255, 255, 255, 0.15);
            padding: 6px 12px;
            border-radius: 10px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            font-size: 11px;
            margin-bottom: 5px;
            backdrop-filter: blur(5px);
            width: 100%;
            max-width: 360px;
        }

        #masterModal {
            position: fixed;
            top: 0; left: 0; width: 100%; height: 100%;
            background: rgba(15, 23, 42, 0.9);
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            z-index: 2000;
            gap: 15px;
            padding: 20px;
            box-sizing: border-box;
            backdrop-filter: blur(10px);
            text-align: center;
        }

        .spinner {
            width: 45px;
            height: 45px;
            border: 4px solid rgba(45, 212, 191, 0.2);
            border-top: 4px solid #2dd4bf;
            border-radius: 50%;
            animation: spin 1s linear infinite;
        }

        @keyframes spin { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }

        .hidden { display: none !important; }

        #toast {
            position: fixed;
            bottom: 30px;
            left: 50%;
            transform: translateX(-50%);
            background: #0f172a;
            color: white;
            padding: 10px 20px;
            border-radius: 8px;
            font-size: 12px;
            font-weight: 600;
            opacity: 0;
            transition: opacity 0.3s;
            z-index: 1000;
            border: 1px solid rgba(255,255,255,0.2);
        }
    </style>
</head>
<body>

<div id="toast">Berjaya!</div>

<div id="masterModal" class="hidden">
    <div class="spinner"></div>
    <div style="font-family: 'Syne', sans-serif; font-size: 18px; font-weight: 700; color: #2dd4bf;">AI Mastering sedang diproses...</div>
    <div style="font-size: 12px; color: #cbd5e1; text-align: center;" id="masterStatusText">Mengoptimumkan frekuensi & kompresi studio...</div>
</div>

<div class="app-container">

    <div id="loginScreen" class="screen-overlay">
        <div class="login-header">
            <div class="brand-logo-large">BP AI MUSIC STUDIO</div>
            <div class="login-subtitle">Log masuk ke akaun profesional anda</div>
        </div>

        <div style="width: 100%; max-width: 360px;">
            <div class="social-login-container">
                <button class="social-btn" onclick="nextScreen('profileScreen')">🌐 Google</button>
                <button class="social-btn" onclick="nextScreen('profileScreen')">🍎 Apple</button>
                <button class="social-btn" onclick="nextScreen('profileScreen')">📘 Facebook</button>
            </div>

            <div class="divider-text">atau melalui e-mel</div>

            <div class="form-group" style="margin: 0 auto 12px auto;">
                <input type="email" class="form-input" placeholder="E-mel anda" value="boyz@bpstudio.com">
            </div>

            <div class="form-group" style="margin: 0 auto 12px auto;">
                  <input type="password" class="form-input" placeholder="Kata laluan" value="********">
            </div>

            <div class="forgot-password" onclick="alert('Fungsi Lupa Kata Laluan')">Lupa kata laluan?</div>

            <button class="btn-primary" style="width: 100%; padding: 12px;" onclick="nextScreen('profileScreen')">Log Masuk</button>
        </div>
    </div>

    <div id="profileScreen" class="screen-overlay hidden">
        <div class="wizard-header-container">
            <div class="brand-logo">BP AI MUSIC STUDIO</div>
            <div class="wizard-title">Let's configure your profile</div>
            <div class="wizard-subtitle">Join and connect with our network of artists.</div>
        </div>
        
        <div class="wizard-body">
            <div class="form-group">
                <label class="form-label">Your name</label>
                <input type="text" id="inputProfileName" class="form-input" value="Boyz">
            </div>

            <div class="form-group">
                <label class="form-label">Profile URL</label>
                <input type="text" class="form-input" value="network.bpstudio.com/users/boyz">
                <div class="url-helper">URL available.</div>
            </div>

            <div class="form-group">
                <label class="form-label">Profile picture</label>
                <div class="avatar-section">
                    <div class="avatar-circle">
                        B
                        <div class="avatar-badge">📷</div>
                    </div>
                </div>
            </div>
        </div>

        <div class="wizard-footer">
            <button class="btn-text" onclick="nextScreen('loginScreen')">← Back</button>
            <button class="btn-primary" onclick="nextScreen('roleScreen')">Next →</button>
        </div>
    </div>

    <div id="roleScreen" class="screen-overlay hidden">
        <div class="wizard-header-container">
            <div class="brand-logo">BP AI MUSIC STUDIO</div>
            <div class="wizard-title">What best represents you?</div>
            <div class="wizard-subtitle">Display the best of yourself and link up with like-minded creators.</div>
        </div>
        
        <div class="wizard-body">
            <div style="font-size: 12px; font-weight: 600; margin-bottom: 8px; color: #ffffff; text-align: center; width: 100%;">How would you best describe yourself?</div>
            <div class="landr-pill-cloud">
                <div class="landr-pill active" onclick="togglePill(this)">Producer</div>
                <div class="landr-pill" onclick="togglePill(this)">Musician</div>
                <div class="landr-pill" onclick="togglePill(this)">Engineer</div>
                <div class="landr-pill" onclick="togglePill(this)">Label</div>
                <div class="landr-pill" onclick="togglePill(this)">Podcaster</div>
                <div class="landr-pill" onclick="togglePill(this)">Beatmaker</div>
                <div class="landr-pill" onclick="togglePill(this)">Vocalist</div>
            </div>
        </div>

        <div class="wizard-footer">
            <button class="btn-text" onclick="nextScreen('profileScreen')">← Back</button>
            <button class="btn-primary" onclick="nextScreen('genreScreen')">Next →</button>
        </div>
    </div>

    <div id="genreScreen" class="screen-overlay hidden">
        <div class="wizard-header-container">
            <div class="brand-logo">BP AI MUSIC STUDIO</div>
            <div class="wizard-title">Pick your favorite genres</div>
            <div class="wizard-subtitle">Tell us what types of music you're into.</div>
        </div>
        
        <div class="wizard-body">
            <div class="genre-category-title">🇲🇾 Melayu / Nusantara</div>
            <div class="landr-pill-cloud">
                <div class="landr-pill" onclick="togglePill(this)">Pop Melayu</div>
                <div class="landr-pill" onclick="togglePill(this)">Rock Melayu</div>
                <div class="landr-pill" onclick="togglePill(this)">Balada Melayu</div>
                <div class="landr-pill active" onclick="togglePill(this)">Malay Bounce</div>
                <div class="landr-pill" onclick="togglePill(this)">Malay Trap</div>
                <div class="landr-pill active" onclick="togglePill(this)">Malay Phonk</div>
            </div>

            <div class="genre-category-title">🎤 Pop & Rock</div>
            <div class="landr-pill-cloud">
                <div class="landr-pill" onclick="togglePill(this)">Pop</div>
                <div class="landr-pill" onclick="togglePill(this)">Pop Ballad</div>
                <div class="landr-pill" onclick="togglePill(this)">Rock</div>
                <div class="landr-pill" onclick="togglePill(this)">Indie Pop</div>
            </div>

            <div class="genre-category-title">🔥 Phonk & Electronic</div>
            <div class="landr-pill-cloud">
                <div class="landr-pill" onclick="togglePill(this)">Phonk</div>
                <div class="landr-pill" onclick="togglePill(this)">Drift Phonk</div>
                <div class="landr-pill" onclick="togglePill(this)">EDM</div>
                <div class="landr-pill" onclick="togglePill(this)">Techno</div>
            </div>
        </div>

        <div class="wizard-footer">
            <button class="btn-text" onclick="nextScreen('roleScreen')">← Back</button>
            <button class="btn-primary" onclick="nextScreen('exportScreen')">Next →</button>
        </div>
    </div>

    <div id="exportScreen" class="screen-overlay hidden">
        <div class="wizard-header-container">
            <div class="brand-logo">BP AI MUSIC STUDIO</div>
            <div class="wizard-title">Export & Release Setup</div>
            <div class="wizard-subtitle">Choose where you want to publish your AI track globally.</div>
        </div>
        
        <div class="wizard-body">
            <div class="genre-category-title">🌐 Platform Edaran Utama</div>
            <div class="landr-pill-cloud" id="platformCloud">
                <div class="landr-pill active" onclick="togglePill(this)">Spotify</div>
                <div class="landr-pill active" onclick="togglePill(this)">Apple Music</div>
                <div class="landr-pill active" onclick="togglePill(this)">TikTok & IG</div>
                <div class="landr-pill" onclick="togglePill(this)">YouTube Music</div>
                <div class="landr-pill" onclick="togglePill(this)">Amazon Music</div>
                <div class="landr-pill" onclick="togglePill(this)">Deezer</div>
            </div>

            <div class="form-group" style="margin-top: 14px;">
                <label class="form-label">Tarikh Pelancaran (Release Date)</label>
                <input type="date" id="releaseDateInput" class="form-input" value="2026-09-05">
            </div>

            <div class="form-group">
                <label class="form-label">ISRC Code (Auto-Generated AI)</label>
                <input type="text" class="form-input" value="MY-BP2-26-00014" readonly>
                <div class="url-helper">Kod sah untuk hak cipta digital.</div>
            </div>
        </div>

        <div class="wizard-footer">
            <button class="btn-text" onclick="nextScreen('genreScreen')">← Back</button>
            <button class="btn-primary" onclick="publishProjectAPI()">Publish Now 🚀</button>
        </div>
    </div>

    <div id="screenAudioPlayer" class="screen-overlay hidden">
        <div class="wizard-header-container">
            <div class="brand-logo">BP AI STUDIO</div>
            <div class="wizard-title" id="playerProjectTitle">Projek Malay Bounce Studio</div>
            <div class="wizard-subtitle">Pratonton audio masa sebenar & fail stems AI.</div>
        </div>
        
        <div class="wizard-body">
            <div class="waveform-box">
                <div style="font-size: 11px; color: #94a3b8; font-weight: 600;">WAVESURFER VISUALIZER SEBENAR</div>
                <div id="waveform"></div>
                <div style="font-size: 12px; font-weight: 700; color: #2dd4bf;" id="playerTime">00:00 / 00:00</div>

                <button class="control-btn-main" id="playPauseBtn" onclick="togglePlayAudio()">▶</button>
            </div>

            <div style="font-size: 11px; font-weight: 700; color: #ffffff; margin-bottom: 6px; width: 100%; text-align: center;">Fail Stems Berasingan</div>
            <div class="stem-item">
                <span>🎙️ Vokal Utama (AI)</span>
                <button class="btn-text" style="color: #2dd4bf;" onclick="downloadCurrentStem()">Muat Turun ⬇</button>
            </div>
            <div class="stem-item">
                <span>🥁 Drum & Percussion</span>
                <button class="btn-text" style="color: #2dd4bf;" onclick="downloadCurrentStem()">Muat Turun ⬇</button>
            </div>
            <div class="stem-item">
                <span>🎸 Bass Line</span>
                <button class="btn-text" style="color: #2dd4bf;" onclick="downloadCurrentStem()">Muat Turun ⬇</button>
            </div>
            <div class="stem-item">
                <span>🎹 Melodi & Synth</span>
                <button class="btn-text" style="color: #2dd4bf;" onclick="downloadCurrentStem()">Muat Turun ⬇</button>
            </div>
        </div>

        <div class="wizard-footer">
            <button class="btn-text" onclick="nextScreen('dashboardScreen')">← Dashboard</button>
            <button class="btn-primary" onclick="startAIMastering()">Simpan Master 🎵</button>
        </div>
    </div>

    <div id="dashboardScreen" class="dashboard-container hidden">
        <div class="dash-top-bar">
            <div class="workspace-badge">
                <span>🎧</span> <span id="dashWorkspaceName">Boyz's Studio</span> ▾
            </div>
        </div>

        <h1 style="font-family: 'Syne', sans-serif; font-size: 20px; font-weight: 800; margin: 0 0 12px 0; text-align: center; width: 100%;">Overview</h1>

        <div id="projectListContainer" style="width: 100%; display: flex; flex-direction: column; align-items: center;">
            <div class="project-card" onclick="nextScreen('screenAudioPlayer')">
                <div style="font-weight: 700; font-size: 13px;" id="dashProjectName">Projek Malay Bounce Studio</div>
                <div style="font-size: 11px; color: #cbd5e1; margin-top: 4px;">Klik untuk buka pemain audio & fail stems 🎧</div>
                <div class="project-status" id="dashProjectStatus">✓ Sedia dimainkan</div>
            </div>
        </div>

        <div class="upload-audio-box" onclick="document.getElementById('audioFileInput').click()" style="margin-top: 12px;">
            + Muat naik fail audio baru
            <input type="file" id="audioFileInput" accept="audio/*" style="display: none;" onchange="handleAudioUpload(event)">
        </div>
        <div id="uploadStatus" style="font-size: 11px; color: #34d399; text-align: center; margin-top: 4px; width: 100%;"></div>
    </div>

</div>

<script>
    let currentUploadedFilename = "";
    let currentProjectId = 1;
    let wavesurfer = null;

    function showToast(msg) {
        let t = document.getElementById('toast');
        t.innerText = msg;
        t.style.opacity = '1';
        setTimeout(() => { t.style.opacity = '0'; }, 2000);
    }

    function initWaveform(audioUrl) {
        if (wavesurfer) {
            wavesurfer.destroy();
        }
        
        wavesurfer = WaveSurfer.create({
            container: '#waveform',
            waveColor: 'rgba(45, 212, 191, 0.4)',
            progressColor: '#2dd4bf',
            cursorColor: '#ffffff',
            barWidth: 3,
            barGap: 3,
            height: 45,
            barRadius: 3,
            url: audioUrl
        });

        wavesurfer.on('ready', () => {
            updateTimeDisplay(0, wavesurfer.getDuration());
        });

        wavesurfer.on('audioprocess', () => {
            updateTimeDisplay(wavesurfer.getCurrentTime(), wavesurfer.getDuration());
        });

        wavesurfer.on('finish', () => {
            document.getElementById('playPauseBtn').innerText = '▶';
        });
    }

    function formatTime(seconds) {
        let mins = Math.floor(seconds / 60);
        let secs = Math.floor(seconds % 60);
        return `${mins.toString().padStart(2, '0')}:${secs.toString().padStart(2, '0')}`;
    }

    function updateTimeDisplay(current, duration) {
        document.getElementById('playerTime').innerText = `${formatTime(current)} / ${formatTime(duration || 0)}`;
    }

    function nextScreen(screenId) {
        if(screenId !== 'screenAudioPlayer' && wavesurfer && wavesurfer.isPlaying()) {
            wavesurfer.pause();
            document.getElementById('playPauseBtn').innerText = '▶';
        }

        let nameInput = document.getElementById('inputProfileName').value;
        if(nameInput) {
            document.getElementById('dashWorkspaceName').innerText = nameInput + "'s Studio";
        }

        document.querySelectorAll('.screen-overlay, .dashboard-container').forEach(el => el.classList.add('hidden'));
        document.getElementById(screenId).classList.remove('hidden');
        window.scrollTo(0, 0);

        if(screenId === 'screenAudioPlayer' && wavesurfer && !wavesurfer.options.url) {
            initWaveform('/stream-audio/sample.wav');
        }
    }

    function togglePill(el) {
        el.classList.toggle('active');
    }

    async function handleAudioUpload(event) {
        const file = event.target.files[0];
        if (!file) return;

        currentUploadedFilename = file.name;
        let formData = new FormData();
        formData.append("file", file);

        showToast("Sedang memuat naik audio & pangkalan data...");
        document.getElementById('uploadStatus').innerText = "⏳ Memproses " + file.name + "...";

        try {
            let response = await fetch('/upload-audio', {
                method: 'POST',
                body: formData
            });
            let result = await response.json();
            
            if (result.url) {
                currentProjectId = result.project_id;
                initWaveform(result.url);
                
                let fullName = file.name;
                let displayName = fullName.length > 25 ? fullName.substring(0, 22) + '...' : fullName;
                
                document.getElementById('playerProjectTitle').innerText = displayName;
                document.getElementById('dashProjectName').innerText = displayName;
                document.getElementById('dashProjectStatus').innerText = "✓ Sedia dimainkan";
                
                showToast("Fail audio & pangkalan data berjaya disimpan!");
                document.getElementById('uploadStatus').innerText = "✓ " + displayName + " sedia dimainkan!";
                setTimeout(() => { nextScreen('screenAudioPlayer'); }, 1000);
            }
        } catch (err) {
            showToast("Gagal memuat naik fail audio.");
        }
    }

    async function publishProjectAPI() {
        let releaseDate = document.getElementById('releaseDateInput').value;
        let activePlatforms = [];
        document.querySelectorAll('#platformCloud .landr-pill.active').forEach(p => {
            activePlatforms.push(p.innerText);
        });

        let formData = new FormData();
        formData.append("project_id", currentProjectId);
        formData.append("release_date", releaseDate);
        formData.append("platforms", activePlatforms.join(", "));

        try {
            let response = await fetch('/publish-project', {
                method: 'POST',
                body: formData
            });
            let res = await response.json();
            if(res.success) {
                showToast(res.message);
                document.getElementById('dashProjectStatus').innerText = "✓ Dijadualkan untuk Edaran";
                setTimeout(() => { nextScreen('screenAudioPlayer'); }, 1200);
            }
        } catch(e) {
            showToast("Ralat penghantaran edaran.");
        }
    }

    function downloadCurrentStem() {
        if (!currentUploadedFilename) {
            window.location.href = `/download-stem/sample.wav`;
            return;
        }
        window.location.href = `/download-stem/${encodeURIComponent(currentUploadedFilename)}`;
    }

    function startAIMastering() {
        let modal = document.getElementById('masterModal');
        let statusText = document.getElementById('masterStatusText');
        modal.classList.remove('hidden');

        setTimeout(() => { statusText.innerText = "Mengaplikasikan AI Neural Limiter..."; }, 2000);
        setTimeout(() => {
            modal.classList.add('hidden');
            showToast("Master file berjaya disimpan ke pangkalan data!");
        }, 3500);
    }

    function togglePlayAudio() {
        if (!wavesurfer) {
            initWaveform('/stream-audio/sample.wav');
        }
        
        let btn = document.getElementById('playPauseBtn');
        if (wavesurfer.isPlaying()) {
            wavesurfer.pause();
            btn.innerText = '▶';
        } else {
            wavesurfer.play();
            btn.innerText = '⏸';
        }
    }

    // Initialize default wavesurfer on load
    window.addEventListener('DOMContentLoaded', () => {
        initWaveform('/stream-audio/sample.wav');
    });
</script>
</body>
</html>
    """
