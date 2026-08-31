from fastapi import FastAPI
from fastapi.responses import HTMLResponse, FileResponse
import os

app = FastAPI()

@app.get("/Untitled design.png")
def get_image():
    return FileResponse("Untitled design.png")

@app.get("/", response_class=HTMLResponse)
def home():
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
                min-height: 100vh;
                box-sizing: border-box;
                overflow-x: hidden;
            }

            .studio-container {
                width: 100%;
                max-width: 480px;
                min-height: 100vh;
                background: #0b0f19;
                background-image: url('Untitled design.png');
                background-size: cover;
                background-position: center;
                background-attachment: fixed;
                position: relative;
                display: flex;
                flex-direction: column;
                box-shadow: 0 0 25px rgba(0,0,0,0.8);
                box-sizing: border-box;
            }

            .studio-overlay {
                flex: 1;
                background: rgba(11, 15, 25, 0.85);
                backdrop-filter: blur(4px);
                display: flex;
                flex-direction: column;
                justify-content: flex-start;
                padding: 24px 18px 40px 18px;
                box-sizing: border-box;
                min-height: 100vh;
            }

            .poster-title {
                font-family: 'Syne', sans-serif;
                font-size: 16px;
                font-weight: 800;
                color: #60a5fa;
                letter-spacing: 1.5px;
                text-transform: uppercase;
                margin-bottom: 16px;
                text-align: center;
                text-shadow: 0 3px 10px rgba(0, 0, 0, 0.9);
            }

            .content-readable-box {
                background: rgba(15, 23, 42, 0.9);
                padding: 16px 14px;
                border-radius: 12px;
                border: 1px solid rgba(59, 130, 246, 0.4);
                margin-bottom: 16px;
                box-sizing: border-box;
                box-shadow: 0 4px 20px rgba(0,0,0,0.6);
            }

            .poster-desc {
                font-size: 12px;
                line-height: 1.6;
                color: #f1f5f9;
                margin-bottom: 12px;
                font-weight: 500;
            }

            .poster-desc:last-child {
                margin-bottom: 0;
            }

            .poster-quote-box {
                margin-bottom: 20px;
                padding: 12px 14px;
                background: rgba(15, 23, 42, 0.9);
                border-left: 4px solid #fbbf24;
                border-radius: 6px;
                box-sizing: border-box;
                box-shadow: 0 4px 15px rgba(0,0,0,0.6);
            }

            .poster-quote-title {
                font-family: 'Syne', sans-serif;
                font-size: 11px;
                font-weight: 800;
                color: #ffffff;
                letter-spacing: 1px;
                text-transform: uppercase;
                margin-bottom: 2px;
            }

            .poster-quote {
                font-size: 11.5px;
                font-weight: 700;
                color: #fbbf24;
                font-style: italic;
            }

            .section-label {
                font-family: 'Syne', sans-serif;
                font-size: 13px;
                font-weight: 700;
                color: #60a5fa;
                margin-bottom: 6px;
                display: block;
                text-align: left;
                text-shadow: 0 2px 8px rgba(0,0,0,0.8);
            }

            input[type="file"] {
                background: rgba(30, 41, 59, 0.95);
                border: 1px dashed #3b82f6;
                padding: 12px 14px;
                border-radius: 10px;
                width: 100%;
                color: #ffffff;
                font-size: 13px;
                font-family: 'Montserrat', sans-serif;
                box-sizing: border-box;
                margin-bottom: 20px;
                cursor: pointer;
                box-shadow: 0 4px 15px rgba(0,0,0,0.5);
                outline: none;
            }

            .custom-dropdown-container {
                position: relative;
                width: 100%;
                margin-bottom: 24px;
                box-sizing: border-box;
            }

            .custom-dropdown-trigger {
                background: rgba(30, 41, 59, 0.95);
                border: 1px solid rgba(59, 130, 246, 0.6);
                padding: 12px 14px;
                border-radius: 10px;
                width: 100%;
                color: #ffffff;
                font-size: 13px;
                font-family: 'Montserrat', sans-serif;
                font-weight: 600;
                text-align: center;
                cursor: pointer;
                box-sizing: border-box;
                box-shadow: 0 4px 15px rgba(0,0,0,0.5);
                display: flex;
                justify-content: space-between;
                align-items: center;
            }

            .custom-dropdown-list {
                position: absolute;
                top: 100%;
                left: 0;
                width: 100%;
                max-height: 280px;
                overflow-y: auto;
                background: #0f172a;
                border: 1px solid rgba(59, 130, 246, 0.6);
                border-radius: 10px;
                margin-top: 5px;
                z-index: 100;
                box-shadow: 0 8px 25px rgba(0,0,0,0.9);
                box-sizing: border-box;
            }

            .dropdown-search-box {
                position: sticky;
                top: 0;
                background: #1e293b;
                padding: 10px;
                border-bottom: 1px solid rgba(59, 130, 246, 0.4);
                z-index: 10;
            }

            .dropdown-search-input {
                width: 100%;
                background: #0f172a;
                border: 1px solid rgba(59, 130, 246, 0.6);
                padding: 8px 12px;
                border-radius: 6px;
                color: #ffffff;
                font-size: 12px;
                font-family: 'Montserrat', sans-serif;
                box-sizing: border-box;
                outline: none;
            }

            .dropdown-group-header {
                background: #1e293b;
                color: #fbbf24;
                font-size: 11.5px;
                font-weight: 700;
                padding: 8px 12px;
                text-align: left;
                letter-spacing: 0.5px;
                border-top: 1px solid rgba(59, 130, 246, 0.2);
                border-bottom: 1px solid rgba(59, 130, 246, 0.2);
            }

            .dropdown-option {
                padding: 10px 14px;
                font-size: 12.5px;
                color: #f1f5f9;
                text-align: left;
                cursor: pointer;
                transition: background 0.2s;
            }

            .dropdown-option:hover {
                background: #3b82f6;
                color: #ffffff;
            }

            .status-ready {
                font-size: 12px;
                color: #34d399;
                margin-top: -12px;
                margin-bottom: 16px;
                font-weight: 700;
                display: none;
                text-align: left;
            }

            .btn-container {
                display: flex;
                gap: 10px;
                margin-top: auto;
                width: 100%;
                padding-top: 10px;
            }

            .btn {
                flex: 1;
                padding: 13px;
                border-radius: 10px;
                font-family: 'Syne', sans-serif;
                font-weight: 700;
                font-size: 13px;
                text-align: center;
                cursor: pointer;
                border: none;
                background: linear-gradient(135deg, #3b82f6, #2563eb);
                color: white;
                box-shadow: 0 4px 15px rgba(59, 130, 246, 0.5);
            }

            .control-group {
                margin-bottom: 16px;
            }

            .control-label {
                font-size: 12px;
                color: #93c5fd;
                margin-bottom: 6px;
                display: block;
                font-weight: 600;
            }

            select.studio-select {
                background: rgba(30, 41, 59, 0.95);
                border: 1px solid rgba(59, 130, 246, 0.6);
                padding: 11px 12px;
                border-radius: 8px;
                width: 100%;
                color: #ffffff;
                font-size: 13px;
                font-family: 'Montserrat', sans-serif;
                box-sizing: border-box;
                outline: none;
            }

            .hidden {
                display: none !important;
            }
        </style>
    </head>
    <body>

    <div class="studio-container">
        <div class="studio-overlay">
            
            <!-- HALAMAN 1 -->
            <div id="page1" style="display: flex; flex-direction: column; flex: 1;">
                <div class="poster-title">MASTERING BP AI MUSIC STUDIO</div>
                
                <div class="content-readable-box">
                    <div class="poster-desc">
                        Mastering BP AI MUSIC STUDIO adalah langkah terakhir dalam menghasilkan muzik yang lebih kemas, seimbang dan berkualiti. Setiap lagu diproses dengan teliti bagi memastikan vokal, muzik, bass dan keseluruhan bunyi kedengaran lebih jelas serta selesa didengar.
                    </div>
                    
                    <div class="poster-desc">
                        Dengan sentuhan mastering yang tepat, karya muzik anda dapat tampil lebih profesional dan mempunyai karakter bunyi yang lebih mantap.
                    </div>
                </div>

                <div class="poster-quote-box">
                    <div class="poster-quote-title">BP AI MUSIC STUDIO</div>
                    <div class="poster-quote">Memperkemas bunyi, menghidupkan karya.</div>
                </div>

                <div class="btn-container">
                    <button type="button" class="btn" onclick="goToPage(2)">Mula Mastering ➡️</button>
                </div>
            </div>

            <!-- HALAMAN 2 -->
            <div id="page2" class="hidden" style="display: flex; flex-direction: column; flex: 1;">
                <div class="poster-title">TETAPAN MASTERING</div>

                <span class="section-label">📁 Pilih Fail Muzik</span>
                <input type="file" id="audioFile" accept="audio/*" onchange="handleFileSelected(this)">
                <div id="fileStatus" class="status-ready">✅ Fail berjaya dipilih!</div>

                <span class="section-label">🎵 Pilih Kategori & Genre Lagu</span>
                
                <div class="custom-dropdown-container">
                    <div class="custom-dropdown-trigger" onclick="toggleDropdown()">
                        <span id="selectedGenreText">-- Sila Pilih Genre Lagu --</span> <span>▼</span>
                    </div>
                    
                    <div id="customDropdownList" class="custom-dropdown-list hidden">
                        <div class="dropdown-search-box">
                            <input type="text" id="genreSearchInput" class="dropdown-search-input" placeholder="🔍 Cari genre lagu..." onkeyup="filterGenres()">
                        </div>

                        <!-- 🇲🇾 Melayu / Nusantara -->
                        <div class="dropdown-group-header category-header">🇲🇾 Melayu / Nusantara</div>
                        <div class="dropdown-option" onclick="selectGenre('Malaya / Melayu')">Malaya / Melayu</div>
                        <div class="dropdown-option" onclick="selectGenre('Pop Melayu')">Pop Melayu</div>
                        <div class="dropdown-option" onclick="selectGenre('Rock Melayu')">Rock Melayu</div>
                        <div class="dropdown-option" onclick="selectGenre('Balada Melayu')">Balada Melayu</div>
                        <div class="dropdown-option" onclick="selectGenre('Melayu Klasik')">Melayu Klasik</div>
                        <div class="dropdown-option" onclick="selectGenre('Irama Malaysia')">Irama Malaysia</div>
                        <div class="dropdown-option" onclick="selectGenre('Lagu Asli')">Lagu Asli</div>
                        <div class="dropdown-option" onclick="selectGenre('Zapin')">Zapin</div>
                        <div class="dropdown-option" onclick="selectGenre('Joget')">Joget</div>
                        <div class="dropdown-option" onclick="selectGenre('Ghazal')">Ghazal</div>
                        <div class="dropdown-option" onclick="selectGenre('Keroncong')">Keroncong</div>
                        <div class="dropdown-option" onclick="selectGenre('Dangdut')">Dangdut</div>
                        <div class="dropdown-option" onclick="selectGenre('Campursari')">Campursari</div>
                        <div class="dropdown-option" onclick="selectGenre('Pop Nusantara')">Pop Nusantara</div>
                        <div class="dropdown-option" onclick="selectGenre('Etnik Nusantara')">Etnik Nusantara</div>
                        <div class="dropdown-option" onclick="selectGenre('Tradisional Melayu')">Tradisional Melayu</div>
                        <div class="dropdown-option" onclick="selectGenre('Tradisional Sabah')">Tradisional Sabah</div>
                        <div class="dropdown-option" onclick="selectGenre('Tradisional Sarawak')">Tradisional Sarawak</div>
                        <div class="dropdown-option" onclick="selectGenre('Minang')">Minang</div>
                        <div class="dropdown-option" onclick="selectGenre('Jawa')">Jawa</div>
                        <div class="dropdown-option" onclick="selectGenre('Sunda')">Sunda</div>
                        <div class="dropdown-option" onclick="selectGenre('Bugis')">Bugis</div>
                        <div class="dropdown-option" onclick="selectGenre('Batak')">Batak</div>
                        <div class="dropdown-option" onclick="selectGenre('Malay Bounce')">Malay Bounce</div>
                        <div class="dropdown-option" onclick="selectGenre('Malay Trap')">Malay Trap</div>
                        <div class="dropdown-option" onclick="selectGenre('Malay Phonk')">Malay Phonk</div>
                        <div class="dropdown-option" onclick="selectGenre('Malay Electronic')">Malay Electronic</div>
                        <div class="dropdown-option" onclick="selectGenre('Nusantara Electronic')">Nusantara Electronic</div>

                        <!-- 🎤 Pop -->
                        <div class="dropdown-group-header category-header">🎤 Pop</div>
                        <div class="dropdown-option" onclick="selectGenre('Pop')">Pop</div>
                        <div class="dropdown-option" onclick="selectGenre('Pop Ballad')">Pop Ballad</div>
                        <div class="dropdown-option" onclick="selectGenre('Electropop')">Electropop</div>
                        <div class="dropdown-option" onclick="selectGenre('Synthpop')">Synthpop</div>
                        <div class="dropdown-option" onclick="selectGenre('Dream Pop')">Dream Pop</div>
                        <div class="dropdown-option" onclick="selectGenre('Indie Pop')">Indie Pop</div>
                        <div class="dropdown-option" onclick="selectGenre('Teen Pop')">Teen Pop</div>
                        <div class="dropdown-option" onclick="selectGenre('Adult Contemporary')">Adult Contemporary</div>
                        <div class="dropdown-option" onclick="selectGenre('Dance Pop')">Dance Pop</div>
                        <div class="dropdown-option" onclick="selectGenre('Power Pop')">Power Pop</div>
                        <div class="dropdown-option" onclick="selectGenre('Soft Pop')">Soft Pop</div>
                        <div class="dropdown-option" onclick="selectGenre('Retro Pop')">Retro Pop</div>
                        <div class="dropdown-option" onclick="selectGenre('City Pop')">City Pop</div>
                        <div class="dropdown-option" onclick="selectGenre('Dark Pop')">Dark Pop</div>
                        <div class="dropdown-option" onclick="selectGenre('Noir Pop')">Noir Pop</div>
                        <div class="dropdown-option" onclick="selectGenre('Future Pop')">Future Pop</div>
                        <div class="dropdown-option" onclick="selectGenre('Neon Pop')">Neon Pop</div>
                        <div class="dropdown-option" onclick="selectGenre('Experimental Pop')">Experimental Pop</div>

                        <!-- 🎸 Rock -->
                        <div class="dropdown-group-header category-header">🎸 Rock</div>
                        <div class="dropdown-option" onclick="selectGenre('Rock')">Rock</div>
                        <div class="dropdown-option" onclick="selectGenre('Soft Rock')">Soft Rock</div>
                        <div class="dropdown-option" onclick="selectGenre('Classic Rock')">Classic Rock</div>
                        <div class="dropdown-option" onclick="selectGenre('Hard Rock')">Hard Rock</div>
                        <div class="dropdown-option" onclick="selectGenre('Alternative Rock')">Alternative Rock</div>
                        <div class="dropdown-option" onclick="selectGenre('Indie Rock')">Indie Rock</div>
                        <div class="dropdown-option" onclick="selectGenre('Pop Rock')">Pop Rock</div>
                        <div class="dropdown-option" onclick="selectGenre('Blues Rock')">Blues Rock</div>
                        <div class="dropdown-option" onclick="selectGenre('Progressive Rock')">Progressive Rock</div>
                        <div class="dropdown-option" onclick="selectGenre('Psychedelic Rock')">Psychedelic Rock</div>
                        <div class="dropdown-option" onclick="selectGenre('Punk Rock')">Punk Rock</div>
                        <div class="dropdown-option" onclick="selectGenre('Garage Rock')">Garage Rock</div>
                        <div class="dropdown-option" onclick="selectGenre('Grunge')">Grunge</div>
                        <div class="dropdown-option" onclick="selectGenre('Post-Rock')">Post-Rock</div>
                        <div class="dropdown-option" onclick="selectGenre('Folk Rock')">Folk Rock</div>
                        <div class="dropdown-option" onclick="selectGenre('Southern Rock')">Southern Rock</div>
                        <div class="dropdown-option" onclick="selectGenre('Glam Rock')">Glam Rock</div>
                        <div class="dropdown-option" onclick="selectGenre('Arena Rock')">Arena Rock</div>
                        <div class="dropdown-option" onclick="selectGenre('Metal Rock')">Metal Rock</div>

                        <!-- 🎤 Hip Hop / Rap -->
                        <div class="dropdown-group-header category-header">🎤 Hip Hop / Rap</div>
                        <div class="dropdown-option" onclick="selectGenre('Hip Hop')">Hip Hop</div>
                        <div class="dropdown-option" onclick="selectGenre('Rap')">Rap</div>
                        <div class="dropdown-option" onclick="selectGenre('Old School Hip Hop')">Old School Hip Hop</div>
                        <div class="dropdown-option" onclick="selectGenre('Trap')">Trap</div>
                        <div class="dropdown-option" onclick="selectGenre('Boom Bap')">Boom Bap</div>
                        <div class="dropdown-option" onclick="selectGenre('Lo-Fi Hip Hop')">Lo-Fi Hip Hop</div>
                        <div class="dropdown-option" onclick="selectGenre('Gangsta Rap')">Gangsta Rap</div>
                        <div class="dropdown-option" onclick="selectGenre('Conscious Rap')">Conscious Rap</div>
                        <div class="dropdown-option" onclick="selectGenre('Melodic Rap')">Melodic Rap</div>
                        <div class="dropdown-option" onclick="selectGenre('Pop Rap')">Pop Rap</div>
                        <div class="dropdown-option" onclick="selectGenre('Alternative Hip Hop')">Alternative Hip Hop</div>
                        <div class="dropdown-option" onclick="selectGenre('R&B Rap')">R&B Rap</div>
                        <div class="dropdown-option" onclick="selectGenre('Drill')">Drill</div>
                        <div class="dropdown-option" onclick="selectGenre('West Coast Hip Hop')">West Coast Hip Hop</div>
                        <div class="dropdown-option" onclick="selectGenre('East Coast Hip Hop')">East Coast Hip Hop</div>
                        <div class="dropdown-option" onclick="selectGenre('UK Drill')">UK Drill</div>
                        <div class="dropdown-option" onclick="selectGenre('Afro Drill')">Afro Drill</div>
                        <div class="dropdown-option" onclick="selectGenre('Cyberpunk Trap')">Cyberpunk Trap</div>
                        <div class="dropdown-option" onclick="selectGenre('Cinematic Trap')">Cinematic Trap</div>
                        <div class="dropdown-option" onclick="selectGenre('Hybrid Trap')">Hybrid Trap</div>

                        <!-- 🔥 Phonk -->
                        <div class="dropdown-group-header category-header">🔥 Phonk</div>
                        <div class="dropdown-option" onclick="selectGenre('Phonk')">Phonk</div>
                        <div class="dropdown-option" onclick="selectGenre('Dark Phonk')">Dark Phonk</div>
                        <div class="dropdown-option" onclick="selectGenre('Drift Phonk')">Drift Phonk</div>
                        <div class="dropdown-option" onclick="selectGenre('Brazilian Phonk')">Brazilian Phonk</div>
                        <div class="dropdown-option" onclick="selectGenre('Memphis Phonk')">Memphis Phonk</div>
                        <div class="dropdown-option" onclick="selectGenre('Aggressive Phonk')">Aggressive Phonk</div>
                        <div class="dropdown-option" onclick="selectGenre('Atmospheric Phonk')">Atmospheric Phonk</div>
                        <div class="dropdown-option" onclick="selectGenre('Electro Phonk')">Electro Phonk</div>
                        <div class="dropdown-option" onclick="selectGenre('Trap Phonk')">Trap Phonk</div>
                        <div class="dropdown-option" onclick="selectGenre('Future Phonk')">Future Phonk</div>
                        <div class="dropdown-option" onclick="selectGenre('Malay Phonk')">Malay Phonk</div>
                        <div class="dropdown-option" onclick="selectGenre('Neon Noir Phonk')">Neon Noir Phonk</div>
                        <div class="dropdown-option" onclick="selectGenre('Neon Noir Phonk - Malay Bounce')">Neon Noir Phonk - Malay Bounce</div>
                        <div class="dropdown-option" onclick="selectGenre('Dark Techno / Neon Noir Phonk - Malay Bounce')">Dark Techno / Neon Noir Phonk - Malay Bounce</div>

                        <!-- ⚡ Techno / Electronic -->
                        <div class="dropdown-group-header category-header">⚡ Techno / Electronic</div>
                        <div class="dropdown-option" onclick="selectGenre('EDM')">EDM</div>
                        <div class="dropdown-option" onclick="selectGenre('Techno')">Techno</div>
                        <div class="dropdown-option" onclick="selectGenre('Dark Techno')">Dark Techno</div>
                        <div class="dropdown-option" onclick="selectGenre('Hard Techno')">Hard Techno</div>
                        <div class="dropdown-option" onclick="selectGenre('Industrial Techno')">Industrial Techno</div>
                        <div class="dropdown-option" onclick="selectGenre('Acid Techno')">Acid Techno</div>
                        <div class="dropdown-option" onclick="selectGenre('Minimal Techno')">Minimal Techno</div>
                        <div class="dropdown-option" onclick="selectGenre('Melodic Techno')">Melodic Techno</div>
                        <div class="dropdown-option" onclick="selectGenre('Progressive Techno')">Progressive Techno</div>
                        <div class="dropdown-option" onclick="selectGenre('Techno Noir')">Techno Noir</div>
                        <div class="dropdown-option" onclick="selectGenre('Cyber Techno')">Cyber Techno</div>
                        <div class="dropdown-option" onclick="selectGenre('House')">House</div>
                        <div class="dropdown-option" onclick="selectGenre('Deep House')">Deep House</div>
                        <div class="dropdown-option" onclick="selectGenre('Tropical House')">Tropical House</div>
                        <div class="dropdown-option" onclick="selectGenre('Future House')">Future House</div>
                        <div class="dropdown-option" onclick="selectGenre('Progressive House')">Progressive House</div>
                        <div class="dropdown-option" onclick="selectGenre('Tech House')">Tech House</div>
                        <div class="dropdown-option" onclick="selectGenre('Electro House')">Electro House</div>
                        <div class="dropdown-option" onclick="selectGenre('Bass House')">Bass House</div>
                        <div class="dropdown-option" onclick="selectGenre('G-House')">G-House</div>
                        <div class="dropdown-option" onclick="selectGenre('Slap House')">Slap House</div>
                        <div class="dropdown-option" onclick="selectGenre('Afro House')">Afro House</div>
                        <div class="dropdown-option" onclick="selectGenre('Trance')">Trance</div>
                        <div class="dropdown-option" onclick="selectGenre('Dubstep')">Dubstep</div>
                        <div class="dropdown-option" onclick="selectGenre('Drum & Bass')">Drum & Bass</div>
                        <div class="dropdown-option" onclick="selectGenre('Future Bass')">Future Bass</div>
                        <div class="dropdown-option" onclick="selectGenre('Breakbeat')">Breakbeat</div>
                        <div class="dropdown-option" onclick="selectGenre('UK Garage')">UK Garage</div>
                        <div class="dropdown-option" onclick="selectGenre('Jersey Club')">Jersey Club</div>
                        <div class="dropdown-option" onclick="selectGenre('Amapiano')">Amapiano</div>
                        <div class="dropdown-option" onclick="selectGenre('Industrial Bass')">Industrial Bass</div>
                        <div class="dropdown-option" onclick="selectGenre('Dark Electro')">Dark Electro</div>
                        <div class="dropdown-option" onclick="selectGenre('Alternative Electronic')">Alternative Electronic</div>
                        <div class="dropdown-option" onclick="selectGenre('Cinematic Electronic')">Cinematic Electronic</div>

                        <!-- 🌑 Dark / Cyber / Experimental -->
                        <div class="dropdown-group-header category-header">🌑 Dark / Cyber / Experimental</div>
                        <div class="dropdown-option" onclick="selectGenre('Darkwave')">Darkwave</div>
                        <div class="dropdown-option" onclick="selectGenre('Witch House')">Witch House</div>
                        <div class="dropdown-option" onclick="selectGenre('Dark Synthwave')">Dark Synthwave</div>
                        <div class="dropdown-option" onclick="selectGenre('Neon Synthwave')">Neon Synthwave</div>
                        <div class="dropdown-option" onclick="selectGenre('Synthwave')">Synthwave</div>
                        <div class="dropdown-option" onclick="selectGenre('Vaporwave')">Vaporwave</div>
                        <div class="dropdown-option" onclick="selectGenre('Cyberpunk')">Cyberpunk</div>
                        <div class="dropdown-option" onclick="selectGenre('Cyber Pop')">Cyber Pop</div>
                        <div class="dropdown-option" onclick="selectGenre('Noir Electronic')">Noir Electronic</div>
                        <div class="dropdown-option" onclick="selectGenre('Dark Ambient')">Dark Ambient</div>
                        <div class="dropdown-option" onclick="selectGenre('Ambient Dark')">Ambient Dark</div>
                        <div class="dropdown-option" onclick="selectGenre('Horror Electronic')">Horror Electronic</div>
                        <div class="dropdown-option" onclick="selectGenre('Experimental Electronic')">Experimental Electronic</div>
                        <div class="dropdown-option" onclick="selectGenre('Future Garage')">Future Garage</div>
                        <div class="dropdown-option" onclick="selectGenre('Industrial')">Industrial</div>
                        <div class="dropdown-option" onclick="selectGenre('Noise')">Noise</div>
                        <div class="dropdown-option" onclick="selectGenre('Glitch')">Glitch</div>
                        <div class="dropdown-option" onclick="selectGenre('Glitch Hop')">Glitch Hop</div>

                        <!-- 🎷 R&B / Soul / Funk -->
                        <div class="dropdown-group-header category-header">🎷 R&B / Soul / Funk</div>
                        <div class="dropdown-option" onclick="selectGenre('R&B')">R&B</div>
                        <div class="dropdown-option" onclick="selectGenre('Contemporary R&B')">Contemporary R&B</div>
                        <div class="dropdown-option" onclick="selectGenre('Soul')">Soul</div>
                        <div class="dropdown-option" onclick="selectGenre('Neo Soul')">Neo Soul</div>
                        <div class="dropdown-option" onclick="selectGenre('Motown')">Motown</div>
                        <div class="dropdown-option" onclick="selectGenre('Funk')">Funk</div>
                        <div class="dropdown-option" onclick="selectGenre('Smooth Soul')">Smooth Soul</div>
                        <div class="dropdown-option" onclick="selectGenre('Gospel Soul')">Gospel Soul</div>
                        <div class="dropdown-option" onclick="selectGenre('R&B Ballad')">R&B Ballad</div>
                        <div class="dropdown-option" onclick="selectGenre('Funk Soul')">Funk Soul</div>

                        <!-- 🎷 Jazz / Blues -->
                        <div class="dropdown-group-header category-header">🎷 Jazz / Blues</div>
                        <div class="dropdown-option" onclick="selectGenre('Jazz')">Jazz</div>
                        <div class="dropdown-option" onclick="selectGenre('Smooth Jazz')">Smooth Jazz</div>
                        <div class="dropdown-option" onclick="selectGenre('Contemporary Jazz')">Contemporary Jazz</div>
                        <div class="dropdown-option" onclick="selectGenre('Swing')">Swing</div>
                        <div class="dropdown-option" onclick="selectGenre('Bebop')">Bebop</div>
                        <div class="dropdown-option" onclick="selectGenre('Fusion Jazz')">Fusion Jazz</div>
                        <div class="dropdown-option" onclick="selectGenre('Latin Jazz')">Latin Jazz</div>
                        <div class="dropdown-option" onclick="selectGenre('Blues')">Blues</div>
                        <div class="dropdown-option" onclick="selectGenre('Slow Blues')">Slow Blues</div>
                        <div class="dropdown-option" onclick="selectGenre('Soul Blues')">Soul Blues</div>

                        <!-- 🎸 Akustik / Folk -->
                        <div class="dropdown-group-header category-header">🎸 Akustik / Folk</div>
                        <div class="dropdown-option" onclick="selectGenre('Acoustic')">Acoustic</div>
                        <div class="dropdown-option" onclick="selectGenre('Acoustic Pop')">Acoustic Pop</div>
                        <div class="dropdown-option" onclick="selectGenre('Acoustic Ballad')">Acoustic Ballad</div>
                        <div class="dropdown-option" onclick="selectGenre('Folk')">Folk</div>
                        <div class="dropdown-option" onclick="selectGenre('Indie Folk')">Indie Folk</div>
                        <div class="dropdown-option" onclick="selectGenre('Folk Pop')">Folk Pop</div>
                        <div class="dropdown-option" onclick="selectGenre('Singer-Songwriter')">Singer-Songwriter</div>
                        <div class="dropdown-option" onclick="selectGenre('Coffeehouse')">Coffeehouse</div>
                        <div class="dropdown-option" onclick="selectGenre('Chill')">Chill</div>
                        <div class="dropdown-option" onclick="selectGenre('Lo-Fi')">Lo-Fi</div>
                        <div class="dropdown-option" onclick="selectGenre('Lounge')">Lounge</div>
                        <div class="dropdown-option" onclick="selectGenre('Relaxing')">Relaxing</div>

                        <!-- 🎻 Orkestra / Klasik -->
                        <div class="dropdown-group-header category-header">🎻 Orkestra / Klasik</div>
                        <div class="dropdown-option" onclick="selectGenre('Classical')">Classical</div>
                        <div class="dropdown-option" onclick="selectGenre('Piano Solo')">Piano Solo</div>
                        <div class="dropdown-option" onclick="selectGenre('Piano Ballad')">Piano Ballad</div>
                        <div class="dropdown-option" onclick="selectGenre('String Orchestra')">String Orchestra</div>
                        <div class="dropdown-option" onclick="selectGenre('Symphony')">Symphony</div>
                        <div class="dropdown-option" onclick="selectGenre('Chamber Music')">Chamber Music</div>
                        <div class="dropdown-option" onclick="selectGenre('Cinematic')">Cinematic</div>
                        <div class="dropdown-option" onclick="selectGenre('Epic Orchestra')">Epic Orchestra</div>
                        <div class="dropdown-option" onclick="selectGenre('Film Score')">Film Score</div>
                        <div class="dropdown-option" onclick="selectGenre('Dramatic')">Dramatic</div>
                        <div class="dropdown-option" onclick="selectGenre('Emotional Orchestra')">Emotional Orchestra</div>
                        <div class="dropdown-option" onclick="selectGenre('Fantasy')">Fantasy</div>
                        <div class="dropdown-option" onclick="selectGenre('Medieval')">Medieval</div>
                        <div class="dropdown-option" onclick="selectGenre('Baroque')">Baroque</div>

                        <!-- ❤️ Sedih / Emosi / Cinta -->
                        <div class="dropdown-group-header category-header">❤️ Sedih / Emosi / Cinta</div>
                        <div class="dropdown-option" onclick="selectGenre('Sad Song')">Sad Song</div>
                        <div class="dropdown-option" onclick="selectGenre('Emotional')">Emotional</div>
                        <div class="dropdown-option" onclick="selectGenre('Heartbreak')">Heartbreak</div>
                        <div class="dropdown-option" onclick="selectGenre('Melancholic')">Melancholic</div>
                        <div class="dropdown-option" onclick="selectGenre('Nostalgic')">Nostalgic</div>
                        <div class="dropdown-option" onclick="selectGenre('Romantic')">Romantic</div>
                        <div class="dropdown-option" onclick="selectGenre('Love Song')">Love Song</div>
                        <div class="dropdown-option" onclick="selectGenre('Deep Emotional')">Deep Emotional</div>
                        <div class="dropdown-option" onclick="selectGenre('Tearjerker')">Tearjerker</div>
                        <div class="dropdown-option" onclick="selectGenre('Slow Ballad')">Slow Ballad</div>
                        <div class="dropdown-option" onclick="selectGenre('Emotional Piano')">Emotional Piano</div>
                        <div class="dropdown-option" onclick="selectGenre('Emotional Acoustic')">Emotional Acoustic</div>
                        <div class="dropdown-option" onclick="selectGenre('Power Ballad')">Power Ballad</div>

                        <!-- 🌎 Antarabangsa -->
                        <div class="dropdown-group-header category-header">🌎 Antarabangsa</div>
                        <div class="dropdown-option" onclick="selectGenre('K-Pop')">K-Pop</div>
                        <div class="dropdown-option" onclick="selectGenre('J-Pop')">J-Pop</div>
                        <div class="dropdown-option" onclick="selectGenre('C-Pop')">C-Pop</div>
                        <div class="dropdown-option" onclick="selectGenre('Bollywood')">Bollywood</div>
                        <div class="dropdown-option" onclick="selectGenre('Latin Pop')">Latin Pop</div>
                        <div class="dropdown-option" onclick="selectGenre('Reggaeton')">Reggaeton</div>
                        <div class="dropdown-option" onclick="selectGenre('Salsa')">Salsa</div>
                        <div class="dropdown-option" onclick="selectGenre('Bachata')">Bachata</div>
                        <div class="dropdown-option" onclick="selectGenre('Flamenco')">Flamenco</div>
                        <div class="dropdown-option" onclick="selectGenre('Afrobeat')">Afrobeat</div>
                        <div class="dropdown-option" onclick="selectGenre('Afropop')">Afropop</div>
                        <div class="dropdown-option" onclick="selectGenre('Reggae')">Reggae</div>
                        <div class="dropdown-option" onclick="selectGenre('Dancehall')">Dancehall</div>
                        <div class="dropdown-option" onclick="selectGenre('Ska')">Ska</div>
                        <div class="dropdown-option" onclick="selectGenre('Country')">Country</div>
                        <div class="dropdown-option" onclick="selectGenre('Country Pop')">Country Pop</div>
                        <div class="dropdown-option" onclick="selectGenre('Bluegrass')">Bluegrass</div>
                        <div class="dropdown-option" onclick="selectGenre('Gospel')">Gospel</div>
                        <div class="dropdown-option" onclick="selectGenre('Celtic')">Celtic</div>
                        <div class="dropdown-option" onclick="selectGenre('Arabic')">Arabic</div>
                        <div class="dropdown-option" onclick="selectGenre('Middle Eastern')">Middle Eastern</div>

                        <!-- 🤘 Metal -->
                        <div class="dropdown-group-header category-header">🤘 Metal</div>
                        <div class="dropdown-option" onclick="selectGenre('Heavy Metal')">Heavy Metal</div>
                        <div class="dropdown-option" onclick="selectGenre('Metalcore')">Metalcore</div>
                        <div class="dropdown-option" onclick="selectGenre('Death Metal')">Death Metal</div>
                        <div class="dropdown-option" onclick="selectGenre('Black Metal')">Black Metal</div>
                        <div class="dropdown-option" onclick="selectGenre('Symphonic Metal')">Symphonic Metal</div>
                        <div class="dropdown-option" onclick="selectGenre('Power Metal')">Power Metal</div>
                        <div class="dropdown-option" onclick="selectGenre('Progressive Metal')">Progressive Metal</div>
                        <div class="dropdown-option" onclick="selectGenre('Nu Metal')">Nu Metal</div>
                        <div class="dropdown-option" onclick="selectGenre('Alternative Metal')">Alternative Metal</div>
                        <div class="dropdown-option" onclick="selectGenre('Doom Metal')">Doom Metal</div>

                        <!-- 🎬 Cinematic / Mood / Khas -->
                        <div class="dropdown-group-header category-header">🎬 Cinematic / Mood / Khas</div>
                        <div class="dropdown-option" onclick="selectGenre('Epic')">Epic</div>
                        <div class="dropdown-option" onclick="selectGenre('Dark')">Dark</div>
                        <div class="dropdown-option" onclick="selectGenre('Mysterious')">Mysterious</div>
                        <div class="dropdown-option" onclick="selectGenre('Horror')">Horror</div>
                        <div class="dropdown-option" onclick="selectGenre('Thriller')">Thriller</div>
                        <div class="dropdown-option" onclick="selectGenre('Adventure')">Adventure</div>
                        <div class="dropdown-option" onclick="selectGenre('Heroic')">Heroic</div>
                        <div class="dropdown-option" onclick="selectGenre('Inspirational')">Inspirational</div>
                        <div class="dropdown-option" onclick="selectGenre('Motivational')">Motivational</div>
                        <div class="dropdown-option" onclick="selectGenre('Spiritual')">Spiritual</div>
                        <div class="dropdown-option" onclick="selectGenre('Religious')">Religious</div>
                        <div class="dropdown-option" onclick="selectGenre('Peaceful')">Peaceful</div>
                        <div class="dropdown-option" onclick="selectGenre('Meditation')">Meditation</div>
                        <div class="dropdown-option" onclick="selectGenre('Atmospheric')">Atmospheric</div>
                        <div class="dropdown-option" onclick="selectGenre('Dreamy')">Dreamy</div>
                        <div class="dropdown-option" onclick="selectGenre('Powerful')">Powerful</div>
                        <div class="dropdown-option" onclick="selectGenre('Energetic')">Energetic</div>
                        <div class="dropdown-option" onclick="selectGenre('Vintage')">Vintage</div>
                        <div class="dropdown-option" onclick="selectGenre('Retro')">Retro</div>
                        <div class="dropdown-option" onclick="selectGenre('80s')">80s</div>
                        <div class="dropdown-option" onclick="selectGenre('90s')">90s</div>
                        <div class="dropdown-option" onclick="selectGenre('Wedding')">Wedding</div>
                        <div class="dropdown-option" onclick="selectGenre('Festival')">Festival</div>
                        <div class="dropdown-option" onclick="selectGenre('Party')">Party</div>
                        <div class="dropdown-option" onclick="selectGenre('Christmas')">Christmas</div>
                        <div class="dropdown-option" onclick="selectGenre('Raya / Aidilfitri')">Raya / Aidilfitri</div>
                    </div>
                </div>

                <div class="btn-container">
                    <button type="button" class="btn" onclick="goToPage(1)">⬅️ Kembali</button>
                    <button type="button" class="btn" onclick="goToPage(3)">Seterusnya ➡️</button>
                </div>
            </div>

            <!-- HALAMAN 3 -->
            <div id="page3" class="hidden" style="display: flex; flex-direction: column; flex: 1;">
                <div class="poster-title">TETAPAN AUDIO LANJUTAN</div>

                <div class="content-readable-box">
                    <div class="control-group">
                        <label class="control-label">🎚️ Profil Mastering</label>
                        <select class="studio-select" id="masteringProfile">
                            <option value="balanced">Balanced Pro (Seimbang)</option>
                            <option value="punchy">Punchy & Loud (Kuat & Bas Mantap)</option>
                            <option value="vocal">Vocal Clear (Vokal Lebih Jelas)</option>
                            <option value="warm">Warm Analog (Lembut & Klasik)</option>
                        </select>
                    </div>

                    <div class="control-group" style="margin-bottom: 0;">
                        <label class="control-label">🔊 Tahap Kekuatan (Gain Boost)</label>
                        <select class="studio-select" id="gainBoost">
                            <option value="standard">Standard (Rata -14 LUFS)</option>
                            <option value="high">High Volume (-11 LUFS)</option>
                            <option value="max">Max Streaming (-9 LUFS)</option>
                        </select>
                    </div>
                </div>

                <div class="btn-container">
                    <button type="button" class="btn" onclick="goToPage(2)">⬅️ Kembali</button>
                    <button type="button" class="btn" onclick="startMasteringProcess()">Mula Proses ⚡</button>
                </div>
            </div>

        </div>
    </div>

    <script>
        function goToPage(pageNumber) {
            document.getElementById('page1').style.display = 'none';
            document.getElementById('page2').style.display = 'none';
            document.getElementById('page3').style.display = 'none';
            
            if (pageNumber === 1) {
                document.getElementById('page1').style.display = 'flex';
            } else if (pageNumber === 2) {
                document.getElementById('page2').style.display = 'flex';
            } else if (pageNumber === 3) {
                let selected = document.getElementById('selectedGenreText').innerText;
                if(selected.includes('Sila Pilih')) {
                    alert('Sila pilih genre lagu terlebih dahulu.');
                    goToPage(2);
                    return;
                }
                document.getElementById('page3').style.display = 'flex';
            }
            window.scrollTo(0, 0);
        }

        function handleFileSelected(input) {
            if (input.files && input.files[0]) {
                document.getElementById('fileStatus').style.display = 'block';
            }
        }

        function toggleDropdown() {
            let list = document.getElementById('customDropdownList');
            list.classList.toggle('hidden');
            if(!list.classList.contains('hidden')) {
                document.getElementById('genreSearchInput').focus();
            }
        }

        function selectGenre(genreName) {
            document.getElementById('selectedGenreText').innerText = genreName;
            document.getElementById('customDropdownList').classList.add('hidden');
        }

        function filterGenres() {
            let input = document.getElementById('genreSearchInput').value.toLowerCase();
            let list = document.getElementById('customDropdownList');
            let options = list.getElementsByClassName('dropdown-option');
            let headers = list.getElementsByClassName('category-header');

            for (let i = 0; i < options.length; i++) {
                let txt = options[i].innerText || options[i].textContent;
                if (txt.toLowerCase().indexOf(input) > -1) {
                    options[i].style.display = "";
                } else {
                    options[i].style.display = "none";
                }
            }

            for (let h = 0; h < headers.length; h++) {
                let nextEl = headers[h].nextElementSibling;
                let hasVisible = false;
                while (nextEl && !nextEl.classList.contains('category-header')) {
                    if (nextEl.style.display !== "none") {
                        hasVisible = true;
                        break;
                    }
                    nextEl = nextEl.nextElementSibling;
                }
                headers[h].style.display = hasVisible ? "" : "none";
            }
        }

        function startMasteringProcess() {
            alert('Proses mastering berjaya dimulakan! Sila tunggu sebentar sementara AI memproses lagu anda.');
        }

        window.onclick = function(event) {
            if (!event.target.closest('.custom-dropdown-container')) {
                let list = document.getElementById('customDropdownList');
                if (list && !list.classList.contains('hidden')) {
                    list.classList.add('hidden');
                }
            }
        }

        window.onload = function() {
            goToPage(1);
        };
    </script>

    </body>
    </html>
    """
