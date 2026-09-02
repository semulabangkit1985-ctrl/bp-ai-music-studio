from fastapi import FastAPI, UploadFile, File
from fastapi.responses import HTMLResponse, FileResponse
import os
import shutil

app = FastAPI()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.get("/images (43).jpeg")
def get_kl_bg():
    if os.path.exists("images (43).jpeg"):
        return FileResponse("images (43).jpeg")
    return {"error": "Background image not found"}

@app.post("/upload-audio")
async def upload_audio(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_path, "wb+") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"filename": file.filename, "url": f"/stream-audio/{file.filename}"}

@app.get("/stream-audio/{filename}")
def stream_audio(filename: str):
    file_path = os.path.join(UPLOAD_DIR, filename)
    if os.path.exists(file_path):
        return FileResponse(file_path)
    return {"error": "Audio not found"}

@app.get("/download-stem/{filename}")
def download_stem(filename: str):
    file_path = os.path.join(UPLOAD_DIR, filename)
    if os.path.exists(file_path):
        return FileResponse(file_path, media_type="application/octet-stream", filename=f"stem_{filename}")
    return {"error": "File not found"}

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
            min-height: 100vh;
            overflow-x: hidden;
            -webkit-font-smoothing: antialiased;
        }

        .app-container {
            width: 100%;
            max-width: 480px;
            height: 100vh;
            max-height: 100vh;
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
            justify-content: space-between;
            align-items: center;
            padding: 24px 20px;
            box-sizing: border-box;
            height: 100%;
            overflow: hidden;
            text-align: center;
        }

        .brand-logo {
            font-family: 'Syne', sans-serif;
            font-size: 18px;
            font-weight: 800;
            color: #2dd4bf;
            letter-spacing: 0.5px;
            margin-bottom: 12px;
            width: 100%;
            text-align: center;
        }

        .login-header {
            text-align: center;
            margin-top: 20px;
            width: 100%;
        }

        .brand-logo-large {
            font-family: 'Syne', sans-serif;
            font-size: 24px;
            font-weight: 800;
            color: #ffffff;
            letter-spacing: 0.5px;
            margin-bottom: 8px;
            text-transform: uppercase;
        }

        .login-subtitle {
            font-size: 13px;
            color: #cbd5e1;
            margin-bottom: 25px;
        }

        .social-login-container {
            display: flex;
            justify-content: center;
            gap: 10px;
            margin-bottom: 20px;
            width: 100%;
        }

        .social-btn {
            flex: 1;
            max-width: 130px;
            background: rgba(15, 23, 42, 0.6);
            border: 1px solid rgba(255, 255, 255, 0.2);
            padding: 12px 10px;
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
            font-size: 12px;
            color: #94a3b8;
            margin-bottom: 20px;
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
            font-size: 22px;
            font-weight: 800;
            color: #ffffff;
            line-height: 1.2;
            margin-bottom: 6px;
            text-align: center;
            width: 100%;
        }

        .wizard-subtitle {
            font-size: 12px;
            color: #cbd5e1;
            line-height: 1.4;
            margin-bottom: 12px;
            text-align: center;
            width: 100%;
        }

        .wizard-body {
            flex: 1;
            width: 100%;
            max-width: 400px;
            overflow-y: auto;
            padding: 0 4px;
            margin: 8px 0;
            -webkit-overflow-scrolling: touch;
            display: flex;
            flex-direction: column;
            align-items: center;
        }

        .wizard-body::-webkit-scrollbar { width: 4px; }
        .wizard-body::-webkit-scrollbar-thumb { background: rgba(255, 255, 255, 0.2); border-radius: 4px; }

        .genre-category-title {
            font-size: 13px;
            font-weight: 700;
            color: #2dd4bf;
            margin: 16px 0 8px 0;
            letter-spacing: 0.3px;
            text-align: center;
            width: 100%;
        }

        .form-group {
            width: 100%;
            max-width: 360px;
            margin-bottom: 14px;
            display: flex;
            flex-direction: column;
            align-items: center;
        }

        .form-label {
            font-size: 13px;
            font-weight: 600;
            color: #e2e8f0;
            display: block;
            margin-bottom: 6px;
            text-align: center;
            width: 100%;
        }

        .form-input {
            background: rgba(15, 23, 42, 0.75);
            border: 1px solid rgba(255, 255, 255, 0.2);
            padding: 12px 14px;
            border-radius: 12px;
            width: 100%;
            color: #ffffff;
            font-size: 14px;
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
            margin-top: 5px;
            font-weight: 500;
            text-align: center;
            width: 100%;
        }

        .forgot-password {
            text-align: center;
            font-size: 12px;
            color: #38bdf8;
            margin-bottom: 20px;
            cursor: pointer;
            font-weight: 500;
            width: 100%;
        }

        /* Avatar Section */
        .avatar-section {
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 14px;
            margin-top: 6px;
            width: 100%;
        }

        .avatar-circle {
            width: 60px;
            height: 60px;
            background: #65a30d;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            font-family: 'Syne', sans-serif;
            font-size: 24px;
            font-weight: 700;
            position: relative;
        }

        .avatar-badge {
            position: absolute;
            bottom: 0;
            right: 0;
            background: #0f172a;
            color: white;
            width: 22px;
            height: 22px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 11px;
            border: 2px solid white;
        }

        /* Pill Cloud */
        .landr-pill-cloud {
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            gap: 8px;
            width: 100%;
        }

        .landr-pill {
            background: rgba(15, 23, 42, 0.65);
            border: 1px solid rgba(255, 255, 255, 0.2);
            padding: 8px 14px;
            border-radius: 25px;
            font-size: 12px;
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
            max-width: 400px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding-top: 12px;
            border-top: 1px solid rgba(255, 255, 255, 0.15);
            background: rgba(15, 23, 42, 0.85);
            backdrop-filter: blur(10px);
        }

        .btn-text {
            background: none;
            border: none;
            color: #94a3b8;
            font-size: 13px;
            font-weight: 600;
            cursor: pointer;
        }

        .btn-primary {
            background: #2dd4bf;
            color: #0f172a;
            font-family: 'Syne', sans-serif;
            font-weight: 700;
            font-size: 13px;
            padding: 11px 24px;
            border-radius: 30px;
            border: none;
            cursor: pointer;
            box-shadow: 0 4px 12px rgba(45, 212, 191, 0.4);
            transition: all 0.2s;
        }

        /* Dashboard & Studio */
        .dashboard-container {
            background: transparent;
            color: #ffffff;
            flex: 1;
            display: flex;
            flex-direction: column;
            align-items: center;
            padding: 24px 20px;
            box-sizing: border-box;
            height: 100vh;
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
            padding: 16px;
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 10px;
            margin-bottom: 12px;
            backdrop-filter: blur(8px);
            width: 100%;
            max-width: 360px;
        }

        .waveform-bars {
            display: flex;
            align-items: center;
            gap: 4px;
            height: 40px;
            width: 100%;
            justify-content: center;
        }

        .wave-bar {
            width: 4px;
            background: #2dd4bf;
            border-radius: 4px;
            height: 10px;
            transition: height 0.2s ease;
        }

        .playing .wave-bar {
            animation: soundWave 1.2s infinite ease-in-out alternate;
        }

        @keyframes soundWave {
            0% { height: 8px; }
            50% { height: 35px; }
            100% { height: 14px; }
        }

        .wave-bar:nth-child(2) { animation-delay: 0.1s; }
        .wave-bar:nth-child(3) { animation-delay: 0.2s; }
        .wave-bar:nth-child(4) { animation-delay: 0.3s; }
        .wave-bar:nth-child(5) { animation-delay: 0.4s; }

        .control-btn-main {
            background: #2dd4bf;
            color: #0f172a;
            width: 44px;
            height: 44px;
            border-radius: 50%;
            border: none;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 16px;
            cursor: pointer;
            box-shadow: 0 4px 12px rgba(45, 212, 191, 0.4);
        }

        .stem-item {
            background: rgba(15, 23, 42, 0.75);
            border: 1px solid rgba(255, 255, 255, 0.15);
            padding: 8px 12px;
            border-radius: 10px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            font-size: 11px;
            margin-bottom: 6px;
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

<audio id="audioElement" preload="auto"></audio>
<div id="toast">Berjaya!</div>

<div id="masterModal" class="hidden">
    <div class="spinner"></div>
    <div style="font-family: 'Syne', sans-serif; font-size: 18px; font-weight: 700; color: #2dd4bf;">AI Mastering sedang diproses...</div>
    <div style="font-size: 12px; color: #cbd5e1; text-align: center;" id="masterStatusText">Mengoptimumkan frekuensi & kompresi studio...</div>
</div>

<div class="app-container">

    <!-- SKRIN 1: LOGIN -->
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

            <div class="form-group" style="margin: 0 auto 14px auto;">
                <input type="email" class="form-input" placeholder="E-mel anda">
            </div>

            <div class="form-group" style="margin: 0 auto 14px auto;">
                <input type="password" class="form-input" placeholder="Kata laluan">
            </div>

            <div class="forgot-password" onclick="alert('Fungsi Lupa Kata Laluan')">Lupa kata laluan?</div>

            <button class="btn-primary" style="width: 100%; padding: 13px;" onclick="nextScreen('profileScreen')">Log Masuk</button>
        </div>

        <div></div>
    </div>

    <!-- SKRIN 2: KONFIGURASI PROFIL -->
    <div id="profileScreen" class="screen-overlay hidden">
        <div class="wizard-header-container">
            <div class="brand-logo">BP AI MUSIC STUDIO</div>
            <div class="wizard-title">Let's configure your profile</div>
            <div class="wizard-subtitle">Join and connect with our network of artists.</div>
        </div>
        
        <div class="wizard-body">
            <div class="form-group">
                <label class="form-label">Your name</label>
                <input type="text" class="form-input" value="Boyz">
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

    <!-- SKRIN 3: PERANAN KREATOR -->
    <div id="roleScreen" class="screen-overlay hidden">
        <div class="wizard-header-container">
            <div class="brand-logo">BP AI MUSIC STUDIO</div>
            <div class="wizard-title">What best represents you?</div>
            <div class="wizard-subtitle">Display the best of yourself and link up with like-minded creators.</div>
        </div>
        
        <div class="wizard-body">
            <div style="font-size: 13px; font-weight: 600; margin-bottom: 10px; color: #ffffff; text-align: center; width: 100%;">How would you best describe yourself?</div>
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

    <!-- SKRIN 4: PILIHAN GENRE LENGKAP -->
    <div id="genreScreen" class="screen-overlay hidden">
        <div class="wizard-header-container">
            <div class="brand-logo">BP AI MUSIC STUDIO</div>
            <div class="wizard-title">Pick your favorite genres</div>
            <div class="wizard-subtitle">Tell us what types of music you're into.</div>
        </div>
        
        <div class="wizard-body">
            <!-- 🇲🇾 Melayu / Nusantara -->
            <div class="genre-category-title">🇲🇾 Melayu / Nusantara</div>
            <div class="landr-pill-cloud">
                <div class="landr-pill" onclick="togglePill(this)">Pop Melayu</div>
                <div class="landr-pill" onclick="togglePill(this)">Rock Melayu</div>
                <div class="landr-pill" onclick="togglePill(this)">Balada Melayu</div>
                <div class="landr-pill" onclick="togglePill(this)">Melayu Klasik</div>
                <div class="landr-pill" onclick="togglePill(this)">Irama Malaysia</div>
                <div class="landr-pill" onclick="togglePill(this)">Lagu Asli</div>
                <div class="landr-pill" onclick="togglePill(this)">Zapin</div>
                <div class="landr-pill" onclick="togglePill(this)">Joget</div>
                <div class="landr-pill" onclick="togglePill(this)">Ghazal</div>
                <div class="landr-pill" onclick="togglePill(this)">Keroncong</div>
                <div class="landr-pill" onclick="togglePill(this)">Dangdut</div>
                <div class="landr-pill" onclick="togglePill(this)">Campursari</div>
                <div class="landr-pill" onclick="togglePill(this)">Pop Nusantara</div>
                <div class="landr-pill" onclick="togglePill(this)">Etnik Nusantara</div>
                <div class="landr-pill" onclick="togglePill(this)">Tradisional Melayu</div>
                <div class="landr-pill" onclick="togglePill(this)">Minang</div>
                <div class="landr-pill" onclick="togglePill(this)">Jawa</div>
                <div class="landr-pill" onclick="togglePill(this)">Sunda</div>
                <div class="landr-pill" onclick="togglePill(this)">Bugis</div>
                <div class="landr-pill" onclick="togglePill(this)">Batak</div>
                <div class="landr-pill active" onclick="togglePill(this)">Malay Bounce</div>
                <div class="landr-pill" onclick="togglePill(this)">Malay Trap</div>
                <div class="landr-pill active" onclick="togglePill(this)">Malay Phonk</div>
                <div class="landr-pill" onclick="togglePill(this)">Malay Electronic</div>
            </div>

            <!-- 🎤 Pop -->
            <div class="genre-category-title">🎤 Pop</div>
            <div class="landr-pill-cloud">
                <div class="landr-pill" onclick="togglePill(this)">Pop</div>
                <div class="landr-pill" onclick="togglePill(this)">Pop Ballad</div>
                <div class="landr-pill" onclick="togglePill(this)">Electropop</div>
                <div class="landr-pill" onclick="togglePill(this)">Synthpop</div>
                <div class="landr-pill" onclick="togglePill(this)">Indie Pop</div>
                <div class="landr-pill" onclick="togglePill(this)">Dance Pop</div>
                <div class="landr-pill" onclick="togglePill(this)">City Pop</div>
                <div class="landr-pill" onclick="togglePill(this)">Future Pop</div>
            </div>

            <!-- 🎸 Rock -->
            <div class="genre-category-title">🎸 Rock & Metal</div>
            <div class="landr-pill-cloud">
                <div class="landr-pill" onclick="togglePill(this)">Rock</div>
                <div class="landr-pill" onclick="togglePill(this)">Soft Rock</div>
                <div class="landr-pill" onclick="togglePill(this)">Classic Rock</div>
                <div class="landr-pill" onclick="togglePill(this)">Hard Rock</div>
                <div class="landr-pill" onclick="togglePill(this)">Alternative Rock</div>
                <div class="landr-pill" onclick="togglePill(this)">Indie Rock</div>
                <div class="landr-pill" onclick="togglePill(this)">Pop Rock</div>
                <div class="landr-pill" onclick="togglePill(this)">Heavy Metal</div>
                <div class="landr-pill" onclick="togglePill(this)">Metalcore</div>
            </div>

            <!-- 🎤 Hip Hop / Rap -->
            <div class="genre-category-title">🎤 Hip Hop / Rap</div>
            <div class="landr-pill-cloud">
                <div class="landr-pill" onclick="togglePill(this)">Hip Hop</div>
                <div class="landr-pill" onclick="togglePill(this)">Rap</div>
                <div class="landr-pill" onclick="togglePill(this)">Trap</div>
                <div class="landr-pill" onclick="togglePill(this)">Boom Bap</div>
                <div class="landr-pill" onclick="togglePill(this)">Lo-Fi Hip Hop</div>
                <div class="landr-pill" onclick="togglePill(this)">Melodic Rap</div>
                <div class="landr-pill" onclick="togglePill(this)">Drill</div>
                <div class="landr-pill" onclick="togglePill(this)">Cinematic Trap</div>
            </div>

            <!-- 🔥 Phonk -->
            <div class="genre-category-title">🔥 Phonk</div>
            <div class="landr-pill-cloud">
                <div class="landr-pill" onclick="togglePill(this)">Phonk</div>
                <div class="landr-pill" onclick="togglePill(this)">Dark Phonk</div>
                <div class="landr-pill" onclick="togglePill(this)">Drift Phonk</div>
                <div class="landr-pill" onclick="togglePill(this)">Brazilian Phonk</div>
                <div class="landr-pill" onclick="togglePill(this)">Memphis Phonk</div>
                <div class="landr-pill" onclick="togglePill(this)">Aggressive Phonk</div>
                <div class="landr-pill" onclick="togglePill(this)">Atmospheric Phonk</div>
                <div class="landr-pill" onclick="togglePill(this)">Malay Phonk</div>
            </div>

            <!-- ⚡ Techno / Electronic -->
            <div class="genre-category-title">⚡ Techno / Electronic</div>
            <div class="landr-pill-cloud">
                <div class="landr-pill" onclick="togglePill(this)">EDM</div>
                <div class="landr-pill" onclick="togglePill(this)">Techno</div>
                <div class="landr-pill" onclick="togglePill(this)">Hard Techno</div>
                <div class="landr-pill" onclick="togglePill(this)">Melodic Techno</div>
                <div class="landr-pill" onclick="togglePill(this)">House</div>
                <div class="landr-pill" onclick="togglePill(this)">Deep House</div>
                <div class="landr-pill" onclick="togglePill(this)">Trance</div>
                <div class="landr-pill" onclick="togglePill(this)">Dubstep</div>
                <div class="landr-pill" onclick="togglePill(this)">Drum & Bass</div>
                <div class="landr-pill" onclick="togglePill(this)">Amapiano</div>
            </div>

            <!-- 🎷 R&B / Soul / Funk / Jazz -->
            <div class="genre-category-title">🎷 R&B, Soul & Jazz</div>
            <div class="landr-pill-cloud">
                <div class="landr-pill" onclick="togglePill(this)">R&B</div>
                <div class="landr-pill" onclick="togglePill(this)">Contemporary R&B</div>
                <div class="landr-pill" onclick="togglePill(this)">Soul</div>
                <div class="landr-pill" onclick="togglePill(this)">Neo Soul</div>
                <div class="landr-pill" onclick="togglePill(this)">Funk</div>
                <div class="landr-pill" onclick="togglePill(this)">Jazz</div>
                <div class="landr-pill" onclick="togglePill(this)">Smooth Jazz</div>
                <div class="landr-pill" onclick="togglePill(this)">Blues</div>
            </div>

            <!-- 🎸 Akustik / Folk / Lo-Fi -->
            <div class="genre-category-title">🎸 Akustik / Folk / Lo-Fi</div>
            <div class="landr-pill-cloud">
                <div class="landr-pill" onclick="togglePill(this)">Acoustic</div>
                <div class="landr-pill" onclick="togglePill(this)">Acoustic Pop</div>
                <div class="landr-pill" onclick="togglePill(this)">Folk</div>
                <div class="landr-pill" onclick="togglePill(this)">Indie Folk</div>
                <div class="landr-pill" onclick="togglePill(this)">Singer-Songwriter</div>
                <div class="landr-pill" onclick="togglePill(this)">Chill</div>
                <div class="landr-pill" onclick="togglePill(this)">Lo-Fi</div>
                <div class="landr-pill" onclick="togglePill(this)">Lounge</div>
            </div>

            <!-- ❤️ Sedih / Emosi / Cinta -->
            <div class="genre-category-title">❤️ Sedih / Emosi / Cinta</div>
            <div class="landr-pill-cloud">
                <div class="landr-pill" onclick="togglePill(this)">Sad Song</div>
                <div class="landr-pill" onclick="togglePill(this)">Emotional</div>
                <div class="landr-pill" onclick="togglePill(this)">Heartbreak</div>
                <div class="landr-pill" onclick="togglePill(this)">Melancholic</div>
                <div class="landr-pill" onclick="togglePill(this)">Nostalgic</div>
                <div class="landr-pill" onclick="togglePill(this)">Romantic</div>
                <div class="landr-pill" onclick="togglePill(this)">Love Song</div>
                <div class="landr-pill" onclick="togglePill(this)">Slow Ballad</div>
            </div>

            <!-- 🎬 Cinematic / Mood / Khas -->
            <div class="genre-category-title">🎬 Cinematic / Mood / Khas</div>
            <div class="landr-pill-cloud">
                <div class="landr-pill" onclick="togglePill(this)">Cinematic</div>
                <div class="landr-pill" onclick="togglePill(this)">Epic</div>
                <div class="landr-pill" onclick="togglePill(this)">Dark</div>
                <div class="landr-pill" onclick="togglePill(this)">Mysterious</div>
                <div class="landr-pill" onclick="togglePill(this)">Inspirational</div>
                <div class="landr-pill" onclick="togglePill(this)">Motivational</div>
                <div class="landr-pill" onclick="togglePill(this)">Ambient</div>
                <div class="landr-pill" onclick="togglePill(this)">Wedding</div>
                <div class="landr-pill" onclick="togglePill(this)">Party</div>
                <div class="landr-pill" onclick="togglePill(this)">Raya / Aidilfitri</div>
            </div>
        </div>

        <div class="wizard-footer">
            <button class="btn-text" onclick="nextScreen('roleScreen')">← Back</button>
            <button class="btn-primary" onclick="finishOnboarding()">Continue →</button>
        </div>
    </div>

    <!-- AUDIO PLAYER & STEMS SCREEN (SKRIN 5) -->
    <div id="screenAudioPlayer" class="screen-overlay hidden">
        <div class="wizard-header-container">
            <div class="brand-logo">BP AI STUDIO</div>
            <div class="wizard-title" id="playerProjectTitle">Projek Malay Bounce Studio</div>
            <div class="wizard-subtitle">Pratonton audio masa sebenar & fail stems AI.</div>
        </div>
        
        <div class="wizard-body">
            <div class="waveform-box" id="waveformBox">
                <div style="font-size: 11px; color: #94a3b8; font-weight: 600;">WAVEFORM VISUALIZER</div>
                <div class="waveform-bars">
                    <div class="wave-bar"></div><div class="wave-bar"></div><div class="wave-bar"></div>
                    <div class="wave-bar"></div><div class="wave-bar"></div>
                </div>
                <div style="font-size: 13px; font-weight: 700; color: #2dd4bf;" id="playerTime">02:34 / 03:45</div>

                <button class="control-btn-main" id="playPauseBtn" onclick="togglePlayAudio()">▶</button>
            </div>

            <div style="font-size: 12px; font-weight: 700; color: #ffffff; margin-bottom: 8px; width: 100%; text-align: center;">Fail Stems Berasingan</div>
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

    <!-- DASHBOARD -->
    <div id="dashboardScreen" class="dashboard-container hidden">
        <div class="dash-top-bar">
            <div class="workspace-badge">
                <span>🎧</span> Studio Workspace ▾
            </div>
        </div>

        <h1 style="font-family: 'Syne', sans-serif; font-size: 22px; font-weight: 800; margin: 0 0 14px 0; text-align: center; width: 100%;">Overview</h1>

        <div id="projectListContainer" style="width: 100%; display: flex; flex-direction: column; align-items: center;">
            <div class="project-card" onclick="nextScreen('screenAudioPlayer')">
                <div style="font-weight: 700; font-size: 14px;" id="dashProjectName">Projek Malay Bounce Studio</div>
                <div style="font-size: 11px; color: #cbd5e1; margin-top: 4px;">Klik untuk buka pemain audio & fail stems 🎧</div>
                <div class="project-status">✓ Sedia dimainkan</div>
            </div>
        </div>

        <div class="upload-audio-box" onclick="document.getElementById('audioFileInput').click()" style="margin-top: 15px;">
            + Muat naik fail audio baru
            <input type="file" id="audioFileInput" accept="audio/*" style="display: none;" onchange="handleAudioUpload(event)">
        </div>
        <div id="uploadStatus" style="font-size: 11px; color: #34d399; text-align: center; margin-top: 5px; width: 100%;"></div>
    </div>

</div>

<script>
    let currentUploadedFilename = "";

    function showToast(msg) {
        let t = document.getElementById('toast');
        t.innerText = msg;
        t.style.opacity = '1';
        setTimeout(() => { t.style.opacity = '0'; }, 2000);
    }

    function nextScreen(screenId) {
        let audio = document.getElementById('audioElement');
        if(screenId !== 'screenAudioPlayer' && !audio.paused) {
            audio.pause();
            document.getElementById('waveformBox').classList.remove('playing');
            document.getElementById('playPauseBtn').innerText = '▶';
        }

        document.querySelectorAll('.screen-overlay, .dashboard-container').forEach(el => el.classList.add('hidden'));
        document.getElementById(screenId).classList.remove('hidden');
        window.scrollTo(0, 0);
    }

    function togglePill(el) {
        el.classList.toggle('active');
    }

    function finishOnboarding() {
        showToast("Profil & Genre berjaya disimpan!");
        setTimeout(() => { nextScreen('dashboardScreen'); }, 1000);
    }

    async function handleAudioUpload(event) {
        const file = event.target.files[0];
        if (!file) return;

        currentUploadedFilename = file.name;
        let formData = new FormData();
        formData.append("file", file);

        showToast("Sedang memuat naik audio...");
        document.getElementById('uploadStatus').innerText = "⏳ Memuat naik " + file.name + "...";

        try {
            let response = await fetch('/upload-audio', {
                method: 'POST',
                body: formData
            });
            let result = await response.json();
            
            if (result.url) {
                let audio = document.getElementById('audioElement');
                audio.src = result.url;
                
                let fullName = file.name;
                let displayName = fullName.length > 25 ? fullName.substring(0, 22) + '...' : fullName;
                
                document.getElementById('playerProjectTitle').innerText = displayName;
                document.getElementById('dashProjectName').innerText = displayName;
                
                showToast("Fail audio berjaya dipasang!");
                document.getElementById('uploadStatus').innerText = "✓ " + displayName + " sedia dimainkan!";
                setTimeout(() => { nextScreen('screenAudioPlayer'); }, 1000);
            }
        } catch (err) {
            showToast("Gagal memuat naik fail audio.");
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
            showToast("Master file berjaya disimpan!");
        }, 3500);
    }

    const audio = document.getElementById('audioElement');
    function togglePlayAudio() {
        let box = document.getElementById('waveformBox');
        let btn = document.getElementById('playPauseBtn');
        
        if (audio.paused) {
            if (!audio.src) {
                audio.src = "/stream-audio/sample.wav";
            }
            audio.play();
            box.classList.add('playing');
            btn.innerText = '⏸';
        } else {
            audio.pause();
            
      box.classList.remove('playing');
            btn.innerText = '▶';
        }
    }

    audio.onended = () => {
        document.getElementById('waveformBox').classList.remove('playing');
        document.getElementById('playPauseBtn').innerText = '▶';
    };
</script>
</body>
</html>
    """
