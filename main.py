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
        <title>BP AI Music Studio - Genre & Mastering Suite</title>
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
                background: rgba(11, 15, 25, 0.75);
                backdrop-filter: blur(3px);
                display: flex;
                flex-direction: column;
                padding: 24px 16px;
                box-sizing: border-box;
                min-height: 100vh;
            }

            .page-section {
                display: flex;
                flex-direction: column;
                width: 100%;
                flex: 1;
            }

            .page-center {
                justify-content: center;
                align-items: center;
                text-align: center;
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
                text-shadow: 0 3px 10px rgba(0, 0, 0, 0.9);
            }

            .content-readable-box {
                background: rgba(15, 23, 42, 0.95);
                padding: 18px 16px;
                border-radius: 12px;
                border: 1px solid rgba(59, 130, 246, 0.4);
                margin-bottom: 16px;
                box-sizing: border-box;
                box-shadow: 0 4px 20px rgba(0,0,0,0.8);
                width: 100%;
                max-height: 62vh;
                overflow-y: auto;
                text-align: left;
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
            }

            .poster-desc:last-child {
                margin-bottom: 0;
            }

            .poster-quote-box {
                margin-bottom: 20px;
                padding: 12px 14px;
                background: rgba(15, 23, 42, 0.95);
                border-left: 4px solid #fbbf24;
                border-radius: 6px;
                box-sizing: border-box;
                box-shadow: 0 4px 15px rgba(0,0,0,0.6);
                width: 100%;
                text-align: left;
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
                font-size: 12px;
                font-weight: 700;
                color: #60a5fa;
                margin-bottom: 8px;
                display: block;
                text-align: left;
            }

            /* Points Grid Styling */
            .points-grid {
                display: flex;
                flex-direction: column;
                gap: 10px;
                width: 100%;
            }

            .point-card {
                background: rgba(30, 41, 59, 0.9);
                border: 1px solid rgba(59, 130, 246, 0.4);
                padding: 12px 14px;
                border-radius: 10px;
                cursor: pointer;
                display: flex;
                align-items: center;
                justify-content: space-between;
                transition: all 0.2s ease;
            }

            .point-card:hover {
                background: rgba(37, 99, 235, 0.3);
                border-color: #3b82f6;
                transform: translateX(3px);
            }

            .point-card-title {
                font-family: 'Syne', sans-serif;
                font-size: 12.5px;
                font-weight: 700;
                color: #ffffff;
                text-align: left;
            }

            .point-card-desc {
                font-size: 10.5px;
                color: #94a3b8;
                margin-top: 2px;
                text-align: left;
            }

            .genre-group-title {
                font-family: 'Syne', sans-serif;
                font-size: 11.5px;
                font-weight: 700;
                color: #fbbf24;
                margin: 12px 0 6px 0;
                text-transform: uppercase;
                letter-spacing: 0.5px;
            }

            .genre-item-list {
                display: flex;
                flex-direction: column;
                gap: 5px;
                margin-bottom: 10px;
            }

            .genre-chip {
                background: rgba(30, 41, 59, 0.95);
                border: 1px solid rgba(59, 130, 246, 0.25);
                padding: 9px 12px;
                border-radius: 8px;
                font-size: 12px;
                color: #f1f5f9;
                cursor: pointer;
                transition: background 0.2s;
                text-align: left;
                font-weight: 500;
            }

            .genre-chip:hover {
                background: #3b82f6;
                color: #ffffff;
                border-color: #3b82f6;
            }

            input[type="file"] {
                background: rgba(30, 41, 59, 0.95);
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
            }

            .status-ready {
                font-size: 11px;
                color: #34d399;
                margin-top: -6px;
                margin-bottom: 12px;
                font-weight: 700;
                display: none;
                text-align: left;
            }

            .selected-display {
                background: rgba(30, 41, 59, 0.95);
                border: 1px solid #3b82f6;
                padding: 10px 12px;
                border-radius: 8px;
                font-size: 12px;
                color: #34d399;
                font-weight: 600;
                margin-bottom: 14px;
                text-align: center;
            }

            .btn-container {
                display: flex;
                gap: 10px;
                width: 100%;
                margin-bottom: 14px;
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

            .control-group {
                margin-bottom: 14px;
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
            }

            select.studio-select {
                background: rgba(30, 41, 59, 0.95);
                border: 1px solid rgba(59, 130, 246, 0.6);
                padding: 10px 12px;
                border-radius: 8px;
                width: 100%;
                color: #ffffff;
                font-size: 12px;
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
            
            <!-- HALAMAN 1: INTRO (Tengah) -->
            <div id="page1" class="page-section page-center">
                <div class="poster-title">MASTERING BP AI MUSIC STUDIO</div>
                
                <div class="btn-container">
                    <button type="button" class="btn" onclick="goToPage('page2')">Mula Mastering</button>
                </div>

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
            </div>

            <!-- HALAMAN 2: 15 POINT UTAMA GENRE -->
            <div id="page2" class="page-section hidden">
                <div class="poster-title">🎵 GENRE LAGU</div>

                <div class="content-readable-box">
                    <div class="points-grid">
                        <div class="point-card" onclick="openPoint(1)">
                            <div>
                                <div class="point-card-title">01 🇲🇾 Melayu / Nusantara</div>
                                <div class="point-card-desc">Malaya, Tradisional, Nusantara & Modern</div>
                            </div>
                            <span>➡️</span>
                        </div>
                        <div class="point-card" onclick="openPoint(2)">
                            <div>
                                <div class="point-card-title">02 🎤 Pop</div>
                                <div class="point-card-desc">Pop Ballad, Electropop, Synthpop, Indie Pop</div>
                            </div>
                            <span>➡️</span>
                        </div>
                        <div class="point-card" onclick="openPoint(3)">
                            <div>
                                <div class="point-card-title">03 🎸 Rock</div>
                                <div class="point-card-desc">Classic Rock, Alternative, Indie, Grunge, Metal</div>
                            </div>
                            <span>➡️</span>
                        </div>
                        <div class="point-card" onclick="openPoint(4)">
                            <div>
                                <div class="point-card-title">04 🎤 Hip Hop / Rap</div>
                                <div class="point-card-desc">Trap, Boom Bap, Drill, Old School, Melodic</div>
                            </div>
                            <span>➡️</span>
                        </div>
                        <div class="point-card" onclick="openPoint(5)">
                            <div>
                                <div class="point-card-title">05 🔥 Phonk</div>
                                <div class="point-card-desc">Drift Phonk, Brazilian, Dark, Malay Phonk</div>
                            </div>
                            <span>➡️</span>
                        </div>
                        <div class="point-card" onclick="openPoint(6)">
                            <div>
                                <div class="point-card-title">06 ⚡ Techno / Electronic</div>
                                <div class="point-card-desc">EDM, House, Trance, Dubstep, Amapiano</div>
                            </div>
                            <span>➡️</span>
                        </div>
                        <div class="point-card" onclick="openPoint(7)">
                            <div>
                                <div class="point-card-title">07 🌑 Dark / Cyber / Experimental</div>
                                <div class="point-card-desc">Darkwave, Synthwave, Cyberpunk, Ambient</div>
                            </div>
                            <span>➡️</span>
                        </div>
                        <div class="point-card" onclick="openPoint(8)">
                            <div>
                                <div class="point-card-title">08 🎷 R&B / Soul / Funk</div>
                                <div class="point-card-desc">Contemporary R&B, Neo Soul, Motown, Funk</div>
                            </div>
                            <span>➡️</span>
                        </div>
                        <div class="point-card" onclick="openPoint(9)">
                            <div>
                                <div class="point-card-title">09 🎷 Jazz / Blues</div>
                                <div class="point-card-desc">Smooth Jazz, Swing, Bebop, Slow Blues</div>
                            </div>
                            <span>➡️</span>
                        </div>
                        <div class="point-card" onclick="openPoint(10)">
                            <div>
                                <div class="point-card-title">10 🎸 Akustik / Folk</div>
                                <div class="point-card-desc">Acoustic Pop, Indie Folk, Lo-Fi, Chill, Lounge</div>
                            </div>
                            <span>➡️</span>
                        </div>
                        <div class="point-card" onclick="openPoint(11)">
                            <div>
                                <div class="point-card-title">11 🎻 Orkestra / Klasik</div>
                                <div class="point-card-desc">Classical, Piano Solo, Symphony, Cinematic Score</div>
                            </div>
                            <span>➡️</span>
                        </div>
                        <div class="point-card" onclick="openPoint(12)">
                            <div>
                                <div class="point-card-title">12 ❤️ Sedih / Emosi / Cinta</div>
                                <div class="point-card-desc">Sad Song, Heartbreak, Romantic, Slow Ballad</div>
                            </div>
                            <span>➡️</span>
                        </div>
                        <div class="point-card" onclick="openPoint(13)">
                            <div>
                                <div class="point-card-title">13 🌎 Antarabangsa</div>
                                <div class="point-card-desc">K-Pop, J-Pop, Bollywood, Latin, Reggae, Country</div>
                            </div>
                            <span>➡️</span>
                        </div>
                        <div class="point-card" onclick="openPoint(14)">
                            <div>
                                <div class="point-card-title">14 🤘 Metal</div>
                                <div class="point-card-desc">Heavy Metal, Metalcore, Death, Black, Doom</div>
                            </div>
                            <span>➡️</span>
                        </div>
                        <div class="point-card" onclick="openPoint(15)">
                            <div>
                                <div class="point-card-title">15 🎬 Cinematic / Mood / Khas</div>
                                <div class="point-card-desc">Epic, Horror, Motivational, Wedding, Raya</div>
                            </div>
                            <span>➡️</span>
                        </div>
                    </div>
                </div>

                <div class="btn-container">
                    <button type="button" class="btn" onclick="goToPage('page1')">Kembali</button>
                </div>
            </div>

            <!-- HALAMAN SUB-GENRE DINAMIK -->
            <div id="subGenrePage" class="page-section hidden">
                <div class="poster-title" id="subGenreTitle">PILIHAN GENRE</div>
                
                <div class="btn-container">
                    <button type="button" class="btn" onclick="goToPage('page2')">Kembali ke Senarai Point</button>
                </div>

                <div class="content-readable-box" id="subGenreContentContainer">
                    <!-- Dynamic List loaded via JS -->
                </div>
            </div>

            <!-- HALAMAN SETERUSNYA: FAIL & MASTERING -->
            <div id="pageUpload" class="page-section hidden">
                <div class="poster-title">TETAPAN MASTERING AKHIR</div>

                <div class="btn-container">
                    <button type="button" class="btn" onclick="goToPage('subGenrePage')">Kembali</button>
                    <button type="button" class="btn" onclick="startMasteringProcess()">Mula Proses</button>
                </div>

                <div class="content-readable-box">
                    <div class="selected-display" id="displayChosenGenre">Genre Dipilih: -</div>

                    <span class="section-label">📁 Pilih Fail Muzik</span>
                    <input type="file" id="audioFile" accept="audio/*" onchange="handleFileSelected(this)">
                    <div id="fileStatus" class="status-ready">✅ Fail berjaya dipilih!</div>

                    <div class="control-group">
                        <label class="control-label">🎚️ Profil Mastering</label>
                          <select class="studio-select" id="masteringProfile">
                            <option value="balanced">Balanced Pro (Seimbang)</option>
                            <option value="punchy">Punchy & Loud (Kuat & Bas Mantap)</option>
                            <option value="vocal">Vocal Clear (Vokal Lebih Jelas)</option>
                            <option value="warm">Warm Analog (Lembut & Klasik)</option>
                        </select>
                    </div>

                    <div class="control-group" style="margin-top: 12px;">
                        <label class="control-label">🔊 Tahap Kekuatan (Gain Boost)</label>
                        <select class="studio-select" id="gainBoost">
                            <option value="standard">Standard (Rata -14 LUFS)</option>
                            <option value="high">High Volume (-11 LUFS)</option>
                            <option value="max">Max Streaming (-9 LUFS)</option>
                        </select>
                    </div>
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
            2: {
                title: "🎤 02 - Pop",
                groups: [
                    { name: "Kategori Pop", items: ["Pop", "Pop Ballad", "Electropop", "Synthpop", "Dream Pop", "Indie Pop", "Teen Pop", "Adult Contemporary", "Dance Pop", "Power Pop", "Soft Pop", "Retro Pop", "City Pop", "Dark Pop", "Noir Pop", "Future Pop", "Neon Pop", "Experimental Pop"] }
                ]
            },
            3: {
                title: "🎸 03 - Rock",
                groups: [
                    { name: "Kategori Rock", items: ["Rock", "Soft Rock", "Classic Rock", "Hard Rock", "Alternative Rock", "Indie Rock", "Pop Rock", "Blues Rock", "Progressive Rock", "Psychedelic Rock", "Punk Rock", "Garage Rock", "Grunge", "Post-Rock", "Folk Rock", "Southern Rock", "Glam Rock", "Arena Rock", "Metal Rock"] }
                ]
            },
            4: {
                title: "🎤 04 - Hip Hop / Rap",
                groups: [
                    { name: "Kategori Hip Hop / Rap", items: ["Hip Hop", "Rap", "Old School Hip Hop", "Trap", "Boom Bap", "Lo-Fi Hip Hop", "Gangsta Rap", "Conscious Rap", "Melodic Rap", "Pop Rap", "Alternative Hip Hop", "R&B Rap", "Drill", "West Coast Hip Hop", "East Coast Hip Hop", "UK Drill", "Afro Drill", "Cyberpunk Trap", "Cinematic Trap", "Hybrid Trap"] }
                ]
            },
            5: {
                title: "🔥 05 - Phonk",
                groups: [
                    { name: "Kategori Phonk", items: ["Phonk", "Dark Phonk", "Drift Phonk", "Brazilian Phonk", "Memphis Phonk", "Aggressive Phonk", "Atmospheric Phonk", "Electro Phonk", "Trap Phonk", "Future Phonk", "Malay Phonk", "Neon Noir Phonk", "Neon Noir Phonk - Malay Bounce", "Dark Techno / Neon Noir Phonk - Malay Bounce"] }
                ]
            },
            6: {
                title: "⚡ 06 - Techno / Electronic",
                groups: [
                    { name: "Kategori Techno / Electronic", items: ["EDM", "Techno", "Dark Techno", "Hard Techno", "Industrial Techno", "Acid Techno", "Minimal Techno", "Melodic Techno", "Progressive Techno", "Techno Noir", "Cyber Techno", "House", "Deep House", "Tropical House", "Future House", "Progressive House", "Tech House", "Electro House", "Bass House", "G-House", "Slap House", "Afro House", "Trance", "Dubstep", "Drum & Bass", "Future Bass", "Breakbeat", "UK Garage", "Jersey Club", "Amapiano", "Industrial Bass", "Dark Electro", "Alternative Electronic", "Cinematic Electronic"] }
                ]
            },
            7: {
                title: "🌑 07 - Dark / Cyber / Experimental",
                groups: [
                    { name: "Kategori Dark / Cyber / Experimental", items: ["Darkwave", "Witch House", "Dark Synthwave", "Neon Synthwave", "Synthwave", "Vaporwave", "Cyberpunk", "Cyber Pop", "Cyberpunk Trap", "Noir Electronic", "Dark Ambient", "Ambient Dark", "Horror Electronic", "Atmospheric", "Experimental Electronic", "Experimental Pop", "Future Bass", "Future Garage", "Industrial", "Noise", "Glitch", "Glitch Hop"] }
                ]
            },
            8: {
                title: "🎷 08 - R&B / Soul / Funk",
                groups: [
                    { name: "Kategori R&B / Soul / Funk", items: ["R&B", "Contemporary R&B", "Soul", "Neo Soul", "Motown", "Funk", "Smooth Soul", "Gospel Soul", "R&B Ballad", "Funk Soul"] }
                ]
            },
            9: {
                title: "🎷 09 - Jazz / Blues",
                groups: [
                    { name: "Kategori Jazz / Blues", items: ["Jazz", "Smooth Jazz", "Contemporary Jazz", "Swing", "Bebop", "Fusion Jazz", "Latin Jazz", "Blues", "Slow Blues", "Blues Rock", "Soul Blues"] }
                ]
            },
            10: {
                title: "🎸 10 - Akustik / Folk",
                groups: [
                    { name: "Kategori Akustik / Folk", items: ["Acoustic", "Acoustic Pop", "Acoustic Ballad", "Folk", "Indie Folk", "Folk Pop", "Singer-Songwriter", "Coffeehouse", "Chill", "Lo-Fi", "Lounge", "Relaxing"] }
                ]
            },
            11: {
                title: "🎻 11 - Orkestra / Klasik",
                groups: [
                    { name: "Kategori Orkestra / Klasik", items: ["Classical", "Piano Solo", "Piano Ballad", "String Orchestra", "Symphony", "Chamber Music", "Cinematic", "Epic Orchestra", "Film Score", "Dramatic", "Emotional Orchestra", "Fantasy", "Medieval", "Baroque"] }
                ]
            },
            12: {
                title: "❤️ 12 - Sedih / Emosi / Cinta",
                groups: [
                    { name: "Kategori Sedih / Emosi / Cinta", items: ["Sad Song", "Emotional", "Heartbreak", "Melancholic", "Nostalgic", "Romantic", "Love Song", "Deep Emotional", "Tearjerker", "Slow Ballad", "Emotional Piano", "Emotional Acoustic", "Power Ballad"] }
                ]
            },
            13: {
                title: "🌎 13 - Antarabangsa",
                groups: [
                    { name: "Kategori Antarabangsa", items: ["K-Pop", "J-Pop", "C-Pop", "Bollywood", "Latin Pop", "Reggaeton", "Salsa", "Bachata", "Flamenco", "Afrobeat", "Afropop", "Reggae", "Dancehall", "Ska", "Country", "Country Pop", "Bluegrass", "Gospel", "Celtic", "Arabic", "Middle Eastern"] }
                ]
            },
            14: {
                title: "🤘 14 - Metal",
                groups: [
                    { name: "Kategori Metal", items: ["Heavy Metal", "Metalcore", "Death Metal", "Black Metal", "Symphonic Metal", "Power Metal", "Progressive Metal", "Nu Metal", "Alternative Metal", "Doom Metal"] }
                ]
            },
            15: {
                title: "🎬 15 - Cinematic / Mood / Khas",
                groups: [
                    { name: "Kategori Cinematic / Mood / Khas", items: ["Cinematic", "Epic", "Dark", "Mysterious", "Horror", "Thriller", "Adventure", "Fantasy", "Heroic", "Inspirational", "Motivational", "Spiritual", "Religious", "Peaceful", "Meditation", "Atmospheric", "Dreamy", "Powerful", "Energetic", "Romantic", "Vintage", "Retro", "80s", "90s", "Nostalgic", "Wedding", "Festival", "Party", "Christmas", "Raya / Aidilfitri"] }
                ]
            }
        };

        let chosenGenreGlobal = "";

        function goToPage(pageId) {
            document.querySelectorAll('.page-section').forEach(el => {
                el.classList.add('hidden');
            });
            document.getElementById(pageId).classList.remove('hidden');
            window.scrollTo(0, 0);
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
                    chip.onclick = function() {
                        selectGenreAndProceed(genre);
                    };
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
                document.getElementById('fileStatus').style.display = 'block';
            }
        }

        function startMasteringProcess() {
            alert('Proses mastering untuk genre "' + chosenGenreGlobal + '" berjaya dimulakan!');
        }

        window.onload = function() {
            goToPage('page1');
        };
    </script>

    </body>
    </html>
    """
     
