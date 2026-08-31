from fastapi import FastAPI
from fastapi.responses import HTMLResponse, FileResponse
import os

app = FastAPI()

@app.get("/Untitled design.png")
def get_image():
    if os.path.exists("Untitled design.png"):
        return FileResponse("Untitled design.png")
    return {"error": "Image not found"}

@app.get("/", response_class=HTMLResponse)
def main_page():
    return """
<!DOCTYPE html>
<html lang="ms">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>BP AI Music Studio - Pro Mastering Suite</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700&family=Syne:wght@700;800&display=swap" rel="stylesheet">
    
    <style>
        body {
            background: #0b0f19;
            color: #ffffff;
            font-family: 'Montserrat', sans-serif;
            -webkit-font-smoothing: antialiased;
            margin: 0;
            padding: 0;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            min-height: 100vh;
            box-sizing: border-box;
            overflow-x: hidden;
        }

        .studio-container {
            width: 100%;
            max-width: 480px;
            min-height: 100vh;
            background: #0b0f19;
            background-image: url('/Untitled design.png');
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
            position: relative;
            display: flex;
            flex-direction: column;
            align-items: center;
            box-shadow: 0 0 25px rgba(0,0,0,0.8);
            box-sizing: border-box;
        }

        .studio-overlay {
            background: rgba(11, 15, 25, 0.55);
            backdrop-filter: blur(2px);
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            padding: 20px 16px;
            box-sizing: border-box;
            min-height: 100vh;
            width: 100%;
        }

        .page-section {
            display: flex;
            flex-direction: column;
            align-items: center;
            width: 100%;
            box-sizing: border-box;
        }

        .poster-title {
            font-family: 'Syne', sans-serif;
            font-size: 15px;
            font-weight: 800;
            color: #60a5fa;
            letter-spacing: 1.2px;
            text-transform: uppercase;
            margin-bottom: 14px;
            text-align: center;
            width: 100%;
            text-shadow: 0 3px 10px rgba(0, 0, 0, 0.9);
        }

        .content-readable-box {
            background: rgba(15, 23, 42, 0.85);
            padding: 16px;
            border-radius: 12px;
            border: 1px solid rgba(59, 130, 246, 0.4);
            margin-bottom: 12px;
            box-sizing: border-box;
            box-shadow: 0 4px 20px rgba(0,0,0,0.8);
            width: 100%;
            max-height: 68vh;
            overflow-y: auto;
            display: flex;
            flex-direction: column;
            align-items: center;
            text-align: center;
        }

        .content-readable-box::-webkit-scrollbar {
            width: 5px;
        }

        .content-readable-box::-webkit-scrollbar-thumb {
            background: rgba(59, 130, 246, 0.4);
            border-radius: 4px;
        }

        .poster-desc {
            font-size: 12px;
            line-height: 1.6;
            color: #f1f5f9;
            margin-bottom: 12px;
            font-weight: 500;
            text-align: center;
            width: 100%;
        }

        .poster-quote-box {
            margin-bottom: 12px;
            padding: 12px 14px;
            background: rgba(15, 23, 42, 0.80);
            border-left: 4px solid #fbbf24;
            border-radius: 6px;
            box-sizing: border-box;
            box-shadow: 0 4px 15px rgba(0,0,0,0.6);
            width: 100%;
            display: flex;
            flex-direction: column;
            align-items: center;
            text-align: center;
        }

        .poster-quote-title {
            font-family: 'Syne', sans-serif;
            font-size: 11px;
            font-weight: 800;
            color: #ffffff;
            letter-spacing: 1px;
            text-transform: uppercase;
            margin-bottom: 2px;
            text-align: center;
            width: 100%;
        }

        .poster-quote {
            font-size: 11.5px;
            font-weight: 700;
            color: #fbbf24;
            font-style: italic;
            text-align: center;
            width: 100%;
        }

        .section-label {
            font-family: 'Syne', sans-serif;
            font-size: 12px;
            font-weight: 700;
            color: #60a5fa;
            margin-bottom: 8px;
            display: block;
            text-align: center;
            width: 100%;
        }

        .points-grid {
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 10px;
            width: 100%;
        }

        .point-card {
            background: rgba(30, 41, 59, 0.85);
            border: 1px solid rgba(59, 130, 246, 0.4);
            padding: 12px 14px;
            border-radius: 10px;
            cursor: pointer;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            text-align: center;
            transition: all 0.2s ease;
            width: 100%;
            box-sizing: border-box;
        }

        .point-card:hover, .point-card.selected {
            background: rgba(37, 99, 235, 0.4);
            border-color: #3b82f6;
            transform: scale(1.02);
        }

        .point-card-title {
            font-family: 'Syne', sans-serif;
            font-size: 12.5px;
            font-weight: 700;
            color: #ffffff;
            text-align: center;
            width: 100%;
        }

        .point-card-desc {
            font-size: 10.5px;
            color: #94a3b8;
            margin-top: 2px;
            text-align: center;
            width: 100%;
        }

        .genre-group-title {
            font-family: 'Syne', sans-serif;
            font-size: 11.5px;
            font-weight: 700;
            color: #fbbf24;
            margin: 12px 0 6px 0;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            text-align: center;
            width: 100%;
        }

        .genre-item-list {
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 5px;
            margin-bottom: 10px;
            width: 100%;
        }

        .genre-chip {
            background: rgba(30, 41, 59, 0.85);
            border: 1px solid rgba(59, 130, 246, 0.3);
            padding: 9px 12px;
            border-radius: 8px;
            font-size: 12px;
            color: #f1f5f9;
            cursor: pointer;
            transition: background 0.2s;
            text-align: center;
            font-weight: 500;
            width: 100%;
            box-sizing: border-box;
        }

        .genre-chip:hover {
            background: #3b82f6;
            color: #ffffff;
            border-color: #3b82f6;
        }

        input[type="file"] {
            background: rgba(30, 41, 59, 0.85);
            border: 1px dashed #3b82f6;
            padding: 10px 12px;
            border-radius: 10px;
            width: 100%;
            color: #ffffff;
            font-size: 12px;
            font-family: 'Montserrat', sans-serif;
            box-sizing: border-box;
            margin-bottom: 12px;
            cursor: pointer;
            outline: none;
            text-align: center;
        }

        input[type="file"]::file-selector-button {
            background: #3b82f6;
            color: white;
            border: none;
            padding: 6px 10px;
            border-radius: 6px;
            cursor: pointer;
            font-family: 'Montserrat', sans-serif;
            font-weight: 600;
            margin-right: 8px;
        }

        .status-ready {
            font-size: 11px;
            color: #34d399;
            margin-top: -6px;
            margin-bottom: 12px;
            font-weight: 700;
            display: none;
            text-align: center;
            width: 100%;
        }

        .selected-display {
            background: rgba(30, 41, 59, 0.85);
            border: 1px solid #3b82f6;
            padding: 10px 12px;
            border-radius: 8px;
            font-size: 12px;
            color: #34d399;
            font-weight: 600;
            margin-bottom: 14px;
            text-align: center;
            width: 100%;
            box-sizing: border-box;
        }

        .btn-container {
            display: flex;
            justify-content: center;
            align-items: center;
            gap: 10px;
            width: 100%;
            margin-top: 4px;
        }

        .btn {
            flex: 1;
            padding: 12px;
            border-radius: 10px;
            font-family: 'Syne', sans-serif;
            font-weight: 700;
            font-size: 12px;
            text-align: center;
            cursor: pointer;
            border: none;
            background: linear-gradient(135deg, #3b82f6, #2563eb);
            color: white;
            box-shadow: 0 4px 15px rgba(59, 130, 246, 0.5);
        }

        .btn-success {
            background: linear-gradient(135deg, #10b981, #059669);
            box-shadow: 0 4px 15px rgba(16, 185, 129, 0.5);
        }

        .btn-secondary {
            background: linear-gradient(135deg, #475569, #334155);
            box-shadow: 0 4px 15px rgba(71, 85, 105, 0.5);
        }

        .control-group {
            margin-bottom: 14px;
            text-align: center;
            width: 100%;
            display: flex;
            flex-direction: column;
            align-items: center;
        }

        .control-group:last-child {
            margin-bottom: 0;
        }

        .control-label {
            font-size: 11.5px;
            color: #93c5fd;
            margin-bottom: 6px;
            display: block;
            font-weight: 600;
            text-align: center;
            width: 100%;
        }

        select.studio-select {
            background: rgba(30, 41, 59, 0.85);
            border: 1px solid rgba(59, 130, 246, 0.6);
            padding: 10px 12px;
            border-radius: 8px;
            width: 100%;
            color: #ffffff;
            font-size: 12px;
            font-family: 'Montserrat', sans-serif;
            box-sizing: border-box;
            outline: none;
            text-align: center;
            text-align-last: center;
        }

        .studio-range {
            width: 100%;
            accent-color: #3b82f6;
            cursor: pointer;
            margin-top: 4px;
        }

        .eq-container {
            display: flex;
            gap: 8px;
            width: 100%;
            justify-content: space-between;
        }

        .eq-box {
            flex: 1;
            background: rgba(30, 41, 59, 0.85);
            border: 1px solid rgba(59, 130, 246, 0.3);
            padding: 8px;
            border-radius: 8px;
            text-align: center;
        }

        .eq-title {
            font-size: 10.5px;
            color: #93c5fd;
            font-weight: 700;
            margin-bottom: 4px;
            display: block;
        }

        .audio-preview-box {
            background: rgba(30, 41, 59, 0.85);
            border: 1px solid rgba(59, 130, 246, 0.6);
            padding: 10px;
            border-radius: 10px;
            width: 100%;
            box-sizing: border-box;
            margin-bottom: 14px;
            display: none;
        }

        audio {
            width: 100%;
            height: 36px;
            outline: none;
        }

        .visualizer-box {
            display: flex;
            align-items: flex-end;
            justify-content: center;
            gap: 3px;
            height: 35px;
            margin: 4px 0 10px 0;
            width: 100%;
        }

        .bar {
            width: 5px;
            background: #3b82f6;
            border-radius: 2px;
            height: 5px;
            transition: height 0.05s ease;
        }

        .bar:nth-child(2) { background: #60a5fa; }
        .bar:nth-child(3) { background: #34d399; }
        .bar:nth-child(4) { background: #fbbf24; }
        .bar:nth-child(5) { background: #f87171; }
        .bar:nth-child(6) { background: #3b82f6; }

        .success-icon {
            font-size: 32px;
            margin-bottom: 4px;
        }

        #toastNotification {
            position: fixed;
            bottom: 30px;
            background: rgba(16, 185, 129, 0.95);
            color: white;
            padding: 10px 20px;
            border-radius: 8px;
            font-size: 12px;
            font-weight: 600;
            box-shadow: 0 4px 15px rgba(0,0,0,0.5);
            transition: opacity 0.3s ease;
            opacity: 0;
            pointer-events: none;
            z-index: 1000;
            font-family: 'Syne', sans-serif;
        }

        .hidden {
            display: none !important;
        }
    </style>
</head>
<body>

<div id="toastNotification">Notifikasi Berjaya</div>

<div class="studio-container">
    <div class="studio-overlay">
        
        <div id="page1" class="page-section">
            <div class="poster-title">MASTERING BP AI MUSIC STUDIO</div>

            <div class="content-readable-box">
                <div class="poster-desc">
                    Mastering BP AI MUSIC STUDIO ialah langkah akhir untuk mendapatkan hasil audio yang kemas, seimbang, dan berkualiti tinggi. Setiap elemen lagu diproses secara teliti.
                </div>
                <div class="poster-desc">
                    Sila pilih kategori genre muzik anda dengan teratur melalui sistem navigasi point khusus kami di peringkat seterusnya.
                </div>
            </div>

            <div class="poster-quote-box">
                <div class="poster-quote-title">BP AI MUSIC STUDIO</div>
                <div class="poster-quote">Memperkemas bunyi, menghidupkan karya.</div>
            </div>

            <div class="btn-container">
                <button type="button" class="btn" onclick="goToPage('page2')">Mula Pilih Genre</button>
            </div>
        </div>

        <div id="page2" class="page-section hidden">
            <div class="poster-title">🎵 GENRE LAGU</div>

            <div class="content-readable-box">
                <div class="points-grid">
                    <div class="point-card" onclick="selectPoint(1, this)"><div class="point-card-title">01 🇲🇾 Melayu / Nusantara</div><div class="point-card-desc">Malaya, Tradisional, Nusantara & Modern</div></div>
                    <div class="point-card" onclick="selectPoint(2, this)"><div class="point-card-title">02 🎤 Pop</div><div class="point-card-desc">Pop Ballad, Electropop, Synthpop, Indie Pop</div></div>
                    <div class="point-card" onclick="selectPoint(3, this)"><div class="point-card-title">03 🎸 Rock</div><div class="point-card-desc">Classic Rock, Alternative, Indie, Grunge, Metal</div></div>
                    <div class="point-card" onclick="selectPoint(4, this)"><div class="point-card-title">04 🎤 Hip Hop / Rap</div><div class="point-card-desc">Trap, Boom Bap, Drill, Old School, Melodic</div></div>
                    <div class="point-card" onclick="selectPoint(5, this)"><div class="point-card-title">05 🔥 Phonk</div><div class="point-card-desc">Drift Phonk, Brazilian, Dark, Malay Phonk</div></div>
                    <div class="point-card" onclick="selectPoint(6, this)"><div class="point-card-title">06 ⚡ Techno / Electronic</div><div class="point-card-desc">EDM, House, Trance, Dubstep, Amapiano</div></div>
                    <div class="point-card" onclick="selectPoint(7, this)"><div class="point-card-title">07 🌑 Dark / Cyber / Experimental</div><div class="point-card-desc">Darkwave, Synthwave, Cyberpunk, Ambient</div></div>
                    <div class="point-card" onclick="selectPoint(8, this)"><div class="point-card-title">08 🎷 R&B / Soul / Funk</div><div class="point-card-desc">Contemporary R&B, Neo Soul, Motown, Funk</div></div>
                    <div class="point-card" onclick="selectPoint(9, this)"><div class="point-card-title">09 🎷 Jazz / Blues</div><div class="point-card-desc">Smooth Jazz, Swing, Bebop, Slow Blues</div></div>
                    <div class="point-card" onclick="selectPoint(10, this)"><div class="point-card-title">10 🎸 Akustik / Folk</div><div class="point-card-desc">Acoustic Pop, Indie Folk, Lo-Fi, Chill, Lounge</div></div>
                    <div class="point-card" onclick="selectPoint(11, this)"><div class="point-card-title">11 🎻 Orkestra / Klasik</div><div class="point-card-desc">Classical, Piano Solo, Symphony, Cinematic Score</div></div>
                    <div class="point-card" onclick="selectPoint(12, this)"><div class="point-card-title">12 ❤️ Sedih / Emosi / Cinta</div><div class="point-card-desc">Sad Song, Heartbreak, Romantic, Slow Ballad</div></div>
                    <div class="point-card" onclick="selectPoint(13, this)"><div class="point-card-title">13 🌎 Antarabangsa</div><div class="point-card-desc">K-Pop, J-Pop, Bollywood, Latin, Reggae, Country</div></div>
                    <div class="point-card" onclick="selectPoint(14, this)"><div class="point-card-title">14 🤘 Metal</div><div class="point-card-desc">Heavy Metal, Metalcore, Death, Black, Doom</div></div>
                    <div class="point-card" onclick="selectPoint(15, this)"><div class="point-card-title">15 🎬 Cinematic / Mood / Khas</div><div class="point-card-desc">Epic, Horror, Motivational, Wedding, Raya</div></div>
                </div>
            </div>

            <div class="btn-container">
                <button type="button" class="btn btn-secondary" onclick="goToPage('page1')">Kembali</button>
                <button type="button" class="btn" onclick="proceedToSubGenre()">Seterusnya</button>
            </div>
        </div>

        <div id="subGenrePage" class="page-section hidden">
            <div class="poster-title" id="subGenreTitle">PILIHAN GENRE</div>
            <div class="content-readable-box" id="subGenreContentContainer"></div>
            <div class="btn-container">
                <button type="button" class="btn" onclick="goToPage('page2')">Kembali</button>
            </div>
        </div>

        <div id="pageUpload" class="page-section hidden">
            <div class="poster-title">TETAPAN MASTERING AKHIR</div>

            <div class="content-readable-box">
                <div class="selected-display" id="displayChosenGenre">Genre Dipilih: -</div>

                <span class="section-label">📁 Pilih Fail Muzik</span>
                <input type="file" id="audioFile" accept="audio/*" onchange="handleFileSelected(this)">
                <div id="fileStatus" class="status-ready">✅ Fail berjaya dipilih!</div>

                <div class="audio-preview-box" id="audioPreviewContainer">
                    <label class="control-label" style="margin-bottom: 4px;">🎧 Test Dengar Lagu (Real-time Mastering)</label>
                    <audio id="audioPreviewPlayer" controls onplay="initWebAudioAndResume()"></audio>
                </div>
  <div class="control-group">
                    <label class="control-label">🎚️ Profil Mastering</label>
                    <select class="studio-select" id="masteringProfile" onchange="changeProfilePreset()">
                        <option value="universal">Universal (Seimbang & Neutral)</option>
                        <option value="fire">Fire (Bertenaga & Saturasi)</option>
                        <option value="clarity">Clarity (Terang & Bersih)</option>
                        <option value="tape">Tape (Kehangatan Analog Vintaj)</option>
                        <option value="natural">Natural (Keaslian Asal)</option>
                        <option value="spatial">Spatial (Ruang Stereo Luas)</option>
                        <option value="cinematic">Cinematic (Epik & Mendalam)</option>
                        <option value="punch">Punch (Hentakan Dramatis)</option>
                    </select>
                </div>

                <div class="control-group" style="background: rgba(30, 41, 59, 0.4); padding: 8px; border-radius: 8px; border: 1px dashed rgba(59, 130, 246, 0.3);">
                    <label class="control-label">⭐ Preset Tersuai Anda</label>
                    <div style="display: flex; gap: 6px; width: 100%;">
                        <select class="studio-select" id="customPresetSelect" onchange="loadCustomPreset(this.value)">
                            <option value="">-- Pilih Tetapan Disimpan --</option>
                        </select>
                        <button type="button" class="btn" style="padding: 6px 10px; font-size: 10px; flex: 0.6;" onclick="saveCustomPreset()">Simpan</button>
                    </div>
                </div>

                <div class="control-group">
                    <label class="control-label">⚡ Intensity: <span id="intensityVal">50</span>%</label>
                    <input type="range" min="0" max="100" value="50" class="studio-range" id="intensityRange" oninput="document.getElementById('intensityVal').innerText = this.value; applyAudioSettings();">
                </div>

                <div class="control-group">
                    <label class="control-label">🎛️ Equalizer (EQ)</label>
                    <div class="eq-container">
                        <div class="eq-box"><span class="eq-title">LOW <span id="eqLowVal" style="color: #60a5fa; font-weight: 600;">0 dB</span></span><input type="range" min="-12" max="12" value="0" class="studio-range" id="eqLow" oninput="updateEqLabel('Low'); applyAudioSettings();"></div>
                        <div class="eq-box"><span class="eq-title">MID <span id="eqMidVal" style="color: #60a5fa; font-weight: 600;">0 dB</span></span><input type="range" min="-12" max="12" value="0" class="studio-range" id="eqMid" oninput="updateEqLabel('Mid'); applyAudioSettings();"></div>
                        <div class="eq-box"><span class="eq-title">HIGH <span id="eqHighVal" style="color: #60a5fa; font-weight: 600;">0 dB</span></span><input type="range" min="-12" max="12" value="0" class="studio-range" id="eqHigh" oninput="updateEqLabel('High'); applyAudioSettings();"></div>
                    </div>
                </div>
            </div>

            <div class="btn-container">
                <button type="button" class="btn btn-secondary" onclick="goToPage('subGenrePage')">Kembali</button>
                <button type="button" class="btn" onclick="startMasteringProcess()">Mula Proses</button>
            </div>
        </div>

        <div id="pageResult" class="page-section hidden">
            <div class="poster-title">HASIL MASTERING SIAP</div>

            <div class="content-readable-box">
                <div class="success-icon">🎉</div>
                <div class="poster-quote-title" style="margin-bottom: 4px; color: #34d399;">PROSES BERJAYA!</div>
                <div class="selected-display" id="displayResultGenre" style="margin-bottom: 12px; margin-top: 6px;">Genre: -</div>

                <div class="control-group" style="margin-bottom: 12px; width: 100%;">
                    <label class="control-label">1️⃣ Ujian Perbandingan Bunyi</label>
                    <button type="button" id="abTestBtn" class="btn btn-secondary" onclick="toggleABTest()" style="font-size: 11px; padding: 10px; width: 100%;">
                        🔄 A/B Test: Dengar Lagu Asal (Bypass)
                    </button>
                </div>

                <div class="control-group" style="margin-bottom: 12px; width: 100%;">
                    <label class="control-label">2️⃣ Analisis Spektrum & Aras Bunyi (dB)</label>
                    <div class="visualizer-box" id="realVisualizer" style="height: 45px; display: flex; align-items: flex-end; justify-content: center; gap: 3px; background: rgba(15, 23, 42, 0.6); padding: 6px; border-radius: 8px; border: 1px solid rgba(59, 130, 246, 0.3);">
                        <div class="bar"></div><div class="bar"></div><div class="bar"></div>
                        <div class="bar"></div><div class="bar"></div><div class="bar"></div>
                        <div class="bar"></div><div class="bar"></div><div class="bar"></div>
                    </div>

                    <div style="margin-top: 8px; width: 100%;">
                        <div style="display: flex; justify-content: space-between; font-size: 10px; color: #94a3b8; margin-bottom: 3px;">
                            <span>Aras dB</span>
                            <span id="dbValueText">-24.0 dB</span>
                        </div>
                        <div style="width: 100%; background: rgba(30, 41, 59, 0.8); height: 8px; border-radius: 4px; overflow: hidden; border: 1px solid rgba(59, 130, 246, 0.2);">
                            <div id="dbMeterBar" style="width: 40%; height: 100%; background: linear-gradient(90deg, #3b82f6, #10b981, #f59e0b); transition: width 0.05s ease;"></div>
                        </div>
                    </div>
                </div>

                <div class="control-group" style="margin-bottom: 0; width: 100%;">
                    <label class="control-label">3️⃣ Muat Turun Fail</label>
                    <select class="studio-select" id="downloadFormat" style="margin-bottom: 8px;">
                        <option value="mp3">MP3 (Standard & Ringkas)</option>
                        <option value="wav">WAV (Kualiti Studio Penuh / Lossless)</option>
                    </select>
                </div>
            </div>

            <div class="btn-container" style="flex-direction: column; gap: 8px;">
                <button type="button" class="btn btn-success" onclick="downloadMasteredFile()" style="width: 100%;">📥 Muat Turun Sekarang</button>
                <button type="button" class="btn btn-secondary" onclick="goToPage('pageUpload')" style="width: 100%;">⬅️ Kembali ke Tetapan</button>
                <button type="button" class="btn btn-secondary" onclick="resetStudio()" style="width: 100%;">Mastering Lagu Lain</button>
            </div>
        </div>

    </div>
</div>

<script>
    const genreData = {
        1: {
            title: "🇲🇾 01 - Melayu / Nusantara",
            groups: [
                { name: "Melayu / Malaya", items: ["Malaya / Melayu", "Pop Melayu", "Rock Melayu", "Balada Melayu", "Melayu Klasik", "Irama Malaysia"] },
                { name: "Tradisional", items: ["Lagu Asli", "Zapin", "Joget", "Ghazal", "Keroncong"] },
                { name: "Nusantara", items: ["Dangdut", "Campursari", "Pop Nusantara", "Etnik Nusantara", "Tradisional Melayu", "Tradisional Sabah", "Tradisional Sarawak", "Minang", "Jawa", "Sunda", "Bugis", "Batak"] },
                { name: "Modern Melayu", items: ["Malay Bounce", "Malay Trap", "Malay Phonk", "Malay Electronic", "Nusantara Electronic"] }
            ]
        },
        2: { title: "🎤 02 - Pop", groups: [{ name: "Kategori Pop", items: ["Pop", "Pop Ballad", "Electropop", "Synthpop", "Dream Pop", "Indie Pop", "Teen Pop", "Adult Contemporary", "Dance Pop", "Power Pop", "Soft Pop", "Retro Pop", "City Pop", "Dark Pop", "Noir Pop", "Future Pop", "Neon Pop", "Experimental Pop"] }] },
        3: { title: "🎸 03 - Rock", groups: [{ name: "Kategori Rock", items: ["Rock", "Soft Rock", "Classic Rock", "Hard Rock", "Alternative Rock", "Indie Rock", "Pop Rock", "Blues Rock", "Progressive Rock", "Psychedelic Rock", "Punk Rock", "Garage Rock", "Grunge", "Post-Rock", "Folk Rock", "Southern Rock", "Glam Rock", "Arena Rock", "Metal Rock"] }] },
        4: { title: "🎤 04 - Hip Hop / Rap", groups: [{ name: "Kategori Hip Hop / Rap", items: ["Hip Hop", "Rap", "Old School Hip Hop", "Trap", "Boom Bap", "Lo-Fi Hip Hop", "Gangsta Rap", "Conscious Rap", "Melodic Rap", "Pop Rap", "Alternative Hip Hop", "R&B Rap", "Drill", "West Coast Hip Hop", "East Coast Hip Hop", "UK Drill", "Afro Drill", "Cyberpunk Trap", "Cinematic Trap", "Hybrid Trap"] }] },
        5: { title: "🔥 05 - Phonk", groups: [{ name: "Kategori Phonk", items: ["Phonk", "Dark Phonk", "Drift Phonk", "Brazilian Phonk", "Memphis Phonk", "Aggressive Phonk", "Atmospheric Phonk", "Electro Phonk", "Trap Phonk", "Future Phonk", "Malay Phonk", "Neon Noir Phonk", "Neon Noir Phonk - Malay Bounce", "Dark Techno / Neon Noir Phonk - Malay Bounce"] }] },
        6: { title: "⚡ 06 - Techno / Electronic", groups: [{ name: "Kategori Techno / Electronic", items: ["EDM", "Techno", "Dark Techno", "Hard Techno", "Industrial Techno", "Acid Techno", "Minimal Techno", "Melodic Techno", "Progressive Techno", "Techno Noir", "Cyber Techno", "House", "Deep House", "Tropical House", "Future House", "Progressive House", "Tech House", "Electro House", "Bass House", "G-House", "Slap House", "Afro House", "Trance", "Dubstep", "Drum & Bass", "Future Bass", "Breakbeat", "UK Garage", "Jersey Club", "Amapiano", "Industrial Bass", "Dark Electro", "Alternative Electronic", "Cinematic Electronic"] }] },
        7: { title: "🌑 07 - Dark / Cyber / Experimental", groups: [{ name: "Kategori Dark / Cyber / Experimental", items: ["Darkwave", "Witch House", "Dark Synthwave", "Neon Synthwave", "Synthwave", "Vaporwave", "Cyberpunk", "Cyber Pop", "Cyberpunk Trap", "Noir Electronic", "Dark Ambient", "Ambient Dark", "Horror Electronic", "Atmospheric", "Experimental Electronic", "Experimental Pop", "Future Bass", "Future Garage", "Industrial", "Noise", "Glitch", "Glitch Hop"] }] },
        8: { title: "🎷 08 - R&B / Soul / Funk", groups: [{ name: "Kategori R&B / Soul / Funk", items: ["R&B", "Contemporary R&B", "Soul", "Neo Soul", "Motown", "Funk", "Smooth Soul", "Gospel Soul", "R&B Ballad", "Funk Soul"] }] },
        9: { title: "🎷 09 - Jazz / Blues", groups: [{ name: "Kategori Jazz / Blues", items: ["Jazz", "Smooth Jazz", "Contemporary Jazz", "Swing", "Bebop", "Fusion Jazz", "Latin Jazz", "Blues", "Slow Blues", "Blues Rock", "Soul Blues"] }] },
        10: { title: "🎸 10 - Akustik / Folk", groups: [{ name: "Kategori Akustik / Folk", items: ["Acoustic", "Acoustic Pop", "Acoustic Ballad", "Folk", "Indie Folk", "Folk Pop", "Singer-Songwriter", "Coffeehouse", "Chill", "Lo-Fi", "Lounge", "Relaxing"] }] },
        11: { title: "🎻 11 - Orkestra / Klasik", groups: [{ name: "Kategori Orkestra / Klasik", items: ["Classical", "Piano Solo", "Piano Ballad", "String Orchestra", "Symphony", "Chamber Music", "Cinematic", "Epic Orchestra", "Film Score", "Dramatic", "Emotional Orchestra", "Fantasy", "Medieval", "Baroque"] }] },
        12: { title: "❤️ 12 - Sedih / Emosi / Cinta", groups: [{ name: "Kategori Sedih / Emosi / Cinta", items: ["Sad Song", "Emotional", "Heartbreak", "Melancholic", "Nostalgic", "Romantic", "Love Song", "Deep Emotional", "Tearjerker", "Slow Ballad", "Emotional Piano", "Emotional Acoustic", "Power Ballad"] }] },
        13: { title: "🌎 13 - Antarabangsa", groups: [{ name: "Kategori Antarabangsa", items: ["K-Pop", "J-Pop", "C-Pop", "Bollywood", "Latin Pop", "Reggaeton", "Salsa", "Bachata", "Flamenco", "Afrobeat", "Afropop", "Reggae", "Dancehall", "Ska", "Country", "Country Pop", "Bluegrass", "Gospel", "Celtic", "Arabic", "Middle Eastern"] }] },
        14: { title: "🤘 14 - Metal", groups: [{ name: "Kategori Metal", items: ["Heavy Metal", "Metalcore", "Death Metal", "Black Metal", "Symphonic Metal", "Power Metal", "Progressive Metal", "Nu Metal", "Alternative Metal", "Doom Metal"] }] },
        15: { title: "🎬 15 - Cinematic / Mood / Khas", groups: [{ name: "Kategori Cinematic / Mood / Khas", items: ["Cinematic", "Epic", "Dark", "Mysterious", "Horror", "Thriller", "Adventure", "Fantasy", "Heroic", "Inspirational", "Motivational", "Spiritual", "Religious", "Peaceful", "Meditation", "Atmospheric", "Dreamy", "Powerful", "Energetic", "Romantic", "Vintage", "Retro", "80s", "90s", "Nostalgic", "Wedding", "Festival", "Party", "Christmas", "Raya / Aidilfitri"] }] }
    };

    let chosenGenreGlobal = "";
    let selectedPointGlobal = null;
    let audioFileGlobal = null;
    let audioCtx = null;
    let sourceNode = null;
    let lowFilter, midFilter, highFilter, compressorNode, analyserNode;
    let isWebAudioInitialized = false;
    let isBypassed = false;
    let animationId = null;

    function showToast(message) {
        let toast = document.getElementById('toastNotification');
        toast.innerText = message;
        toast.style.opacity = '1';
        setTimeout(() => { toast.style.opacity = '0'; }, 2500);
    }

    function goToPage(pageId) {
        document.querySelectorAll('.page-section').forEach(el => el.classList.add('hidden'));
        document.getElementById(pageId).classList.remove('hidden');
        window.scrollTo(0, 0);
    }

    function selectPoint(pointNumber, element) {
        document.querySelectorAll('.point-card').forEach(card => card.classList.remove('selected'));
        element.classList.add('selected');
        selectedPointGlobal = pointNumber;
    }

    function proceedToSubGenre() {
        if (!selectedPointGlobal) {
            alert('Sila pilih salah satu genre terlebih dahulu!');
            return;
        }
        openPoint(selectedPointGlobal);
    }

    function openPoint(pointNumber) {
        let data = genreData[pointNumber];
        document.getElementById('subGenreTitle').innerText = data.title;
        let container = document.getElementById('subGenreContentContainer');
        container.innerHTML = '';

        data.groups.forEach(group => {
            let groupHeader = document.createElement('div');
            groupHeader.className = 'genre-group-title';
            groupHeader.innerText = group.name;
            container.appendChild(groupHeader);

            let listDiv = document.createElement('div');
            listDiv.className = 'genre-item-list';

            group.items.forEach(genre => {
                let chip = document.createElement('div');
                chip.className = 'genre-chip';
                chip.innerText = genre;
                chip.onclick = function() { selectGenreAndProceed(genre); };
                listDiv.appendChild(chip);
            });
            container.appendChild(listDiv);
        });

        goToPage('subGenrePage');
    }

    function selectGenreAndProceed(genreName) {
        chosenGenreGlobal = genreName;
        document.getElementById('displayChosenGenre').innerText = "Genre Dipilih: " + genreName;
        goToPage('pageUpload');
    }

    function handleFileSelected(input) {
        if (input.files && input.files[0]) {
            audioFileGlobal = input.files[0];
            document.getElementById('fileStatus').style.display = 'block';
            let audioPlayer = document.getElementById('audioPreviewPlayer');
            let previewBox = document.getElementById('audioPreviewContainer');
            audioPlayer.src = URL.createObjectURL(audioFileGlobal);
            previewBox.style.display = 'block';
            isWebAudioInitialized = false;
            showToast("Fail audio berjaya dimuat naik!");
        }
    }

    function initWebAudioAndResume() {
        let audioElement = document.getElementById('audioPreviewPlayer');
        if (!isWebAudioInitialized) {
            try {
                const AudioContext = window.AudioContext || window.webkitAudioContext;
                audioCtx = new AudioContext();
                sourceNode = audioCtx.createMediaElementSource(audioElement);

                lowFilter = audioCtx.createBiquadFilter();
                lowFilter.type = 'lowshelf';
                lowFilter.frequency.value = 250;

                midFilter = audioCtx.createBiquadFilter();
                midFilter.type = 'peaking';
                midFilter.frequency.value = 1500;
                midFilter.Q.value = 1;

                highFilter = audioCtx.createBiquadFilter();
                highFilter.type = 'highshelf';
                highFilter.frequency.value = 4000;

                compressorNode = audioCtx.createDynamicsCompressor();
                analyserNode = audioCtx.createAnalyser();
                analyserNode.fftSize = 64;

                rebuildAudioChain();
                isWebAudioInitialized = true;
                startVisualizerAndMeterLoop();
            } catch(e) {
                console.log("Web Audio API Error:", e);
            }
        }
        if (audioCtx && audioCtx.state === 'suspended') { audioCtx.resume(); }
        applyAudioSettings();
    }

    function rebuildAudioChain() {
        if (!sourceNode) return;
        sourceNode.disconnect();
        if (lowFilter) lowFilter.disconnect();
        if (midFilter) midFilter.disconnect();
        if (highFilter) highFilter.disconnect();
        if (compressorNode) compressorNode.disconnect();
        if (analyserNode) analyserNode.disconnect();

        if (isBypassed) {
            sourceNode.connect(analyserNode);
            analyserNode.connect(audioCtx.destination);
        } else {
            sourceNode.connect(lowFilter);
            lowFilter.connect(midFilter);
            midFilter.connect(highFilter);
            highFilter.connect(compressorNode);
            compressorNode.connect(analyserNode);
            analyserNode.connect(audioCtx.destination);
        }
    }

    function startVisualizerAndMeterLoop() {
        if (!analyserNode) return;
        let bufferLength = analyserNode.frequencyBinCount;
        let dataArray = new Uint8Array(bufferLength);
        let bars = document.querySelectorAll('#realVisualizer .bar');
        
        let barMeter = document.getElementById('dbMeterBar');
        let textDb = document.getElementById('dbValueText');

        function renderFrame() {
            animationId = requestAnimationFrame(renderFrame);
            analyserNode.getByteFrequencyData(dataArray);
            
            let sum = 0;
            bars.forEach((bar, index) => {
                let value = dataArray[index * 2] || 0;
                sum += value;
                let height = (value / 255) * 35 + 5;
                bar.style.height = height + 'px';
            });

            let average = sum / bars.length;
            let percentage = (average / 255) * 100;
            let estimatedDb = -48 + (percentage * 0.48);
            
            if (barMeter && textDb) {
                barMeter.style.width = Math.max(5, percentage) + '%';
                textDb.innerText = estimatedDb.toFixed(1) + ' dB';
                
                if (estimatedDb > -3) {
                    barMeter.style.background = '#ef4444'; 
                } else if (estimatedDb > -12) {
                    barMeter.style.background = '#f59e0b'; 
                } else {
                    barMeter.style.background = 'linear-gradient(90deg, #3b82f6, #10b981)'; 
                }
            }
        }
        renderFrame();
    }

    function toggleABTest() {
        isBypassed = !isBypassed;
        let btn = document.getElementById('abTestBtn');
        if (isBypassed) {
            btn.innerText = "🔄 A/B Test: Sedang Dengar Bunyi Asal (Tanpa Mastering)";
            btn.style.background = "linear-gradient(135deg, #f59e0b, #d97706)";
            showToast("Beralih ke Bunyi Asal (Bypass)");
        } else {
            btn.innerText = "🔄 A/B Test: Dengar Lagu Asal (Bypass)";
            btn.style.background = "";
            showToast("Beralih ke Bunyi Dimaster");
        }
        rebuildAudioChain();
    }

    function updateEqLabel(type) {
        let slider = document.getElementById('eq' + type);
        let valSpan = document.getElementById('eq' + type + 'Val');
        if (slider && valSpan) {
            let val = parseFloat(slider.value);
            valSpan.innerText = (val > 0 ? '+' + val : val) + ' dB';
        }
    }

    function applyAudioSettings() {
        if (!isWebAudioInitialized || !audioCtx || isBypassed) return;
        let lowVal = parseFloat(document.getElementById('eqLow').value);
        let midVal = parseFloat(document.getElementById('eqMid').value);
        let highVal = parseFloat(document.getElementById('eqHigh').value);
        let intensity = parseFloat(document.getElementById('intensityRange').value);

        lowFilter.gain.value = lowVal;
        midFilter.gain.value = midVal;
        highFilter.gain.value = highVal;
        compressorNode.threshold.setValueAtTime(- (intensity * 0.35), audioCtx.currentTime);
        compressorNode.ratio.setValueAtTime(1 + (intensity * 0.18), audioCtx.currentTime);
    }

    function changeProfilePreset() {
        let profile = document.getElementById('masteringProfile').value;
        let low = 0, mid = 0, high = 0, intensity = 50;

        switch(profile) {
            case 'universal': low = 1; mid = 0; high = 1; intensity = 50; break;
            case 'fire': low = 4; mid = 3; high = 4; intensity = 85; break;
            case 'clarity': low = -1; mid = 2; high = 6; intensity = 60; break;
            case 'tape': low = 3; mid = -1; high = -3; intensity = 45; break;
            case 'natural': low = 0; mid = 0; high = 0; intensity = 20; break;
            case 'spatial': low = 2; mid = 1; high = 5; intensity = 55; break;
            case 'cinematic': low = 6; mid = -3; high = 5; intensity = 80; break;
            case 'punch': low = 5; mid = 3; high = 4; intensity = 90; break;
        }

        document.getElementById('eqLow').value = low;
        document.getElementById('eqMid').value = mid;
        document.getElementById('eqHigh').value = high;
        document.getElementById('intensityRange').value = intensity;
        document.getElementById('intensityVal').innerText = intensity;
        
        updateEqLabel('Low');
        updateEqLabel('Mid');
        updateEqLabel('High');

        applyAudioSettings();
        showToast("Profil " + profile.toUpperCase() + " dimuat turun!");
    }

    function saveCustomPreset() {
        let presetName = prompt("Masukkan nama untuk preset tersuai anda:");
        if (!presetName) return;

        let presetData = {
            low: document.getElementById('eqLow').value,
            mid: document.getElementById('eqMid').value,
            high: document.getElementById('eqHigh').value,
            intensity: document.getElementById('intensityRange').value
        };

        let savedPresets = JSON.parse(localStorage.getItem('bp_custom_presets') || '{}');
        savedPresets[presetName] = presetData;
        localStorage.setItem('bp_custom_presets', JSON.stringify(savedPresets));

        updateCustomPresetDropdown();
        showToast("Preset '" + presetName + "' berjaya disimpan!");
    }

    function updateCustomPresetDropdown() {
        let select = document.getElementById('customPresetSelect');
        if(!select) return;
        select.innerHTML = '<option value="">-- Pilih Tetapan Disimpan --</option>';
        let savedPresets = JSON.parse(localStorage.getItem('bp_custom_presets') || '{}');
        
        for (let name in savedPresets) {
            let opt = document.createElement('option');
            opt.value = name;
            opt.innerText = name;
            select.appendChild(opt);
        }
    }

    function loadCustomPreset(name) {
        if (!name) return;
        let savedPresets = JSON.parse(localStorage.getItem('bp_custom_presets') || '{}');
        let data = savedPresets[name];
        if (data) {
            document.getElementById('eqLow').value = data.low;
            document.getElementById('eqMid').value = data.mid;
            document.getElementById('eqHigh').value = data.high;
            document.getElementById('intensityRange').value = data.intensity;
            document.getElementById('intensityVal').innerText = data.intensity;
            
            updateEqLabel('Low');
            updateEqLabel('Mid');
            updateEqLabel('High');

            applyAudioSettings();
            showToast("Preset '" + name + "' dimuatkan!");
        }
    }

    function startMasteringProcess() {
        if (!audioFileGlobal) {
            alert('Sila pilih fail muzik terlebih dahulu!');
            return;
        }
        document.getElementById('displayResultGenre').innerText = "Genre: " + chosenGenreGlobal;
        goToPage('pageResult');
        showToast("Mastering selesai sepenuhnya!");
    }

    function downloadMasteredFile() {
        if (!audioFileGlobal) return;
        let format = document.getElementById('downloadFormat').value;
        let url = URL.createObjectURL(audioFileGlobal);
        let a = document.createElement('a');
        a.href = url;
        let originalName = audioFileGlobal.name.substring(0, audioFileGlobal.name.lastIndexOf('.')) || audioFileGlobal.name;
        a.download = `${originalName}_mastered_${chosenGenreGlobal.replace(/[^a-zA-Z0-9]/g, '_')}.${format}`;
        document.body.appendChild(a);
        a.click();
        document.body.removeChild(a);
        showToast("Fail berjaya dimuat turun!");
    }

    function resetStudio() {
        document.getElementById('audioFile').value = '';
        document.getElementById('fileStatus').style.display = 'none';
        document.getElementById('audioPreviewContainer').style.display = 'none';
        document.getElementById('audioPreviewPlayer').src = '';
        isWebAudioInitialized = false;
        audioFileGlobal = null;
        chosenGenreGlobal = "";
        selectedPointGlobal = null;
        isBypassed = false;
        document.querySelectorAll('.point-card').forEach(card => card.classList.remove('selected'));
        goToPage('page1');
    }

    window.onload = function() { 
        goToPage('page1'); 
        updateCustomPresetDropdown();
        updateEqLabel('Low');
        updateEqLabel('Mid');
        updateEqLabel('High');
    };
</script>

</body>
</html>
"""
                
