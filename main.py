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
            background: #0b0f19;
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
            text-rendering: optimizeLegibility;
        }

        .app-container {
            width: 100%;
            max-width: 480px;
            min-height: 100vh;
            background-color: #0b0f19;
            position: relative;
            display: flex;
            flex-direction: column;
            box-shadow: 0 0 30px rgba(0,0,0,0.8);
            box-sizing: border-box;
            margin: 0 auto;
        }

        .screen-overlay {
            background: rgba(11, 15, 25, 0.85);
            backdrop-filter: blur(6px);
            flex: 1;
            display: flex;
            flex-direction: column;
            justify-content: center;
            gap: 16px;
            padding: 24px 20px;
            box-sizing: border-box;
            min-height: 100vh;
            width: 100%;
        }

        #screenLogin {
            background-image: url('/images (43).jpeg');
            background-size: cover;
            background-position: center;
        }

        .dashboard-container {
            background: #f8fafc;
            color: #0f172a;
            flex: 1;
            display: flex;
            flex-direction: column;
            padding: 24px 20px;
            box-sizing: border-box;
            min-height: 100vh;
            width: 100%;
            overflow-y: auto;
        }

        .brand-logo {
            font-family: 'Syne', sans-serif;
            font-size: 22px;
            font-weight: 800;
            color: #ffffff;
            text-align: center;
            letter-spacing: 1px;
            margin-bottom: 10px;
        }

        .social-login-grid {
            display: flex;
            gap: 12px;
            width: 100%;
            margin-bottom: 15px;
        }

        .social-btn {
            flex: 1;
            background: rgba(255, 255, 255, 0.08);
            border: 1px solid rgba(255, 255, 255, 0.15);
            padding: 12px;
            border-radius: 30px;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            transition: all 0.2s ease;
            color: #ffffff;
            font-size: 13px;
        }

        .divider-text {
            text-align: center;
            font-size: 13px;
            color: #94a3b8;
            margin: 10px 0;
        }

        .form-group {
            width: 100%;
            margin-bottom: 12px;
        }

        .form-input {
            background: rgba(15, 23, 42, 0.9);
            border: 1px solid rgba(255, 255, 255, 0.15);
            padding: 14px 18px;
            border-radius: 12px;
            width: 100%;
            color: #ffffff;
            font-size: 13px;
            box-sizing: border-box;
            outline: none;
            text-align: center;
        }

        .btn-primary {
            background: #22d3ee;
            color: #0b0f19;
            font-family: 'Syne', sans-serif;
            font-weight: 700;
            font-size: 14px;
            padding: 14px;
            border-radius: 30px;
            border: none;
            width: 100%;
            cursor: pointer;
            box-shadow: 0 4px 15px rgba(34, 211, 238, 0.4);
            transition: all 0.2s;
            margin-top: 5px;
        }

        .wizard-step-indicator {
            font-family: 'Syne', sans-serif;
            font-size: 13px;
            font-weight: 700;
            color: #22d3ee;
            letter-spacing: 1px;
            margin-bottom: 4px;
        }

        .wizard-title {
            font-family: 'Syne', sans-serif;
            font-size: 20px;
            font-weight: 800;
            color: #ffffff;
            line-height: 1.3;
            margin-bottom: 6px;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
            width: 100%;
        }

        .wizard-subtitle {
            font-size: 12px;
            color: #94a3b8;
            line-height: 1.4;
            margin-bottom: 12px;
        }

        .wizard-body {
            width: 100%;
            max-height: 52vh;
            overflow-y: auto;
            padding-right: 4px;
        }

        .wizard-body::-webkit-scrollbar { width: 4px; }
        .wizard-body::-webkit-scrollbar-thumb { background: rgba(255, 255, 255, 0.2); border-radius: 4px; }

        .genre-category-title {
            font-size: 12px;
            font-weight: 700;
            color: #22d3ee;
            margin: 14px 0 8px 0;
            letter-spacing: 0.5px;
        }

        .pill-grid {
            display: flex;
            flex-wrap: wrap;
            gap: 8px;
            width: 100%;
            margin-bottom: 10px;
        }

        .pill-option {
            background: rgba(255, 255, 255, 0.05);
            border: 1px solid rgba(255, 255, 255, 0.15);
            padding: 8px 14px;
            border-radius: 20px;
            font-size: 12px;
            font-weight: 500;
            color: #e2e8f0;
            cursor: pointer;
            transition: all 0.2s ease;
        }

        .pill-option.active {
            background: rgba(34, 211, 238, 0.25);
            border-color: #22d3ee;
            color: #ffffff;
        }

        .wizard-footer {
            width: 100%;
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding-top: 12px;
            border-top: 1px solid rgba(255, 255, 255, 0.08);
        }

        .btn-text {
            background: none;
            border: none;
            color: #94a3b8;
            font-size: 13px;
            font-weight: 600;
            cursor: pointer;
        }

        .dash-top-bar {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 24px;
        }

        .workspace-badge {
            display: flex;
            align-items: center;
            gap: 8px;
            font-weight: 600;
            font-size: 14px;
            color: #0f172a;
        }

        .dash-actions {
            display: flex;
            gap: 10px;
            margin-bottom: 24px;
        }

        .dash-btn-new {
            background: #0f172a;
            color: #ffffff;
            border: none;
            padding: 8px 16px;
            border-radius: 8px;
            font-size: 13px;
            font-weight: 600;
            cursor: pointer;
        }

        .project-card {
            background: #ffffff;
            border: 1px solid #e2e8f0;
            border-radius: 12px;
            padding: 16px;
            margin-bottom: 14px;
            box-shadow: 0 1px 3px rgba(0,0,0,0.05);
            cursor: pointer;
        }
        
        .project-card:hover { border-color: #22d3ee; }

        .project-status {
            display: inline-flex;
            align-items: center;
            gap: 6px;
            background: #dcfce7;
            color: #166534;
            padding: 6px 12px;
            border-radius: 20px;
            font-size: 12px;
            font-weight: 600;
            margin-top: 10px;
        }

        .create-project-box {
            border: 2px dashed #cbd5e1;
            border-radius: 12px;
            padding: 24px;
            text-align: center;
            color: #64748b;
            font-size: 14px;
            font-weight: 600;
            cursor: pointer;
            background: #ffffff;
            transition: border-color 0.2s;
        }

        .upload-audio-box {
            border: 2px dashed rgba(34, 211, 238, 0.4);
            border-radius: 12px;
            padding: 16px;
            text-align: center;
            color: #22d3ee;
            font-size: 12px;
            font-weight: 600;
            cursor: pointer;
            background: rgba(15, 23, 42, 0.6);
            margin-bottom: 14px;
        }

        .waveform-box {
            background: rgba(15, 23, 42, 0.9);
            border: 1px solid rgba(34, 211, 238, 0.3);
            border-radius: 14px;
            padding: 20px;
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 14px;
            margin-bottom: 15px;
        }

        .waveform-bars {
            display: flex;
            align-items: center;
            gap: 4px;
            height: 48px;
            width: 100%;
            justify-content: center;
        }

        .wave-bar {
            width: 4px;
            background: #22d3ee;
            border-radius: 4px;
            height: 12px;
            transition: height 0.2s ease;
        }

        .playing .wave-bar {
            animation: soundWave 1.2s infinite ease-in-out alternate;
        }

        @keyframes soundWave {
            0% { height: 10px; }
            50% { height: 42px; }
            100% { height: 16px; }
        }

        .wave-bar:nth-child(2) { animation-delay: 0.1s; }
        .wave-bar:nth-child(3) { animation-delay: 0.2s; }
        .wave-bar:nth-child(4) { animation-delay: 0.3s; }
        .wave-bar:nth-child(5) { animation-delay: 0.4s; }
        .wave-bar:nth-child(6) { animation-delay: 0.5s; }
        .wave-bar:nth-child(7) { animation-delay: 0.15s; }
        .wave-bar:nth-child(8) { animation-delay: 0.25s; }
        .wave-bar:nth-child(9) { animation-delay: 0.35s; }
        .wave-bar:nth-child(10) { animation-delay: 0.45s; }

        .player-controls {
            display: flex;
            align-items: center;
            gap: 20px;
        }

        .control-btn-main {
            background: #22d3ee;
            color: #0b0f19;
            width: 50px;
            height: 50px;
            border-radius: 50%;
            border: none;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 20px;
            cursor: pointer;
            box-shadow: 0 0 15px rgba(34, 211, 238, 0.5);
        }

        .stems-list {
            display: flex;
            flex-direction: column;
            gap: 8px;
            width: 100%;
        }

        .stem-item {
            background: rgba(255, 255, 255, 0.05);
            border: 1px solid rgba(255, 255, 255, 0.1);
            padding: 10px 14px;
            border-radius: 10px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            font-size: 12px;
        }

        /* MODAL LOADING AI MASTERING */
        #masterModal {
            position: fixed;
            top: 0; left: 0; width: 100%; height: 100%;
            background: rgba(11, 15, 25, 0.9);
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            z-index: 2000;
            gap: 15px;
            padding: 20px;
            box-sizing: border-box;
        }

        .spinner {
            width: 45px;
            height: 45px;
            border: 4px solid rgba(34, 211, 238, 0.2);
            border-top: 4px solid #22d3ee;
            border-radius: 50%;
            animation: spin 1s linear infinite;
        }

        @keyframes spin { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }

        .hidden { display: none !important; }

        #toast {
            position: fixed;
            bottom: 30px;
            background: #10b981;
            color: white;
            padding: 10px 20px;
            border-radius: 8px;
            font-size: 12px;
            font-weight: 600;
            opacity: 0;
            transition: opacity 0.3s;
            z-index: 1000;
        }
    </style>
