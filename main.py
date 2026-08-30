from fastapi import FastAPI
from fastapi.responses import HTMLResponse, FileResponse
import os

app = FastAPI()

# Laluan khas untuk membenarkan pelayan memaparkan gambar latar belakang
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
                background: rgba(11, 15, 25, 0.88);
                backdrop-filter: blur(5px);
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
                background: rgba(15, 23, 42, 0.9);
                padding: 16px 14px;
                border-radius: 12px;
                border: 1px solid rgba(59, 130, 246, 0.3);
                margin-bottom: 14px;
                box-sizing: border-box;
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
                background: rgba(15, 23, 42, 0.95);
                border-left: 4px solid #fbbf24;
                border-radius: 6px;
                box-sizing: border-box;
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
            }

            input[type="file"], select {
                background: #1e293b;
                border: 1px solid rgba(59, 130, 246, 0.5);
                padding: 12px 14px;
                border-radius: 10px;
                width: 100%;
                color: #ffffff;
                font-size: 13.5px;
                font-family: 'Montserrat', sans-serif;
                box-sizing: border-box;
                margin-bottom: 16px;
                outline: none;
            }

            input[type="file"] {
                border: 1px dashed #3b82f6;
                cursor: pointer;
            }

            select {
                cursor: pointer;
                font-weight: 600;
                text-align: center;
                text-align-last: center;
            }

            select option {
                background: #1e293b;
                color: #ffffff;
                padding: 12px;
                text-align: center;
            }

            select optgroup {
                background: #0f172a;
                color: #fbbf24;
                font-weight: 700;
                text-align: center;
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
                <select id="genreSelect">
                    <option value="" disabled selected>-- Sila Pilih Genre Lagu --</option>
                    
                    <optgroup label="🇲🇾 Melayu / Nusantara">
                        <option value="Pop Melayu">Pop Melayu</option>
                        <option value="Rock Melayu">Rock Melayu</option>
                        <option value="Balada Melayu">Balada Melayu</option>
                        <option value="Dangdut">Dangdut</option>
                        <option value="Malay Phonk">Malay Phonk</option>
                    </optgroup>
                    <optgroup label="🎤 Pop">
                        <option value="Pop">Pop</option>
                        <option value="Pop Ballad">Pop Ballad</option>
                        <option value="Indie Pop">Indie Pop</option>
                    </optgroup>
                    <optgroup label="🎸 Rock">
                        <option value="Rock">Rock</option>
                        <option value="Alternative Rock">Alternative Rock</option>
                        <option value="Classic Rock">Classic Rock</option>
                    </optgroup>
                    <optgroup label="🔥 Phonk">
                        <option value="Phonk">Phonk</option>
                        <option value="Drift Phonk">Drift Phonk</option>
                        <option value="Brazilian Phonk">Brazilian Phonk</option>
                    </optgroup>
                </select>

                <div class="btn-container">
                    <button type="button" class="btn" onclick="goToPage(1)">⬅️ Kembali</button>
                    <button type="button" class="btn" onclick="goToPage(3)">Seterusnya ➡️</button>
                </div>
            </div>

        </div>
    </div>

    <script>
        function goToPage(pageNumber) {
            document.getElementById('page1').classList.add('hidden');
            document.getElementById('page2').classList.add('hidden');
            
            if (pageNumber === 1) {
                document.getElementById('page1').classList.remove('hidden');
            } else if (pageNumber === 2) {
                document.getElementById('page2').classList.remove('hidden');
            } else if (pageNumber === 3) {
                alert('Sila teruskan ke tetapan seterusnya.');
            }
            window.scrollTo(0, 0);
        }

        function handleFileSelected(input) {
            if (input.files && input.files[0]) {
                document.getElementById('fileStatus').style.display = 'block';
            }
        }
    </script>

    </body>
    </html>
    """
    
