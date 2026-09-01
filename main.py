from fastapi import FastAPI
from fastapi.responses import HTMLResponse, FileResponse
import os

app = FastAPI()

@app.get("/images (43).jpeg")
def get_kl_bg():
    if os.path.exists("images (43).jpeg"):
        return FileResponse("images (43).jpeg")
    return {"error": "Background image not found"}

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
            -moz-osx-font-smoothing: grayscale;
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

        .social-btn:hover {
            background: rgba(255, 255, 255, 0.15);
            border-color: rgba(255, 255, 255, 0.3);
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

        .form-input:focus {
            border-color: #22d3ee;
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
            font-size: 22px;
            font-weight: 800;
            color: #ffffff;
            line-height: 1.2;
            margin-bottom: 6px;
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

        .wizard-body::-webkit-scrollbar {
            width: 4px;
        }
        .wizard-body::-webkit-scrollbar-thumb {
            background: rgba(255, 255, 255, 0.2);
            border-radius: 4px;
        }

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

        .dash-btn-invite {
            background: #f1f5f9;
            border: 1px solid #cbd5e1;
            padding: 8px 14px;
            border-radius: 8px;
            font-size: 13px;
            font-weight: 600;
            color: #334155;
            cursor: pointer;
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
            transition: transform 0.1s ease;
        }
        
        .project-card:hover {
            border-color: #22d3ee;
        }

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
        
        .create-project-box:hover {
            border-color: #0f172a;
            color: #0f172a;
        }

        /* WAVEFORM STYLES */
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

<audio id="audioElement" src="https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3" preload="auto"></audio>

<div id="toast">Berjaya!</div>

<div class="app-container">

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
            <div style="text-align: center; margin-bottom: 10px;">
                <a href="#" style="font-size: 12px; color: #22d3ee; text-decoration: none;">Lupa kata laluan?</a>
            </div>
        </div>

        <div>
            <button class="btn-primary" onclick="nextScreen('wizardStep1')">Log Masuk</button>
            <div style="text-align: center; font-size: 12px; color: #94a3b8; margin-top: 12px;">
                Belum ada akaun? <span style="color: #22d3ee; cursor: pointer;" onclick="nextScreen('wizardStep1')">Daftar sekarang</span>
            </div>
        </div>
    </div>

    <div id="wizardStep1" class="screen-overlay hidden">
        <div>
            <div class="wizard-step-indicator">1/5</div>
            <div class="wizard-title">Selamat datang! Apa yang anda ingin buat dahulu?</div>
            <div class="wizard-subtitle">Beritahu kami keperluan anda supaya kami boleh bantu anda manfaatkan studio sepenuhnya.</div>
        </div>
        <div class="wizard-body">
            <div class="pill-grid">
                <div class="pill-option active" onclick="selectPill(this)">🎚️ Mastering</div>
                <div class="pill-option" onclick="selectPill(this)">🌍 Distribution</div>
                <div class="pill-option" onclick="selectPill(this)">🎵 Samples</div>
                <div class="pill-option" onclick="selectPill(this)">🔌 Plugins</div>
            </div>
        </div>
        <div class="wizard-footer">
            <button class="btn-text" onclick="nextScreen('screenLogin')">← Kembali</button>
            <button class="btn-primary" style="width: auto; padding: 10px 24px; margin: 0;" onclick="nextScreen('wizardStep2')">Seterusnya →</button>
        </div>
    </div>

    <div id="wizardStep2" class="screen-overlay hidden">
        <div>
            <div class="wizard-step-indicator">2/5</div>
            <div class="wizard-title">Mari tetapkan Profil Studio anda</div>
            <div class="wizard-subtitle">Sertai dan berhubung dengan komuniti pencipta muzik dalam ekosistem awan kami.</div>
        </div>
        <div class="wizard-body">
            <div class="form-group">
                <label style="font-size: 11px; color: #22d3ee; font-weight: 600; display: block; margin-bottom: 6px;">NAMA ANDA / ARTIS</label>
                <input type="text" class="form-input" value="Boyz">
            </div>
            <div class="form-group">
                <label style="font-size: 11px; color: #22d3ee; font-weight: 600; display: block; margin-bottom: 6px;">URL PROFIL STUDIO</label>
                <input type="text" class="form-input" value="network.bpstudio.com/users/boyz" readonly style="color: #60a5fa;">
                <span style="font-size: 11px; color: #10b981; margin-top: 4px; display: block; text-align: center;">✓ URL tersedia</span>
            </div>
        </div>
        <div class="wizard-footer">
            <button class="btn-text" onclick="nextScreen('wizardStep1')">← Kembali</button>
            <button class="btn-primary" style="width: auto; padding: 10px 24px; margin: 0;" onclick="nextScreen('wizardStep3')">Seterusnya →</button>
        </div>
    </div>

    <div id="wizardStep3" class="screen-overlay hidden">
        <div>
            <div class="wizard-step-indicator">3/5</div>
            <div class="wizard-title">Apakah peranan utama anda?</div>
            <div class="wizard-subtitle">Pamerkan kepakaran anda dan berhubung dengan komuniti pencipta muzik.</div>
        </div>
        <div class="wizard-body">
            <div class="pill-grid">
                <div class="pill-option active" onclick="toggleMulti(this)">Producer</div>
                <div class="pill-option" onclick="toggleMulti(this)">Musician</div>
                <div class="pill-option" onclick="toggleMulti(this)">Engineer</div>
                <div class="pill-option" onclick="toggleMulti(this)">Beatmaker</div>
                <div class="pill-option" onclick="toggleMulti(this)">Vocalist</div>
                <div class="pill-option" onclick="toggleMulti(this)">Composer</div>
                <div class="pill-option" onclick="toggleMulti(this)">Podcaster</div>
            </div>
        </div>
        <div class="wizard-footer">
            <button class="btn-text" onclick="nextScreen('wizardStep2')">← Kembali</button>
            <button class="btn-primary" style="width: auto; padding: 10px 24px; margin: 0;" onclick="nextScreen('wizardStep4')">Seterusnya →</button>
        </div>
    </div>

    <div id="wizardStep4" class="screen-overlay hidden">
        <div>
            <div class="wizard-step-indicator">5/5</div>
            <div class="wizard-title">Pick your favorite genres</div>
            <div class="wizard-subtitle">Pilih gaya & genre kegemaran anda untuk tetapan AI tersuai.</div>
        </div>
        
        <div class="wizard-body">
            <div class="genre-category-title">🇲🇾 Melayu / Nusantara</div>
            <div class="pill-grid">
                <div class="pill-option active" onclick="toggleMulti(this)">Malaya / Melayu</div>
                <div class="pill-option" onclick="toggleMulti(this)">Pop Melayu</div>
                <div class="pill-option" onclick="toggleMulti(this)">Rock Melayu</div>
                <div class="pill-option" onclick="toggleMulti(this)">Balada Melayu</div>
                <div class="pill-option" onclick="toggleMulti(this)">Melayu Klasik</div>
                <div class="pill-option" onclick="toggleMulti(this)">Irama Malaysia</div>
                <div class="pill-option" onclick="toggleMulti(this)">Lagu Asli</div>
                <div class="pill-option" onclick="toggleMulti(this)">Zapin</div>
                <div class="pill-option" onclick="toggleMulti(this)">Joget</div>
                <div class="pill-option" onclick="toggleMulti(this)">Ghazal</div>
                <div class="pill-option" onclick="toggleMulti(this)">Keroncong</div>
                <div class="pill-option" onclick="toggleMulti(this)">Dangdut</div>
                <div class="pill-option" onclick="toggleMulti(this)">Campursari</div>
                <div class="pill-option" onclick="toggleMulti(this)">Pop Nusantara</div>
                <div class="pill-option" onclick="toggleMulti(this)">Etnik Nusantara</div>
                <div class="pill-option" onclick="toggleMulti(this)">Tradisional Melayu</div>
                       <div class="pill-option" onclick="toggleMulti(this)">Tradisional Sabah</div>
                <div class="pill-option" onclick="toggleMulti(this)">Tradisional Sarawak</div>
                <div class="pill-option" onclick="toggleMulti(this)">Minang</div>
                <div class="pill-option" onclick="toggleMulti(this)">Jawa</div>
                <div class="pill-option" onclick="toggleMulti(this)">Sunda</div>
                <div class="pill-option" onclick="toggleMulti(this)">Bugis</div>
                <div class="pill-option" onclick="toggleMulti(this)">Batak</div>
                <div class="pill-option" onclick="toggleMulti(this)">Malay Bounce</div>
                <div class="pill-option" onclick="toggleMulti(this)">Malay Trap</div>
                <div class="pill-option" onclick="toggleMulti(this)">Malay Phonk</div>
                <div class="pill-option" onclick="toggleMulti(this)">Malay Electronic</div>
                <div class="pill-option" onclick="toggleMulti(this)">Nusantara Electronic</div>
            </div>

            <div class="genre-category-title">🎤 Pop</div>
            <div class="pill-grid">
                <div class="pill-option" onclick="toggleMulti(this)">Pop</div>
                <div class="pill-option" onclick="toggleMulti(this)">Pop Ballad</div>
                <div class="pill-option" onclick="toggleMulti(this)">Electropop</div>
                <div class="pill-option" onclick="toggleMulti(this)">Synthpop</div>
                <div class="pill-option" onclick="toggleMulti(this)">Dream Pop</div>
                <div class="pill-option" onclick="toggleMulti(this)">Indie Pop</div>
                <div class="pill-option" onclick="toggleMulti(this)">Teen Pop</div>
                <div class="pill-option" onclick="toggleMulti(this)">Adult Contemporary</div>
                <div class="pill-option" onclick="toggleMulti(this)">Dance Pop</div>
                <div class="pill-option" onclick="toggleMulti(this)">Power Pop</div>
                <div class="pill-option" onclick="toggleMulti(this)">Soft Pop</div>
                <div class="pill-option" onclick="toggleMulti(this)">Retro Pop</div>
                <div class="pill-option" onclick="toggleMulti(this)">City Pop</div>
                <div class="pill-option" onclick="toggleMulti(this)">Dark Pop</div>
                <div class="pill-option" onclick="toggleMulti(this)">Noir Pop</div>
                <div class="pill-option" onclick="toggleMulti(this)">Future Pop</div>
                <div class="pill-option" onclick="toggleMulti(this)">Neon Pop</div>
                <div class="pill-option" onclick="toggleMulti(this)">Experimental Pop</div>
            </div>

            <div class="genre-category-title">🎸 Rock</div>
            <div class="pill-grid">
                <div class="pill-option" onclick="toggleMulti(this)">Rock</div>
                <div class="pill-option" onclick="toggleMulti(this)">Soft Rock</div>
                <div class="pill-option" onclick="toggleMulti(this)">Classic Rock</div>
                <div class="pill-option" onclick="toggleMulti(this)">Hard Rock</div>
                <div class="pill-option" onclick="toggleMulti(this)">Alternative Rock</div>
                <div class="pill-option" onclick="toggleMulti(this)">Indie Rock</div>
                <div class="pill-option" onclick="toggleMulti(this)">Pop Rock</div>
                <div class="pill-option" onclick="toggleMulti(this)">Blues Rock</div>
                <div class="pill-option" onclick="toggleMulti(this)">Progressive Rock</div>
                <div class="pill-option" onclick="toggleMulti(this)">Psychedelic Rock</div>
                <div class="pill-option" onclick="toggleMulti(this)">Punk Rock</div>
                <div class="pill-option" onclick="toggleMulti(this)">Garage Rock</div>
                <div class="pill-option" onclick="toggleMulti(this)">Grunge</div>
                <div class="pill-option" onclick="toggleMulti(this)">Post-Rock</div>
                <div class="pill-option" onclick="toggleMulti(this)">Folk Rock</div>
                <div class="pill-option" onclick="toggleMulti(this)">Southern Rock</div>
                <div class="pill-option" onclick="toggleMulti(this)">Glam Rock</div>
                <div class="pill-option" onclick="toggleMulti(this)">Arena Rock</div>
                <div class="pill-option" onclick="toggleMulti(this)">Metal Rock</div>
            </div>

            <div class="genre-category-title">🎤 Hip Hop / Rap</div>
            <div class="pill-grid">
                <div class="pill-option" onclick="toggleMulti(this)">Hip Hop</div>
                <div class="pill-option" onclick="toggleMulti(this)">Rap</div>
                <div class="pill-option" onclick="toggleMulti(this)">Old School Hip Hop</div>
                <div class="pill-option" onclick="toggleMulti(this)">Trap</div>
                <div class="pill-option" onclick="toggleMulti(this)">Boom Bap</div>
                <div class="pill-option" onclick="toggleMulti(this)">Lo-Fi Hip Hop</div>
                <div class="pill-option" onclick="toggleMulti(this)">Gangsta Rap</div>
                <div class="pill-option" onclick="toggleMulti(this)">Conscious Rap</div>
                <div class="pill-option" onclick="toggleMulti(this)">Melodic Rap</div>
                <div class="pill-option" onclick="toggleMulti(this)">Pop Rap</div>
                <div class="pill-option" onclick="toggleMulti(this)">Alternative Hip Hop</div>
                <div class="pill-option" onclick="toggleMulti(this)">R&B Rap</div>
                <div class="pill-option" onclick="toggleMulti(this)">Drill</div>
                <div class="pill-option" onclick="toggleMulti(this)">West Coast Hip Hop</div>
                <div class="pill-option" onclick="toggleMulti(this)">East Coast Hip Hop</div>
                <div class="pill-option" onclick="toggleMulti(this)">UK Drill</div>
                <div class="pill-option" onclick="toggleMulti(this)">Afro Drill</div>
                <div class="pill-option" onclick="toggleMulti(this)">Cyberpunk Trap</div>
                <div class="pill-option" onclick="toggleMulti(this)">Cinematic Trap</div>
                <div class="pill-option" onclick="toggleMulti(this)">Hybrid Trap</div>
            </div>

            <div class="genre-category-title">🔥 Phonk</div>
            <div class="pill-grid">
                <div class="pill-option" onclick="toggleMulti(this)">Phonk</div>
                <div class="pill-option" onclick="toggleMulti(this)">Dark Phonk</div>
                <div class="pill-option" onclick="toggleMulti(this)">Drift Phonk</div>
                <div class="pill-option" onclick="toggleMulti(this)">Brazilian Phonk</div>
                <div class="pill-option" onclick="toggleMulti(this)">Memphis Phonk</div>
                <div class="pill-option" onclick="toggleMulti(this)">Aggressive Phonk</div>
                <div class="pill-option" onclick="toggleMulti(this)">Atmospheric Phonk</div>
                <div class="pill-option" onclick="toggleMulti(this)">Electro Phonk</div>
                <div class="pill-option" onclick="toggleMulti(this)">Trap Phonk</div>
                <div class="pill-option" onclick="toggleMulti(this)">Future Phonk</div>
                <div class="pill-option" onclick="toggleMulti(this)">Malay Phonk</div>
                <div class="pill-option" onclick="toggleMulti(this)">Neon Noir Phonk</div>
                <div class="pill-option" onclick="toggleMulti(this)">Neon Noir Phonk - Malay Bounce</div>
                <div class="pill-option" onclick="toggleMulti(this)">Dark Techno / Neon Noir Phonk - Malay Bounce</div>
            </div>

            <div class="genre-category-title">⚡ Techno / Electronic</div>
            <div class="pill-grid">
                <div class="pill-option" onclick="toggleMulti(this)">EDM</div>
                <div class="pill-option" onclick="toggleMulti(this)">Techno</div>
                <div class="pill-option" onclick="toggleMulti(this)">Dark Techno</div>
                <div class="pill-option" onclick="toggleMulti(this)">Hard Techno</div>
                <div class="pill-option" onclick="toggleMulti(this)">Industrial Techno</div>
                <div class="pill-option" onclick="toggleMulti(this)">Acid Techno</div>
                <div class="pill-option" onclick="toggleMulti(this)">Minimal Techno</div>
                <div class="pill-option" onclick="toggleMulti(this)">Melodic Techno</div>
                <div class="pill-option" onclick="toggleMulti(this)">Progressive Techno</div>
                <div class="pill-option" onclick="toggleMulti(this)">Techno Noir</div>
                <div class="pill-option" onclick="toggleMulti(this)">Cyber Techno</div>
                <div class="pill-option" onclick="toggleMulti(this)">House</div>
                <div class="pill-option" onclick="toggleMulti(this)">Deep House</div>
                <div class="pill-option" onclick="toggleMulti(this)">Tropical House</div>
                <div class="pill-option" onclick="toggleMulti(this)">Future House</div>
                <div class="pill-option" onclick="toggleMulti(this)">Progressive House</div>
                <div class="pill-option" onclick="toggleMulti(this)">Tech House</div>
                <div class="pill-option" onclick="toggleMulti(this)">Electro House</div>
                <div class="pill-option" onclick="toggleMulti(this)">Bass House</div>
                <div class="pill-option" onclick="toggleMulti(this)">G-House</div>
                <div class="pill-option" onclick="toggleMulti(this)">Slap House</div>
                <div class="pill-option" onclick="toggleMulti(this)">Afro House</div>
                <div class="pill-option" onclick="toggleMulti(this)">Trance</div>
                <div class="pill-option" onclick="toggleMulti(this)">Dubstep</div>
                <div class="pill-option" onclick="toggleMulti(this)">Drum & Bass</div>
                <div class="pill-option" onclick="toggleMulti(this)">Future Bass</div>
                <div class="pill-option" onclick="toggleMulti(this)">Breakbeat</div>
                <div class="pill-option" onclick="toggleMulti(this)">UK Garage</div>
                <div class="pill-option" onclick="toggleMulti(this)">Jersey Club</div>
                <div class="pill-option" onclick="toggleMulti(this)">Amapiano</div>
                <div class="pill-option" onclick="toggleMulti(this)">Industrial Bass</div>
                <div class="pill-option" onclick="toggleMulti(this)">Dark Electro</div>
                <div class="pill-option" onclick="toggleMulti(this)">Alternative Electronic</div>
                <div class="pill-option" onclick="toggleMulti(this)">Cinematic Electronic</div>
            </div>

            <div class="genre-category-title">🌑 Dark / Cyber / Experimental</div>
            <div class="pill-grid">
                <div class="pill-option" onclick="toggleMulti(this)">Darkwave</div>
                <div class="pill-option" onclick="toggleMulti(this)">Witch House</div>
                <div class="pill-option" onclick="toggleMulti(this)">Dark Synthwave</div>
                <div class="pill-option" onclick="toggleMulti(this)">Neon Synthwave</div>
                <div class="pill-option" onclick="toggleMulti(this)">Synthwave</div>
                <div class="pill-option" onclick="toggleMulti(this)">Vaporwave</div>
                <div class="pill-option" onclick="toggleMulti(this)">Cyberpunk</div>
                <div class="pill-option" onclick="toggleMulti(this)">Cyber Pop</div>
                <div class="pill-option" onclick="toggleMulti(this)">Cyberpunk Trap</div>
                <div class="pill-option" onclick="toggleMulti(this)">Noir Electronic</div>
                <div class="pill-option" onclick="toggleMulti(this)">Dark Ambient</div>
                <div class="pill-option" onclick="toggleMulti(this)">Ambient Dark</div>
                <div class="pill-option" onclick="toggleMulti(this)">Horror Electronic</div>
                <div class="pill-option" onclick="toggleMulti(this)">Atmospheric</div>
                <div class="pill-option" onclick="toggleMulti(this)">Experimental Electronic</div>
                <div class="pill-option" onclick="toggleMulti(this)">Experimental Pop</div>
                <div class="pill-option" onclick="toggleMulti(this)">Future Garage</div>
                <div class="pill-option" onclick="toggleMulti(this)">Industrial</div>
                <div class="pill-option" onclick="toggleMulti(this)">Noise</div>
                <div class="pill-option" onclick="toggleMulti(this)">Glitch</div>
                <div class="pill-option" onclick="toggleMulti(this)">Glitch Hop</div>
            </div>

            <div class="genre-category-title">🎷 R&B / Soul / Funk</div>
            <div class="pill-grid">
                <div class="pill-option" onclick="toggleMulti(this)">R&B</div>
                <div class="pill-option" onclick="toggleMulti(this)">Contemporary R&B</div>
                <div class="pill-option" onclick="toggleMulti(this)">Soul</div>
                <div class="pill-option" onclick="toggleMulti(this)">Neo Soul</div>
                <div class="pill-option" onclick="toggleMulti(this)">Motown</div>
                <div class="pill-option" onclick="toggleMulti(this)">Funk</div>
                <div class="pill-option" onclick="toggleMulti(this)">Smooth Soul</div>
                <div class="pill-option" onclick="toggleMulti(this)">Gospel Soul</div>
                <div class="pill-option" onclick="toggleMulti(this)">R&B Ballad</div>
                <div class="pill-option" onclick="toggleMulti(this)">Funk Soul</div>
            </div>

            <div class="genre-category-title">🎷 Jazz / Blues</div>
            <div class="pill-grid">
                <div class="pill-option" onclick="toggleMulti(this)">Jazz</div>
                <div class="pill-option" onclick="toggleMulti(this)">Smooth Jazz</div>
                <div class="pill-option" onclick="toggleMulti(this)">Contemporary Jazz</div>
                <div class="pill-option" onclick="toggleMulti(this)">Swing</div>
                <div class="pill-option" onclick="toggleMulti(this)">Bebop</div>
                <div class="pill-option" onclick="toggleMulti(this)">Fusion Jazz</div>
                <div class="pill-option" onclick="toggleMulti(this)">Latin Jazz</div>
                <div class="pill-option" onclick="toggleMulti(this)">Blues</div>
                <div class="pill-option" onclick="toggleMulti(this)">Slow Blues</div>
                <div class="pill-option" onclick="toggleMulti(this)">Blues Rock</div>
                <div class="pill-option" onclick="toggleMulti(this)">Soul Blues</div>
            </div>
               <div class="genre-category-title">🎸 Akustik / Folk</div>
            <div class="pill-grid">
                <div class="pill-option" onclick="toggleMulti(this)">Acoustic</div>
                <div class="pill-option" onclick="toggleMulti(this)">Acoustic Pop</div>
                <div class="pill-option" onclick="toggleMulti(this)">Acoustic Ballad</div>
                <div class="pill-option" onclick="toggleMulti(this)">Folk</div>
                <div class="pill-option" onclick="toggleMulti(this)">Indie Folk</div>
                <div class="pill-option" onclick="toggleMulti(this)">Folk Pop</div>
                <div class="pill-option" onclick="toggleMulti(this)">Singer-Songwriter</div>
                <div class="pill-option" onclick="toggleMulti(this)">Coffeehouse</div>
                <div class="pill-option" onclick="toggleMulti(this)">Chill</div>
                <div class="pill-option" onclick="toggleMulti(this)">Lo-Fi</div>
                <div class="pill-option" onclick="toggleMulti(this)">Lounge</div>
                <div class="pill-option" onclick="toggleMulti(this)">Relaxing</div>
            </div>

            <div class="genre-category-title">🎻 Orkestra / Klasik</div>
            <div class="pill-grid">
                <div class="pill-option" onclick="toggleMulti(this)">Classical</div>
                <div class="pill-option" onclick="toggleMulti(this)">Piano Solo</div>
                <div class="pill-option" onclick="toggleMulti(this)">Piano Ballad</div>
                <div class="pill-option" onclick="toggleMulti(this)">String Orchestra</div>
                <div class="pill-option" onclick="toggleMulti(this)">Symphony</div>
                <div class="pill-option" onclick="toggleMulti(this)">Chamber Music</div>
                <div class="pill-option" onclick="toggleMulti(this)">Cinematic</div>
                <div class="pill-option" onclick="toggleMulti(this)">Epic Orchestra</div>
                <div class="pill-option" onclick="toggleMulti(this)">Film Score</div>
                <div class="pill-option" onclick="toggleMulti(this)">Dramatic</div>
                <div class="pill-option" onclick="toggleMulti(this)">Emotional Orchestra</div>
                <div class="pill-option" onclick="toggleMulti(this)">Fantasy</div>
                <div class="pill-option" onclick="toggleMulti(this)">Medieval</div>
                <div class="pill-option" onclick="toggleMulti(this)">Baroque</div>
            </div>

            <div class="genre-category-title">❤️ Sedih / Emosi / Cinta</div>
            <div class="pill-grid">
                <div class="pill-option" onclick="toggleMulti(this)">Sad Song</div>
                <div class="pill-option" onclick="toggleMulti(this)">Emotional</div>
                <div class="pill-option" onclick="toggleMulti(this)">Heartbreak</div>
                <div class="pill-option" onclick="toggleMulti(this)">Melancholic</div>
                <div class="pill-option" onclick="toggleMulti(this)">Nostalgic</div>
                <div class="pill-option" onclick="toggleMulti(this)">Romantic</div>
                <div class="pill-option" onclick="toggleMulti(this)">Love Song</div>
                <div class="pill-option" onclick="toggleMulti(this)">Deep Emotional</div>
                <div class="pill-option" onclick="toggleMulti(this)">Tearjerker</div>
                <div class="pill-option" onclick="toggleMulti(this)">Slow Ballad</div>
                <div class="pill-option" onclick="toggleMulti(this)">Emotional Piano</div>
                <div class="pill-option" onclick="toggleMulti(this)">Emotional Acoustic</div>
                <div class="pill-option" onclick="toggleMulti(this)">Power Ballad</div>
            </div>

            <div class="genre-category-title">🌎 Antarabangsa</div>
            <div class="pill-grid">
                <div class="pill-option" onclick="toggleMulti(this)">K-Pop</div>
                <div class="pill-option" onclick="toggleMulti(this)">J-Pop</div>
                <div class="pill-option" onclick="toggleMulti(this)">C-Pop</div>
                <div class="pill-option" onclick="toggleMulti(this)">Bollywood</div>
                <div class="pill-option" onclick="toggleMulti(this)">Latin Pop</div>
                <div class="pill-option" onclick="toggleMulti(this)">Reggaeton</div>
                <div class="pill-option" onclick="toggleMulti(this)">Salsa</div>
                <div class="pill-option" onclick="toggleMulti(this)">Bachata</div>
                <div class="pill-option" onclick="toggleMulti(this)">Flamenco</div>
                <div class="pill-option" onclick="toggleMulti(this)">Afrobeat</div>
                <div class="pill-option" onclick="toggleMulti(this)">Afropop</div>
                <div class="pill-option" onclick="toggleMulti(this)">Reggae</div>
                <div class="pill-option" onclick="toggleMulti(this)">Dancehall</div>
                <div class="pill-option" onclick="toggleMulti(this)">Ska</div>
                <div class="pill-option" onclick="toggleMulti(this)">Country</div>
                <div class="pill-option" onclick="toggleMulti(this)">Country Pop</div>
                <div class="pill-option" onclick="toggleMulti(this)">Bluegrass</div>
                <div class="pill-option" onclick="toggleMulti(this)">Gospel</div>
                <div class="pill-option" onclick="toggleMulti(this)">Celtic</div>
                <div class="pill-option" onclick="toggleMulti(this)">Arabic</div>
                <div class="pill-option" onclick="toggleMulti(this)">Middle Eastern</div>
            </div>

            <div class="genre-category-title">🤘 Metal</div>
            <div class="pill-grid">
                <div class="pill-option" onclick="toggleMulti(this)">Heavy Metal</div>
                <div class="pill-option" onclick="toggleMulti(this)">Metalcore</div>
                <div class="pill-option" onclick="toggleMulti(this)">Death Metal</div>
                <div class="pill-option" onclick="toggleMulti(this)">Black Metal</div>
                <div class="pill-option" onclick="toggleMulti(this)">Symphonic Metal</div>
                <div class="pill-option" onclick="toggleMulti(this)">Power Metal</div>
                <div class="pill-option" onclick="toggleMulti(this)">Progressive Metal</div>
                <div class="pill-option" onclick="toggleMulti(this)">Nu Metal</div>
                <div class="pill-option" onclick="toggleMulti(this)">Alternative Metal</div>
                <div class="pill-option" onclick="toggleMulti(this)">Doom Metal</div>
            </div>

            <div class="genre-category-title">🎬 Cinematic / Mood / Khas</div>
            <div class="pill-grid">
                <div class="pill-option" onclick="toggleMulti(this)">Cinematic</div>
                <div class="pill-option" onclick="toggleMulti(this)">Epic</div>
                <div class="pill-option" onclick="toggleMulti(this)">Dark</div>
                <div class="pill-option" onclick="toggleMulti(this)">Mysterious</div>
                <div class="pill-option" onclick="toggleMulti(this)">Horror</div>
                <div class="pill-option" onclick="toggleMulti(this)">Thriller</div>
                <div class="pill-option" onclick="toggleMulti(this)">Adventure</div>
                <div class="pill-option" onclick="toggleMulti(this)">Fantasy</div>
                <div class="pill-option" onclick="toggleMulti(this)">Heroic</div>
                <div class="pill-option" onclick="toggleMulti(this)">Inspirational</div>
                <div class="pill-option" onclick="toggleMulti(this)">Motivational</div>
                <div class="pill-option" onclick="toggleMulti(this)">Spiritual</div>
                <div class="pill-option" onclick="toggleMulti(this)">Religious</div>
                <div class="pill-option" onclick="toggleMulti(this)">Peaceful</div>
                <div class="pill-option" onclick="toggleMulti(this)">Meditation</div>
                <div class="pill-option" onclick="toggleMulti(this)">Atmospheric</div>
                <div class="pill-option" onclick="toggleMulti(this)">Dreamy</div>
                <div class="pill-option" onclick="toggleMulti(this)">Powerful</div>
                <div class="pill-option" onclick="toggleMulti(this)">Energetic</div>
                <div class="pill-option" onclick="toggleMulti(this)">Romantic</div>
                <div class="pill-option" onclick="toggleMulti(this)">Vintage</div>
                <div class="pill-option" onclick="toggleMulti(this)">Retro</div>
                <div class="pill-option" onclick="toggleMulti(this)">80s</div>
                <div class="pill-option" onclick="toggleMulti(this)">90s</div>
                <div class="pill-option" onclick="toggleMulti(this)">Nostalgic</div>
                <div class="pill-option" onclick="toggleMulti(this)">Wedding</div>
                <div class="pill-option" onclick="toggleMulti(this)">Festival</div>
                <div class="pill-option" onclick="toggleMulti(this)">Party</div>
                <div class="pill-option" onclick="toggleMulti(this)">Christmas</div>
                <div class="pill-option" onclick="toggleMulti(this)">Raya / Aidilfitri</div>
            </div>
        </div>

        <div class="wizard-footer">
            <button class="btn-text" onclick="nextScreen('wizardStep3')">← Kembali</button>
            <button class="btn-primary" style="width: auto; padding: 10px 24px; margin: 0;" onclick="finishWizard()">Continue</button>
        </div>
    </div>

    <div id="screenAIPrompt" class="screen-overlay hidden">
        <div>
            <div class="wizard-step-indicator">AI STUDIO</div>
            <div class="wizard-title">Jana Gubahan Muzik AI</div>
            <div class="wizard-subtitle">Taip konsep lagu anda atau biarkan AI gubah rentak mengikut gaya pilihan anda.</div>
        </div>
        
        <div class="wizard-body">
            <div class="form-group">
                <label style="font-size: 11px; color: #22d3ee; font-weight: 600; display: block; margin-bottom: 6px;">KONSEP / LIRIK / DESKRIPSI LAGU</label>
                <textarea class="form-input" id="songPromptText" style="height: 100px; text-align: left; resize: none;" placeholder="Contoh: Lagu pop melayu santai tentang perjalanan malam di Johor dengan sentuhan Malay Bounce..."></textarea>
            </div>

            <div class="genre-category-title">Pilih Vibe Utama Anda</div>
            <div class="pill-grid">
                <div class="pill-option active" onclick="toggleMulti(this)">Malay Bounce</div>
                <div class="pill-option" onclick="toggleMulti(this)">Malay Phonk</div>
                <div class="pill-option" onclick="toggleMulti(this)">Pop Melayu</div>
                <div class="pill-option" onclick="toggleMulti(this)">Cinematic</div>
            </div>

            <div id="generationStatus" style="margin-top: 15px; padding: 12px; background: rgba(34, 211, 238, 0.1); border: 1px solid rgba(34, 211, 238, 0.3); border-radius: 10px; font-size: 12px; color: #22d3ee; display: none; text-align: center;">
                ⚡ AI sedang menggubah trek muzik anda... Sila tunggu sebentar.
            </div>
        </div>

        <div class="wizard-footer">
            <button class="btn-text" onclick="nextScreen('dashboardScreen')">← Kembali</button>
            <button class="btn-primary" style="width: auto; padding: 10px 24px; margin: 0;" onclick="generateMusicAI()">Jana Muzik 🎵</button>
        </div>
    </div>

    <div id="screenAudioPlayer" class="screen-overlay hidden">
        <div>
            <div class="wizard-step-indicator">PLAYER & STEMS</div>
            <div class="wizard-title">Projek Malay Bounce Studio</div>
            <div class="wizard-subtitle">Pratonton audio masa sebenar & fail stems yang dijana AI.</div>
        </div>
        
        <div class="wizard-body">
            <div class="waveform-box" id="waveformBox">
                <div style="font-size: 11px; color: #94a3b8; font-weight: 600;">WAVEFORM VISUALIZER</div>
                <div class="waveform-bars">
                    <div class="wave-bar"></div>
                    <div class="wave-bar"></div>
                    <div class="wave-bar"></div>
                    <div class="wave-bar"></div>
                    <div class="wave-bar"></div>
                    <div class="wave-bar"></div>
                    <div class="wave-bar"></div>
                    <div class="wave-bar"></div>
                    <div class="wave-bar"></div>
                    <div class="wave-bar"></div>
                </div>
                <div style="font-size: 13px; font-weight: 700; color: #22d3ee;" id="playerTime">00:00 / 03:45</div>

                <div class="player-controls">
                    <button class="control-btn-main" id="playPauseBtn" onclick="togglePlayAudio()">▶</button>
                </div>
            </div>

            <div class="genre-category-title">Fail Stems Berasingan</div>
            <div class="stems-list">
                <div class="stem-item">
                    <span>🎙️ Vokal Utama (AI)</span>
                    <button class="btn-text" style="color: #22d3ee;" onclick="showToast('Muat turun stem Vokal...')">Muat Turun ⬇</button>
                </div>
                <div class="stem-item">
                    <span>🥁 Drum & Percussion</span>
                    <button class="btn-text" style="color: #22d3ee;" onclick="showToast('Muat turun stem Drum...')">Muat Turun ⬇</button>
                </div>
                <div class="stem-item">
                    <span>🎸 Bass Line</span>
                    <button class="btn-text" style="color: #22d3ee;" onclick="showToast('Muat turun stem Bass...')">Muat Turun ⬇</button>
                </div>
                <div class="stem-item">
                    <span>🎹 Melodi & Synth</span>
                    <button class="btn-text" style="color: #22d3ee;" onclick="showToast('Muat turun stem Melodi...')">Muat Turun ⬇</button>
                </div>
            </div>
        </div>

        <div class="wizard-footer">
            <button class="btn-text" onclick="nextScreen('dashboardScreen')">← Kembali ke Dashboard</button>
            <button class="btn-primary" style="width: auto; padding: 10px 24px; margin: 0;" onclick="showToast('Master file berjaya dimuat turun!')">Muat Turun Master 🎵</button>
        </div>
    </div>

    <div id="dashboardScreen" class="dashboard-container hidden">
        <div class="dash-top-bar">
            <div class="workspace-badge">
                <span>🎧</span> Bangkit's workspace ▾
            </div>
            <div style="display: flex; gap: 12px; align-items: center; font-size: 16px;">
                <span>🔍</span>
                <span style="background: #e2e8f0; width: 28px; height: 28px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 12px; font-weight: 700;">B</span>
            </div>
        </div>

        <h1 style="font-family: 'Syne', sans-serif; font-size: 26px; font-weight: 800; margin: 0 0 16px 0;">Overview</h1>

        <div class="dash-actions">
            <button class="dash-btn-invite" onclick="showToast('Pautan jemputan disalin!')">👤 Invite your team</button>
            <button class="dash-btn-new" onclick="nextScreen('screenAIPrompt')">+ New ▾</button>
        </div>

        <h3 style="font-size: 14px; font-weight: 700; color: #475569; margin-bottom: 12px;">Projects</h3>

        <div class="project-card" onclick="nextScreen('screenAudioPlayer')">
            <div style="font-weight: 700; font-size: 15px;">Projek Malay Bounce Studio</div>
            <div style="font-size: 12px; color: #64748b; margin-top: 4px;">Klik untuk buka pemain audio & stems 🎧</div>
            <div class="project-status">
                ✓ All services are up and running
            </div>
        </div>

        <div class="create-project-box" onclick="nextScreen('screenAIPrompt')">
            + Create new project
        </div>

        <div style="margin-top: auto; text-align: center; padding-top: 20px;">
            <button class="btn-text" style="color: #64748b;" onclick="nextScreen('screenLogin')">Log Keluar</button>
        </div>
    </div>

</div>

<script>
    function showToast(msg) {
        let t = document.getElementById('toast');
        t.innerText = msg;
        t.style.opacity = '1';
        setTimeout(() => { t.style.opacity = '0'; }, 2000);
    }

    function nextScreen(screenId) {
        // Jeda audio jika keluar dari skrin player
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

    function toggleMulti(el) {
        el.classList.toggle('active');
    }

    function finishWizard() {
        showToast("Tetapan profil & genre berjaya disimpan!");
        setTimeout(() => {
            nextScreen('dashboardScreen');
        }, 1200);
    }

    function generateMusicAI() {
        let promptText = document.getElementById('songPromptText').value;
        if (!promptText.trim()) {
            showToast("Sila masukkan deskripsi lagu dahulu!");
            return;
        }

        let statusBox = document.getElementById('generationStatus');
        statusBox.style.display = 'block';
        showToast("Proses gubahan AI bermula...");

        setTimeout(() => {
            statusBox.style.display = 'none';
            showToast("Trek muzik berjaya dijana oleh AI!");
            setTimeout(() => {
                nextScreen('screenAudioPlayer');
            }, 1000);
        }, 2500);
    }

    let isPlaying = false;
    const audio = document.getElementById('audioElement');

    function togglePlayAudio() {
        let box = document.getElementById('waveformBox');
        let btn = document.getElementById('playPauseBtn');
        
        if (isPlaying) {
            audio.pause();
            box.classList.remove('playing');
            btn.innerText = '▶';
            showToast("Audio dijeda.");
            isPlaying = false;
        } else {
            audio.play().then(() => {
                box.classList.add('playing');
                btn.innerText = '⏸';
                showToast("Memainkan audio trek...");
                isPlaying = true;
            }).catch(e => {
                showToast("Sila klik skrin sekali lagi untuk kebenaran audio.");
            });
        }
    }

    // Kemas kini masa pemain audio secara masa sebenar
    audio.addEventListener('timeupdate', () => {
        let currentMinutes = Math.floor(audio.currentTime / 60);
        let currentSeconds = Math.floor(audio.currentTime % 60);
        let durMinutes = Math.floor(audio.duration / 60) || 3;
        let durSeconds = Math.floor(audio.duration % 60) || 45;

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
        
                
