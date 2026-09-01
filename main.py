from fastapi import FastAPI
from fastapi.responses import HTMLResponse, FileResponse
import os

app = FastAPI()

@app.get("/kl-background.jpg")
def get_kl_bg():
    if os.path.exists("kl-background.jpg"):
        return FileResponse("kl-background.jpg")
    return {"error": "Background image not found"}

@app.get("/", response_class=HTMLResponse)
def main_page():
    return """
<!DOCTYPE html>
<html lang="ms">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>BP AI Music Studio - Pro Suite</title>
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
        }

        /* Skrin 1: Latar Belakang Kuala Lumpur */
        #screenLogin {
            background-image: url('/kl-background.jpg');
            background-size: cover;
            background-position: center;
        }

        .screen-overlay {
            background: rgba(11, 15, 25, 0.82);
            backdrop-filter: blur(8px);
            flex: 1;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            padding: 28px 22px;
            box-sizing: border-box;
            min-height: 100vh;
            width: 100%;
        }

        /* Komponen Umum */
        .brand-logo {
            font-family: 'Syne', sans-serif;
            font-size: 22px;
            font-weight: 800;
            color: #ffffff;
            text-align: center;
            letter-spacing: 1px;
            margin-bottom: 20px;
        }

        .social-login-grid {
            display: flex;
            gap: 12px;
            width: 100%;
            margin-bottom: 20px;
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
        }

        .social-btn:hover {
            background: rgba(255, 255, 255, 0.15);
            border-color: rgba(255, 255, 255, 0.3);
        }

        .divider-text {
            text-align: center;
            font-size: 13px;
            color: #94a3b8;
            margin: 15px 0;
            position: relative;
        }

        .form-group {
            width: 100%;
            margin-bottom: 14px;
        }

        .form-input {
            background: rgba(15, 23, 42, 0.9);
            border: 1px solid rgba(255, 255, 255, 0.15);
            padding: 14px 18px;
            border-radius: 12px;
            width: 100%;
            color: #ffffff;
            font-size: 13px;
            font-family: 'Montserrat', sans-serif;
            box-sizing: border-box;
            outline: none;
            transition: border-color 0.2s;
        }

        .form-input:focus {
            border-color: #22d3ee;
            box-shadow: 0 0 10px rgba(34, 211, 238, 0.25);
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
            margin-top: 10px;
        }

        .btn-primary:hover {
            transform: translateY(-1px);
            box-shadow: 0 6px 20px rgba(34, 211, 238, 0.6);
        }

        /* Wizard Styles */
        .wizard-step-indicator {
            font-family: 'Syne', sans-serif;
            font-size: 13px;
            font-weight: 700;
            color: #22d3ee;
            letter-spacing: 1px;
            margin-bottom: 6px;
        }

        .wizard-title {
            font-family: 'Syne', sans-serif;
            font-size: 24px;
            font-weight: 800;
            color: #ffffff;
            line-height: 1.25;
            margin-bottom: 8px;
        }

        .wizard-subtitle {
            font-size: 13px;
            color: #94a3b8;
            line-height: 1.5;
            margin-bottom: 20px;
        }

        .wizard-body {
            flex: 1;
            width: 100%;
            overflow-y: auto;
            max-height: 60vh;
            padding-right: 4px;
        }

        /* Pill Grid ala LANDR */
        .pill-grid {
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
            width: 100%;
            margin-bottom: 20px;
        }

        .pill-option {
            background: rgba(255, 255, 255, 0.05);
            border: 1px solid rgba(255, 255, 255, 0.15);
            padding: 10px 18px;
            border-radius: 30px;
            font-size: 13px;
            font-weight: 500;
            color: #e2e8f0;
            cursor: pointer;
            transition: all 0.2s ease;
        }

        .pill-option:hover, .pill-option.active {
            background: rgba(34, 211, 238, 0.15);
            border-color: #22d3ee;
            color: #ffffff;
            box-shadow: 0 0 10px rgba(34, 211, 238, 0.2);
        }

        .wizard-footer {
            width: 100%;
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding-top: 16px;
            border-top: 1px solid rgba(255, 255, 255, 0.08);
            margin-top: auto;
        }

        .btn-text {
            background: none;
            border: none;
            color: #94a3b8;
            font-size: 13px;
            font-weight: 600;
            cursor: pointer;
        }
        .btn-text:hover { color: #ffffff; }

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
            pointer-events: none;
            z-index: 1000;
        }
    </style>
</head>
<body>

<div id="toast">Notifikasi</div>

<div class="app-container">

    <!-- SKRIN 1: LOGIN DENGAN LATAR BELAKANG KUALA LUMPUR -->
    <div id="screenLogin" class="screen-overlay">
        <div>
            <div class="brand-logo">BP AI MUSIC STUDIO</div>
            <div style="font-size: 12px; color: #94a3b8; text-align: center; margin-bottom: 24px;">Log masuk ke akaun profesional anda</div>
            
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
            <div style="text-align: right; margin-bottom: 15px;">
                <a href="#" style="font-size: 12px; color: #22d3ee; text-decoration: none;">Lupa kata laluan?</a>
            </div>
        </div>

        <div>
            <button class="btn-primary" onclick="nextScreen('wizardStep1')">Log Masuk</button>
            <div style="text-align: center; font-size: 12px; color: #94a3b8; margin-top: 15px;">
                Belum ada akaun? <span style="color: #22d3ee; cursor: pointer;" onclick="nextScreen('wizardStep1')">Daftar sekarang</span>
            </div>
        </div>
    </div>

    <!-- WIZARD STEP 1 (1/5): MATLAMAT UTAMA -->
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
                <div class="pill-option" onclick="selectPill(this)">👥 Finding collaborators</div>
                <div class="pill-option" onclick="selectPill(this)">💰 Selling my services</div>
            </div>
        </div>
        <div class="wizard-footer">
            <button class="btn-text" onclick="nextScreen('screenLogin')">← Kembali</button>
            <button class="btn-primary" style="width: auto; padding: 10px 24px; margin: 0;" onclick="nextScreen('wizardStep2')">Seterusnya →</button>
        </div>
    </div>

    <!-- WIZARD STEP 2 (2/5): PROFIL STUDIO -->
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
                <input type="text" class="form-input" value="network.bpstudio.com/users/boyz-15d0" readonly style="color: #60a5fa;">
                <span style="font-size: 11px; color: #10b981; margin-top: 4px; display: block;">✓ URL tersedia</span>
            </div>
        </div>
        <div class="wizard-footer">
            <button class="btn-text" onclick="nextScreen('wizardStep1')">← Kembali</button>
            <button class="btn-primary" style="width: auto; padding: 10px 24px; margin: 0;" onclick="nextScreen('wizardStep3')">Seterusnya →</button>
        </div>
    </div>

    <!-- WIZARD STEP 3 (3/5): PERANAN PROFESIONAL -->
    <div id="wizardStep3" class="screen-overlay hidden">
        <div>
            <div class="wizard-step-indicator">3/5</div>
            <div class="wizard-title">Apakah peranan utama anda?</div>
            <div class="wizard-subtitle">Pamerkan kepakaran anda dan berhubung dengan komuniti pencipta muzik yang sehaluan.</div>
        </div>
        <div class="wizard-body">
            <div class="pill-grid">
                <div class="pill-option active" onclick="toggleMulti(this)">Producer</div>
                <div class="pill-option" onclick="toggleMulti(this)">Musician</div>
                <div class="pill-option" onclick="toggleMulti(this)">Engineer</div>
                <div class="pill-option" onclick="toggleMulti(this)">Label</div>
                <div class="pill-option" onclick="toggleMulti(this)">Podcaster</div>
                <div class="pill-option" onclick="toggleMulti(this)">Educator</div>
                <div class="pill-option" onclick="toggleMulti(this)">Beatmaker</div>
                <div class="pill-option" onclick="toggleMulti(this)">Composer</div>
                <div class="pill-option" onclick="toggleMulti(this)">Vocalist</div>
                <div class="pill-option" onclick="toggleMulti(this)">Other</div>
            </div>
        </div>
        <div class="wizard-footer">
            <button class="btn-text" onclick="nextScreen('wizardStep2')">← Kembali</button>
            <button class="btn-primary" style="width: auto; padding: 10px 24px; margin: 0;" onclick="nextScreen('wizardStep4')">Seterusnya →</button>
        </div>
    </div>

    <!-- WIZARD STEP 4 (4/5 & 5/5): PILIHAN GENRE & STYLE (RUJUKAN TANGKAPAN SKRIN ANDA) -->
    <div id="wizardStep4" class="screen-overlay hidden">
        <div>
            <div class="wizard-step-indicator">5/5</div>
            <div class="wizard-title">Pick your favorite genres</div>
            <div class="wizard-subtitle">Tell us what types of music you're into and we'll make sure that you get to see (and hear) more stuff that you like.</div>
        </div>
        <div class="wizard-body">
            <div class="pill-grid">
                <div class="pill-option active" onclick="toggleMulti(this)">🇲🇾 Melayu / Nusantara</div>
                <div class="pill-option" onclick="toggleMulti(this)">Acoustic</div>
                <div class="pill-option" onclick="toggleMulti(this)">Afrobeat</div>
                <div class="pill-option" onclick="toggleMulti(this)">Americana</div>
                <div class="pill-option" onclick="toggleMulti(this)">Blues</div>
                <div class="pill-option" onclick="toggleMulti(this)">Chill</div>
                <div class="pill-option" onclick="toggleMulti(this)">Choral</div>
                <div class="pill-option" onclick="toggleMulti(this)">Classical</div>
                <div class="pill-option" onclick="toggleMulti(this)">Country</div>
                <div class="pill-option" onclick="toggleMulti(this)">Dubstep</div>
                <div class="pill-option" onclick="toggleMulti(this)">Edm</div>
                <div class="pill-option" onclick="toggleMulti(this)">Electric pop</div>
                <div class="pill-option" onclick="toggleMulti(this)">Electronic</div>
                <div class="pill-option" onclick="toggleMulti(this)">Folk</div>
                <div class="pill-option" onclick="toggleMulti(this)">Funk</div>
                <div class="pill-option" onclick="toggleMulti(this)">Gospel</div>
                <div class="pill-option" onclick="toggleMulti(this)">Heavy metal</div>
                <div class="pill-option" onclick="toggleMulti(this)">Heavy rock</div>
                <div class="pill-option" onclick="toggleMulti(this)">Hip hop</div>
                <div class="pill-option" onclick="toggleMulti(this)">House</div>
            </div>
        </div>
        <div class="wizard-footer">
            <button class="btn-text" onclick="nextScreen('wizardStep3')">← Kembali</button>
            <button class="btn-primary" style="width: auto; padding: 10px 24px; margin: 0;" onclick="finishWizard()">Continue</button>
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
        document.querySelectorAll('.screen-overlay').forEach(el => el.classList.add('hidden'));
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
        showToast("Tetapan profil berjaya disimpan! Selamat datang ke Studio.");
        setTimeout(() => {
            nextScreen('screenLogin');
        }, 1500);
    }
</script>

</body>
</html>
"""
    
