from fastapi import FastAPI, File, UploadFile
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

@app.get("/", response_class=HTMLResponse)
def login_page():
    return """
<!DOCTYPE html>
<html lang="ms">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>BP AI Music Studio - Log Masuk</title>
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
        }

        .app-container {
            width: 100%;
            max-width: 480px;
            min-height: 100vh;
            background: linear-gradient(135deg, rgba(15, 23, 42, 0.8) 0%, rgba(15, 23, 42, 0.9) 100%), url('/images (43).jpeg');
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            position: relative;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            padding: 32px 24px;
            box-sizing: border-box;
            box-shadow: 0 0 40px rgba(0,0,0,0.7);
            margin: 0 auto;
        }

        .login-header {
            text-align: center;
            margin-top: 20px;
        }

        .brand-logo {
            font-family: 'Syne', sans-serif;
            font-size: 26px;
            font-weight: 800;
            color: #ffffff;
            letter-spacing: 0.5px;
            margin-bottom: 8px;
            text-transform: uppercase;
        }

        .login-subtitle {
            font-size: 13px;
            color: #cbd5e1;
            margin-bottom: 30px;
        }

        .social-login-container {
            display: flex;
            justify-content: space-between;
            gap: 10px;
            margin-bottom: 25px;
        }

        .social-btn {
            flex: 1;
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
            margin-bottom: 25px;
        }

        .form-group {
            margin-bottom: 16px;
        }

        .form-input {
            background: rgba(15, 23, 42, 0.75);
            border: 1px solid rgba(255, 255, 255, 0.2);
            padding: 14px 18px;
            border-radius: 12px;
            width: 100%;
            color: #ffffff;
            font-size: 14px;
            box-sizing: border-box;
            outline: none;
            backdrop-filter: blur(5px);
            transition: border-color 0.2s;
        }

        .form-input:focus {
            border-color: #2dd4bf;
            box-shadow: 0 0 0 3px rgba(45, 212, 191, 0.2);
        }

        .forgot-password {
            text-align: right;
            font-size: 12px;
            color: #38bdf8;
            margin-bottom: 30px;
            cursor: pointer;
            font-weight: 500;
        }

        .forgot-password:hover {
            text-decoration: underline;
        }

        .btn-primary {
            background: #2dd4bf;
            color: #0f172a;
            font-family: 'Syne', sans-serif;
            font-weight: 700;
            font-size: 15px;
            padding: 15px;
            border-radius: 30px;
            border: none;
            width: 100%;
            cursor: pointer;
            box-shadow: 0 4px 15px rgba(45, 212, 191, 0.4);
            transition: opacity 0.2s;
        }

        .btn-primary:hover {
            opacity: 0.9;
        }
    </style>
</head>
<body>

<div class="app-container">
    <div class="login-header">
        <div class="brand-logo">BP AI MUSIC STUDIO</div>
        <div class="login-subtitle">Log masuk ke akaun profesional anda</div>
    </div>

    <div>
        <div class="social-login-container">
            <button class="social-btn" onclick="alert('Login Google')">🌐 Google</button>
            <button class="social-btn" onclick="alert('Login Apple')">🍎 Apple</button>
            <button class="social-btn" onclick="alert('Login Facebook')">📘 Facebook</button>
        </div>

        <div class="divider-text">atau melalui e-mel</div>

        <div class="form-group">
            <input type="email" class="form-input" placeholder="E-mel anda">
        </div>

        <div class="form-group">
            <input type="password" class="form-input" placeholder="Kata laluan">
        </div>

        <div class="forgot-password" onclick="alert('Fungsi Lupa Kata Laluan')">Lupa kata laluan?</div>

        <button class="btn-primary" onclick="alert('Berjaya Log Masuk!')">Log Masuk</button>
    </div>

    <div></div> <!-- Spacer -->
</div>

</body>
</html>
    """
    
