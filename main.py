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

        #screenLogin {
            background-image: url('/kl-background.jpg');
            background-size: cover;
            background-position: center;
        }

        .screen-overlay {
            background: rgba(11, 15, 25, 0.85);
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
            margin: 15px 0;
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
            margin-top: 10px;
        }

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
            max-height: 55vh;
            padding-right: 4px;
        }

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

        .pill-option.active {
            background: rgba(34, 211, 238, 0.2);
            border-color: #22d3ee;
            color: #ffffff;
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
            <div class="wizard-subtitle">Tell us what types of music you're into and we'll make sure you get custom AI presets.</div>
        </div>
        <div class="wizard-body">
            <div class="pill-grid">
                <div class="pill-option active" onclick="toggleMulti(this)">🇲🇾 Melayu / Nusantara</div>
                <div class="pill-option" onclick="toggleMulti(this)">Pop</div>
                <div class="pill-option" onclick="toggleMulti(this)">Hip Hop</div>
                <div class="pill-option" onclick="toggleMulti(this)">Rock</div>
                <div class="pill-option" onclick="toggleMulti(this)">EDM</div>
                <div class="pill-option" onclick="toggleMulti(this)">Cinematic</div>
            </div>
        </div>
        <div class="wizard-footer">
            <button class="btn-text" onclick="nextScreen('wizardStep3')">← Kembali</button>
            <button class="btn-primary" style="width: auto; padding: 10px 24px; margin: 0;" onclick="finishWizard()">Continue</button>
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
            <button class="dash-btn-new" onclick="showToast('Mod projek baharu dibuka')">+ New ▾</button>
        </div>

        <h3 style="font-size: 14px; font-weight: 700; color: #475569; margin-bottom: 12px;">Projects</h3>

        <div class="project-card">
            <div style="font-weight: 700; font-size: 15px;">My project</div>
            <div class="project-status">
                ✓ All services are up and running
            </div>
        </div>

        <div class="create-project-box" onclick="showToast('Membina projek baharu...')">
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
</script>

</body>
</html>
"""
    
