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
            background: rgba(11, 15, 25, 0.75);
            backdrop-filter: blur(4px);
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
                <div class="pill-option" onclick="toggleMulti(this)">Roc