</head>
<body>

<audio id="audioElement" preload="auto"></audio>
<div id="toast">Berjaya!</div>

<!-- SKRIN PROSES AI MASTERING -->
<div id="masterModal" class="hidden">
    <div class="spinner"></div>
    <div style="font-family: 'Syne', sans-serif; font-size: 18px; font-weight: 700; color: #22d3ee;">AI Mastering sedang diproses...</div>
    <div style="font-size: 12px; color: #94a3b8; text-align: center;" id="masterStatusText">Mengoptimumkan frekuensi & kompresi studio...</div>
</div>

<div class="app-container">

    <!-- SKRIN 1: LOGIN -->
    <div id="screenLogin" class="screen-overlay">
        <div>
            <div class="brand-logo">BP AI MUSIC STUDIO</div>
            <div style="font-size: 12px; color: #94a3b8; text-align: center; margin-bottom: 20px;">Log masuk ke akaun profesional anda</div>
            
            <div class="social-login-grid">
                <div class="social-btn" onclick="nextScreen('wizardStep1')">🌐 Google</div>
                <div class="social-btn" onclick="nextScreen('wizardStep1')">🍎 Apple</div>
                <div class="social-btn" onclick="nextScreen('wizardStep1')">📘 Facebook</div>
            </div>

            <div class="divider-text">atau melalui e-mel</div>

            <div class="form-group">
                <input type="email" class="form-input" placeholder="E-mel anda">
            </div>
            <div class="form-group">
                <input type="password" class="form-input" placeholder="Kata laluan">
            </div>
        </div>

        <div>
            <button class="btn-primary" onclick="nextScreen('wizardStep1')">Log Masuk</button>
        </div>
    </div>

    <!-- WIZARD STEP 1 (1/5) -->
    <div id="wizardStep1" class="screen-overlay hidden">
        <div>
            <div class="wizard-step-indicator">1/5</div>
            <div class="wizard-title" style="white-space: normal;">Selamat datang! Apa yang anda ingin buat dahulu?</div>
        </div>
        <div class="wizard-body">
            <div class="pill-grid">
                <div class="pill-option active" onclick="selectPill(this)">🎚️ Mastering</div>
                <div class="pill-option" onclick="selectPill(this)">🌍 Distribution</div>
                <div class="pill-option" onclick="selectPill(this)">🎵 Samples</div>
            </div>
        </div>
        <div class="wizard-footer">
            <button class="btn-text" onclick="nextScreen('screenLogin')">← Kembali</button>
            <button class="btn-primary" style="width: auto; padding: 10px 24px; margin: 0;" onclick="nextScreen('wizardStep2')">Seterusnya →</button>
        </div>
    </div>

    <!-- WIZARD STEP 2 (2/5) -->
    <div id="wizardStep2" class="screen-overlay hidden">
        <div>
            <div class="wizard-step-indicator">2/5</div>
            <div class="wizard-title" style="white-space: normal;">Mari tetapkan Profil Studio anda</div>
        </div>
        <div class="wizard-body">
            <div class="form-group">
                <label style="font-size: 11px; color: #22d3ee; font-weight: 600; display: block; margin-bottom: 6px;">NAMA ANDA / ARTIS</label>
                <input type="text" class="form-input" value="Boyz">
            </div>
        </div>
        <div class="wizard-footer">
            <button class="btn-text" onclick="nextScreen('wizardStep1')">← Kembali</button>
            <button class="btn-primary" style="width: auto; padding: 10px 24px; margin: 0;" onclick="finishWizard()">Selesai →</button>
        </div>
    </div>

    <!-- AI PROMPT STUDIO SCREEN -->
    <div id="screenAIPrompt" class="screen-overlay hidden">
        <div>
            <div class="wizard-step-indicator">AI STUDIO</div>
            <div class="wizard-title" style="white-space: normal;">Jana Gubahan Muzik AI</div>
            <div class="wizard-subtitle">Taip konsep lagu anda atau muat naik fail audio original di bawah.</div>
        </div>
        
        <div class="wizard-body">
            <div class="upload-audio-box" onclick="document.getElementById('audioFileInput').click()">
                📂 Muat Naik Fail Audio Original (.mp3 / .wav)
                <input type="file" id="audioFileInput" accept="audio/*" style="display: none;" onchange="handleAudioUpload(event)">
            </div>
            <div id="uploadStatus" style="font-size: 11px; color: #10b981; text-align: center; margin-bottom: 10px;"></div>

            <div class="form-group">
                <label style="font-size: 11px; color: #22d3ee; font-weight: 600; display: block; margin-bottom: 6px;">KONSEP / DESKRIPSI LAGU</label>
                <textarea class="form-input" id="songPromptText" style="height: 80px; text-align: left; resize: none;" placeholder="Contoh: Lagu pop melayu santai dengan sentuhan Malay Bounce..."></textarea>
            </div>
        </div>

        <div class="wizard-footer">
            <button class="btn-text" onclick="nextScreen('dashboardScreen')">← Kembali</button>
            <button class="btn-primary" style="width: auto; padding: 10px 24px; margin: 0;" onclick="nextScreen('screenAudioPlayer')">Buka Player 🎵</button>
        </div>
    </div>

    <!-- AUDIO PLAYER & WAVEFORM SCREEN -->
    <div id="screenAudioPlayer" class="screen-overlay hidden">
        <div>
            <div class="wizard-step-indicator">PLAYER & STEMS</div>
            <div class="wizard-title" id="playerProjectTitle">Projek Malay Bounce Studio</div>
            <div class="wizard-subtitle">Memainkan fail audio original anda secara langsung.</div>
        </div>
        
        <div class="wizard-body">
            <div class="waveform-box" id="waveformBox">
                <div style="font-size: 11px; color: #94a3b8; font-weight: 600;">WAVEFORM VISUALIZER</div>
                <div class="waveform-bars">
                    <div class="wave-bar"></div><div class="wave-bar"></div><div class="wave-bar"></div>
                    <div class="wave-bar"></div><div class="wave-bar"></div><div class="wave-bar"></div>
                    <div class="wave-bar"></div><div class="wave-bar"></div><div class="wave-bar"></div>
                    
         <div class="wave-bar"></div>
                </div>
                <div style="font-size: 13px; font-weight: 700; color: #22d3ee;" id="playerTime">00:00 / 00:00</div>

                <div class="player-controls">
                    <button class="control-btn-main" id="playPauseBtn" onclick="togglePlayAudio()">▶</button>
                </div>
            </div>

            <div class="genre-category-title">Fail Stems Berasingan (Muat Turun Sebenar)</div>
            <div class="stems-list">
                <div class="stem-item">
                    <span>🎙️ Vokal Utama (Original)</span>
                    <button class="btn-text" style="color: #22d3ee;" onclick="downloadCurrentStem()">Muat Turun ⬇</button>
                </div>
                <div class="stem-item">
                    <span>🥁 Drum & Percussion</span>
                    <button class="btn-text" style="color: #22d3ee;" onclick="downloadCurrentStem()">Muat Turun ⬇</button>
                </div>
            </div>
        </div>

        <div class="wizard-footer">
            <button class="btn-text" onclick="nextScreen('dashboardScreen')">← Kembali</button>
            <button class="btn-primary" style="width: auto; padding: 10px 24px; margin: 0;" onclick="startAIMastering()">Simpan Master 🎵</button>
        </div>
    </div>

    <!-- DASHBOARD -->
    <div id="dashboardScreen" class="dashboard-container hidden">
        <div class="dash-top-bar">
            <div class="workspace-badge">
                <span>🎧</span> Bangkit's workspace ▾
            </div>
        </div>

        <h1 style="font-family: 'Syne', sans-serif; font-size: 26px; font-weight: 800; margin: 0 0 16px 0;">Overview</h1>

        <div class="dash-actions">
            <button class="dash-btn-new" onclick="nextScreen('screenAIPrompt')">+ New Project ▾</button>
        </div>

        <!-- SENARAI PROJEK DINAMIK -->
        <div id="projectListContainer">
            <div class="project-card" onclick="nextScreen('screenAudioPlayer')">
                <div style="font-weight: 700; font-size: 15px;" id="dashProjectName">Projek Malay Bounce Studio</div>
                <div style="font-size: 12px; color: #64748b; margin-top: 4px;">Klik untuk buka pemain audio original 🎧</div>
                <div class="project-status">✓ Sedia dimainkan</div>
            </div>
        </div>

        <div class="create-project-box" onclick="nextScreen('screenAIPrompt')">
            + Muat naik fail baru / Buat projek
        </div>
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
            isPlaying = false;
            document.getElementById('waveformBox').classList.remove('playing');
            document.getElementById('playPauseBtn').innerText = '▶';
        }

        document.querySelectorAll('.screen-overlay, .dashboard-container').forEach(el => el.classList.add('hidden'));
        document.getElementById(screenId).classList.remove('hidden');
        window.scrollTo(0, 0);
    }

    function selectPill(el) {
        el.parentElement.querySelectorAll('.pill-option').forEach(p => p.classList.remove('active'));
        el.classList.add('active');
    }

    function finishWizard() {
        showToast("Profil studio disimpan!");
        setTimeout(() => { nextScreen('dashboardScreen'); }, 1000);
    }

    // Fungsi muat naik fail audio & kemas kini senarai projek di dashboard
    async function handleAudioUpload(event) {
        const file = event.target.files[0];
        if (!file) return;

        currentUploadedFilename = file.name;
        let formData = new FormData();
        formData.append("file", file);

        showToast("Sedang memuat naik audio original...");
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
                let displayName = fullName.length > 28 ? fullName.substring(0, 25) + '...' : fullName;
                
                document.getElementById('playerProjectTitle').innerText = displayName;
                document.getElementById('playerProjectTitle').title = fullName;
                document.getElementById('dashProjectName').innerText = displayName;
                
                // Kemas kini senarai projek dinamik di dashboard
                document.getElementById('projectListContainer').innerHTML = `
                    <div class="project-card" onclick="nextScreen('screenAudioPlayer')">
                        <div style="font-weight: 700; font-size: 15px;">${displayName}</div>
                        <div style="font-size: 12px; color: #64748b; margin-top: 4px;">Fail audio original dimuat naik 🎧</div>
                        <div class="project-status">✓ Audio original aktif</div>
                    </div>
                `;
                
                showToast("Fail audio berjaya dipasang!");
                document.getElementById('uploadStatus').innerText = "✓ " + displayName + " sedia dimainkan!";
            }
        } catch (err) {
            showToast("Gagal memuat naik fail audio.");
            document.getElementById('uploadStatus').innerText = "❌ Ralat muat naik.";
        }
    }

    // Muat turun stem sebenar dari server
    function downloadCurrentStem() {
        if (!currentUploadedFilename) {
            showToast("Tiada fail audio aktif untuk dimuat turun.");
            return;
        }
        showToast("Memuat turun fail stem...");
        window.location.href = `/download-stem/${encodeURIComponent(currentUploadedFilename)}`;
    }

    // Simulasi Proses AI Mastering dengan Progress Bar
    function startAIMastering() {
        let modal = document.getElementById('masterModal');
        let statusText = document.getElementById('masterStatusText');
        modal.classList.remove('hidden');

        setTimeout(() => { statusText.innerText = "Menganalisis spektrum dinamik audio..."; }, 1200);
        setTimeout(() => { statusText.innerText = "Mengaplikasikan AI Neural Limiter..."; }, 2500);
        setTimeout(() => {
            modal.classList.add('hidden');
            statusText.innerText = "Mengoptimumkan frekuensi & kompresi studio...";
            showToast("Master file berjaya disimpan & siap!");
        }, 3800);
    }

    let isPlaying = false;
    const audio = document.getElementById('audioElement');

    function togglePlayAudio() {
        let box = document.getElementById('waveformBox');
        let btn = document.getElementById('playPauseBtn');
        
        if (!audio.src) {
            showToast("Sila muat naik fail audio original terlebih dahulu!");
            return;
        }

        if (isPlaying) {
            audio.pause();
            box.classList.remove('playing');
            btn.innerText = '▶';
            isPlaying = false;
        } else {
            audio.play().then(() => {
                box.classList.add('playing');
                btn.innerText = '⏸';
                isPlaying = true;
            }).catch(e => {
                showToast("Sila klik sekali lagi untuk kebenaran audio pelayar.");
            });
        }
    }

    audio.addEventListener('timeupdate', () => {
        let currentMinutes = Math.floor(audio.currentTime / 60);
        let currentSeconds = Math.floor(audio.currentTime % 60);
        let durMinutes = Math.floor(audio.duration / 60) || 0;
        let durSeconds = Math.floor(audio.duration % 60) || 0;

        let formattedCurrent = `${String(currentMinutes).padStart(2, '0')}:${String(currentSeconds).padStart(2, '0')}`;
        let formattedDuration = `${String(durMinutes).padStart(2, '0')}:${String(durSeconds).padStart(2, '0')}`;

        document.getElementById('playerTime').innerText = `${formattedCurrent} / ${formattedDuration}`;
    });

    audio.addEventListener('ended', () => {
        isPlaying = false;
        document.getElementById('waveformBox').classList.remove('playing');
        document.getElementById('playPauseBtn').innerText = '▶';
    });
</script>

</body>
</html>
"""
