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
                background: rgba(11, 15, 25, 0.7);
                backdrop-filter: blur(3px);
                display: flex;
                flex-direction: column;
                justify-content: center;
                padding: 24px 18px;
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
                margin-bottom: 12px;
                text-align: center;
                text-shadow: 0 3px 10px rgba(0, 0, 0, 0.9);
            }

            .content-readable-box {
                background: rgba(15, 23, 42, 0.85);
                padding: 16px 14px;
                border-radius: 12px;
                border: 1px solid rgba(59, 130, 246, 0.4);
                margin-bottom: 14px;
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
                margin-bottom: 16px;
                padding: 10px 14px;
                background: rgba(15, 23, 42, 0.85);
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
                text-align: center;
                text-shadow: 0 2px 8px rgba(0,0,0,0.8);
            }

            input[type="file"] {
                background: rgba(30, 41, 59, 0.9);
                border: 1px dashed #3b82f6;
                padding: 12px 14px;
                border-radius: 10px;
                width: 100%;
                color: #ffffff;
                font-size: 13.5px;
                font-family: 'Montserrat', sans-serif;
                box-sizing: border-box;
                margin-bottom: 16px;
                cursor: pointer;
                box-shadow: 0 4px 15px rgba(0,0,0,0.5);
                outline: none;
            }

            /* Custom Dropdown Styling */
            .custom-dropdown-container {
                position: relative;
                width: 100%;
                margin-bottom: 16px;
                box-sizing: border-box;
            }

            .custom-dropdown-trigger {
                background: rgba(30, 41, 59, 0.95);
                border: 1px solid rgba(59, 130, 246, 0.6);
                padding: 12px 14px;
                border-radius: 10px;
                width: 100%;
                color: #ffffff;
                font-size: 13.5px;
                font-family: 'Montserrat', sans-serif;
                font-weight: 600;
                text-align: center;
                cursor: pointer;
                box-sizing: border-box;
                box-shadow: 0 4px 15px rgba(0,0,0,0.5);
                display: flex;
                justify-content: center;
                align-items: center;
                gap: 8px;
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
                box-shadow: 0 8px 25px rgba(0,0,0,0.8);
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
                font-size: 12.5px;
                font-family: 'Montserrat', sans-serif;
                box-sizing: border-box;
                outline: none;
            }

            .dropdown-group-header {
                background: #1e293b;
                color: #fbbf24;
                font-size: 12px;
                font-weight: 700;
                padding: 8px 12px;
                text-align: center;
                letter-spacing: 0.5px;
                border-top: 1px solid rgba(59, 130, 246, 0.2);
                border-bottom: 1px solid rgba(59, 130, 246, 0.2);
            }

            .dropdown-option {
                padding: 10px 14px;
                font-size: 13px;
                color: #f1f5f9;
                text-align: center;
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
                margin-top: -10px;
                margin-bottom: 14px;
                font-weight: 700;
                display: none;
                text-align: center;
            }

            .btn-container {
                display: flex;
                gap: 10px;
                margin-top: 10px;
                width: 100%;
            }

            .btn {
                flex: 1;
                padding: 13px;
                border-radius: 10px;
                font-family: 'Syne', sans-serif;
                font-weight: 700;
                font-size: 13.5px;
                text-align: center;
                cursor: pointer;
                border: none;
                background: linear-gradient(135deg, #3b82f6, #2563eb);
                color: white;
                box-shadow: 0 4px 15px rgba(59, 130, 246, 0.5);
            }

            .control-group {
                margin-bottom: 14px;
            }

            .control-label {
                font-size: 12px;
                color: #93c5fd;
                margin-bottom: 4px;
                display: block;
                font-weight: 600;
            }

            select.studio-select {
                background: rgba(30, 41, 59, 0.95);
                border: 1px solid rgba(59, 130, 246, 0.6);
                padding: 10px 12px;
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
            <div id="page1">
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
            <div id="page2" class="hidden">
                <div class="poster-title">TETAPAN MASTERING</div>

                <span class="section-label">📁 Pilih Fail Muzik</span>
                <input type="file" id="audioFile" accept="audio/*" onchange="handleFileSelected(this)">
                <div id="fileStatus" class="status-ready">✅ Fail berjaya dipilih!</div>

                <span class="section-label">🎵 Pilih Genre Lagu</span>
                
                <!-- Custom Dropdown Menu -->
                <div class="custom-dropdown-container">
                    <div class="custom-dropdown-trigger" onclick="toggleDropdown()">
                        <span id="selectedGenreText">-- Sila Pilih Genre Lagu --</span> <span>▼</span>
                    </div>
                    
                    <div id="customDropdownList" class="custom-dropdown-list hidden">
                        <div class="dropdown-search-box">
                            <input type="text" id="genreSearchInput" class="dropdown-search-input" placeholder="🔍 Cari genre lagu..." onkeyup="filterGenres()">
                        </div>

                        <!-- Melayu / Nusantara -->
                        <div class="dropdown-group-header category-header">🇲🇾 Melayu / Nusantara</div>
                        <div class="dropdown-option" onclick="selectGenre('Malaya / Melayu')">Malaya / Melayu</div>
                        <div class="dropdown-option" onclick="selectGenre('Pop Melayu')">Pop Melayu</div>
                        <div class="dropdown-option" onclick="selectGenre('Rock Melayu')">Rock Melayu</div>
                        <div class="dropdown-option" onclick="selectGenre('Balada Melayu')">Balada Melayu</div>
                        <div class="dropdown-option" onclick="selectGenre('Malay Phonk')">Malay Phonk</div>

                        <!-- Pop -->
                        <div class="dropdown-group-header category-header">🎤 Pop</div>
                        <div class="dropdown-option" onclick="selectGenre('Pop')">Pop</div>
                        <div class="dropdown-option" onclick="selectGenre('Pop Ballad')">Pop Ballad</div>
                        <div class="dropdown-option" onclick="selectGenre('Indie Pop')">Indie Pop</div>

                        <!-- Rock -->
                        <div class="dropdown-group-header category-header">🎸 Rock</div>
                        <div class="dropdown-option" onclick="selectGenre('Rock')">Rock</div>
                        <div class="dropdown-option" onclick="selectGenre('Classic Rock')">Classic Rock</div>
                        <div class="dropdown-option" onclick="selectGenre('Alternative Rock')">Alternative Rock</div>

                        <!-- Phonk -->
                        <div class="dropdown-group-header category-header">🔥 Phonk</div>
                        <div class="dropdown-option" onclick="selectGenre('Phonk')">Phonk</div>
                        <div class="dropdown-option" onclick="selectGenre('Drift Phonk')">Drift Phonk</div>
                        <div class="dropdown-option" onclick="selectGenre('Brazilian Phonk')">Brazilian Phonk</div>
                    </div>
                </div>

                <div class="btn-container">
                    <button type="button" class="btn" onclick="goToPage(1)">⬅️ Kembali</button>
                    <button type="button" class="btn" onclick="goToPage(3)">Seterusnya ➡️</button>
                </div>
            </div>

            <!-- HALAMAN 3 -->
            <div id="page3" class="hidden">
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

                    <div class="control-group">
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
            document.getElementById('page1').classList.add('hidden');
            document.getElementById('page2').classList.add('hidden');
            document.getElementById('page3').classList.add('hidden');
            
            if (pageNumber === 1) {
                document.getElementById('page1').classList.remove('hidden');
            } else if (pageNumber === 2) {
                document.getElementById('page2').classList.remove('hidden');
            } else if (pageNumber === 3) {
                let selected = document.getElementById('selectedGenreText').innerText;
                if(selected.includes('Sila Pilih')) {
                    alert('Sila pilih genre lagu terlebih dahulu.');
                    goToPage(2);
                    return;
                }
                document.getElementById('page3').classList.remove('hidden');
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
    </script>

    
