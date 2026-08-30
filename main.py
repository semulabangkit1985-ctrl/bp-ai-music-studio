<!DOCTYPE html>
<html lang="ms">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>BP AI Music Studio - Pro Mastering Suite</title>
    <!-- FONT GOOGLE MODEN & STYLISH (SYNE & MONTSERRAT) -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700&family=Syne:wght@700;800&display=swap" rel="stylesheet">
    
    <style>
        body {
            background: #0b0f19;
            color: #ffffff;
            font-family: 'Montserrat', sans-serif;
            -webkit-font-smoothing: antialiased;
            text-rendering: optimizeLegibility;
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
            position: relative;
            margin: 0 auto;
            box-shadow: 0 15px 35px rgba(0,0,0,0.9);
            box-sizing: border-box;
            background: #0b0f19;
            overflow: hidden;
            display: grid;
            grid-template-columns: 1fr;
            grid-template-rows: 1fr;
            min-height: 100vh;
        }

        /* LATAR BELAKANG POSTER KEKAL DI SEMUA HALAMAN */
        .global-poster-bg, .page-content {
            grid-area: 1 / 1;
        }

        .global-poster-bg {
            width: 100%;
            height: 100%;
            object-fit: cover;
            display: block;
            filter: brightness(1.15) contrast(1.05); 
        }

        /* KANDUNGAN HALAMAN 1 */
        .page-content {
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            padding: 22px 16px;
            box-sizing: border-box;
            text-align: center;
            background: rgba(11, 15, 25, 0.45);
            z-index: 2;
        }

        .poster-title {
            font-family: 'Syne', sans-serif;
            font-size: 15px;
            font-weight: 800;
            color: #60a5fa;
            letter-spacing: 1.5px;
            text-transform: uppercase;
            margin-bottom: 10px;
            text-shadow: 0 3px 10px rgba(0, 0, 0, 0.98);
        }

        .content-readable-box {
            background: rgba(11, 15, 25, 0.85);
            padding: 14px 12px;
            border-radius: 10px;
            backdrop-filter: blur(6px);
            border: 1px solid rgba(59, 130, 246, 0.2);
            margin-bottom: 10px;
            box-shadow: 0 8px 20px rgba(0, 0, 0, 0.8);
            width: 100%;
            box-sizing: border-box;
        }

        .poster-desc {
            font-size: 11px;
            line-height: 1.6;
            color: #f1f5f9;
            margin-bottom: 10px;
            text-shadow: 0 1px 4px rgba(0, 0, 0, 0.9);
            font-weight: 500;
            text-align: left;
        }

        .poster-desc:last-child {
            margin-bottom: 0;
        }

        .poster-quote-box {
            margin-top: 2px;
            margin-bottom: 12px;
            padding: 8px 12px;
            background: rgba(15, 23, 42, 0.85);
            border-left: 4px solid #fbbf24;
            border-radius: 6px;
            text-align: left;
            width: 100%;
            box-sizing: border-box;
            backdrop-filter: blur(4px);
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
            text-shadow: 0 1px 4px rgba(0,0,0,0.9);
        }

        .poster-quote {
            font-size: 11px;
            font-weight: 700;
            color: #fbbf24;
            font-style: italic;
            text-shadow: 0 1px 4px rgba(0,0,0,0.9);
        }

        /* KOTAK BORANG UNTUK HALAMAN 2, 3, 4 DENGAN LATAR BELAKANG POSTER DI BELAKANGNYA */
        .overlay-card {
            position: absolute;
            bottom: 0;
            left: 0;
            width: 100%;
            background: linear-gradient(to top, rgba(11, 15, 25, 0.96) 80%, rgba(11, 15, 25, 0.88) 95%, rgba(11, 15, 25, 0.7));
            padding: 25px 20px 20px 20px;
            box-sizing: border-box;
            border-top-left-radius: 16px;
            border-top-right-radius: 16px;
            z-index: 10;
            backdrop-filter: blur(4px);
            box-shadow: 0 -10px 30px rgba(0,0,0,0.8);
        }

        .section-label {
            font-family: 'Syne', sans-serif;
            font-size: 12.5px;
            font-weight: 700;
            color: #60a5fa;
            margin-bottom: 5px;
            display: block;
            letter-spacing: 0.5px;
        }

        input[type="file"], input[type="text"] {
            background: #1e293b;
            border: 1px solid rgba(59, 130, 246, 0.3);
            padding: 10px 12px;
            border-radius: 8px;
            width: 100%;
            color: #cbd5e1;
            font-size: 13px;
            font-family: 'Montserrat', sans-serif;
            box-sizing: border-box;
            margin-bottom: 10px;
        }

        input[type="file"] {
            border: 1px dashed #3b82f6;
            cursor: pointer;
        }

        .status-ready {
            font-size: 11.5px;
            color: #34d399;
            margin-bottom: 10px;
            font-weight: 700;
            display: none;
        }

        .custom-select-box {
            position: relative;
            margin-bottom: 10px;
        }

        .select-trigger {
            background: #1e293b;
            border: 1px solid rgba(59, 130, 246, 0.3);
            padding: 10px 12px;
            border-radius: 8px;
            width: 100%;
            color: #cbd5e1;
            font-size: 13px;
            font-family: 'Montserrat', sans-serif;
            box-sizing: border-box;
            cursor: pointer;
            font-weight: 600;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .select-dropdown {
            position: absolute;
            bottom: 100%;
            left: 0;
            width: 100%;
            max-height: 240px;
            overflow-y: auto;
            background: #1e293b;
            border: 1px solid #3b82f6;
            border-radius: 8px;
            z-index: 99;
            display: none;
            box-shadow: 0 -10px 20px rgba(0,0,0,0.4);
            box-sizing: border-box;
        }

        .select-dropdown.show {
            display: block;
        }

        .option-group-title {
            font-family: 'Syne', sans-serif;
            font-size: 11px;
            color: #fbbf24;
            padding: 8px 12px;
            background: #0f172a;
            font-weight: 700;
            letter-spacing: 0.5px;
            position: sticky;
            top: 0;
            z-index: 2;
        }

        .option-item {
            padding: 9px 12px;
            font-size: 12px;
            color: #cbd5e1;
            cursor: pointer;
            border-bottom: 1px solid #334155;
            font-weight: 500;
        }

        .option-item:hover {
            background: #3b82f6;
            color: white;
        }

        .grid-effects {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 8px;
            margin-bottom: 12px;
        }

        .effect-btn {
            background: #1e293b;
            border: 1px solid rgba(59, 130, 246, 0.3);
            color: white;
            padding: 9px;
            border-radius: 8px;
            font-size: 11.5px;
            font-weight: 700;
            cursor: pointer;
            text-align: center;
            font-family: 'Syne', sans-serif;
        }

        .effect-btn.active {
            background: #3b82f6;
            border-color: #60a5fa;
            box-shadow: 0 0 10px rgba(59, 130, 246, 0.5);
        }

        .btn-container {
            display: flex;
            gap: 8px;
            margin-top: 10px;
            width: 100%;
        }

        .btn {
            flex: 1;
            padding: 12px;
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
            transition: all 0.3s ease;
            letter-spacing: 0.5px;
        }

        .btn:hover {
            background: linear-gradient(135deg, #2563eb, #1d4ed8);
            transform: translateY(-1px);
        }

        .btn-back {
            background: #334155;
            box-shadow: none;
        }

        .hidden {
            display: none !important;
        }

        audio {
            width: 100%;
            margin-top: 6px;
            margin-bottom: 12px;
            border-radius: 8px;
            height: 36px;
        }

        .info-box {
            background: #1e293b;
            padding: 10px 12px;
            border-radius: 8px;
            margin-bottom: 12px;
            font-size: 11.5px;
            border-left: 4px solid #3b82f6;
            line-height: 1.5;
            color: #94a3b8;
            font-weight: 500;
        }

        .info-box strong {
            color: #60a5fa;
            font-weight: 700;
        }
    </style>
</head>
<body>

<div class="studio-container">
    <!-- LATAR BELAKANG POSTER KEKAL DI SEMUA HALAMAN -->
    <img src="Untitled design.png" alt="BP AI Music Studio Background Poster" class="global-poster-bg">

    <!-- HALAMAN 1 -->
    <div id="page1" class="page-content">
        <div class="poster-title">MASTERING BP AI MUSIC STUDIO</div>
        
        <div class="content-readable-box">
            <div class="poster-desc">
                Mastering BP AI MUSIC STUDIO adalah langkah terakhir dalam menghasilkan muzik yang lebih kemas, seimbang dan berkualiti. Setiap lagu diproses dengan teliti bagi memastikan vokal, muzik, bass dan keseluruhan bunyi kedengaran lebih jelas serta selesa didengar.
            </div>
            
            <div class="poster-desc">
                Dengan sentuhan mastering yang tepat, karya muzik anda dapat tampil lebih profesional dan mempunyai karakter bunyi yang lebih mantap — sama ada untuk YouTube, platform digital, video atau koleksi peribadi.
            </div>
        </div>

        <div class="poster-quote-box">
            <div class="poster-quote-title">BP AI MUSIC STUDIO</div>
            <div class="poster-quote">Memperkemas bunyi, menghidupkan karya.</div>
        </div>

        <div class="btn-container" style="margin-top: 2px;">
            <button type="button" class="btn" onclick="goToPage(2)">Mula Mastering ➡️</button>
        </div>
    </div>

    <!-- HALAMAN 2 -->
    <div id="page2" class="overlay-card hidden">
        <span class="section-label">📁 Choose File (Music)</span>
        <input type="file" id="audioFile" accept="audio/*" onchange="handleFileSelected(this)">
        <div id="fileStatus" class="status-ready">✅ Fail berjaya dipilih!</div>

        <span class="section-label">🎵 Pilih Genre Lagu</span>
        <input type="text" id="genreSearch" placeholder="Cari genre..." onkeyup="filterGenres()">

        <div class="custom-select-box">
            <div class="select-trigger" id="selectTrigger" onclick="toggleDropdown()">
                <span id="selectedGenreText">Dark Techno / Neon Noir Phonk - Malay Bounce</span>
                <span>▼</span>
            </div>
            <div class="select-dropdown" id="selectDropdown">
                <!-- 🇲🇾 Melayu / Nusantara -->
                <div class="option-group-title">🇲🇾 Melayu / Nusantara</div>
                <div class="option-item" onclick="selectGenre('Malaya / Melayu')">Malaya / Melayu</div>
                <div class="option-item" onclick="selectGenre('Pop Melayu')">Pop Melayu</div>
                <div class="option-item" onclick="selectGenre('Rock Melayu')">Rock Melayu</div>
                <div class="option-item" onclick="selectGenre('Balada Melayu')">Balada Melayu</div>
                <div class="option-item" onclick="selectGenre('Melayu Klasik')">Melayu Klasik</div>
                <div class="option-item" onclick="selectGenre('Irama Malaysia')">Irama Malaysia</div>
                <div class="option-item" onclick="selectGenre('Lagu Asli')">Lagu Asli</div>
                <div class="option-item" onclick="selectGenre('Zapin')">Zapin</div>
                <div class="option-item" onclick="selectGenre('Joget')">Joget</div>
                <div class="option-item" onclick="selectGenre('Ghazal')">Ghazal</div>
                <div class="option-item" onclick="selectGenre('Keroncong')">Keroncong</div>
                <div class="option-item" onclick="selectGenre('Dangdut')">Dangdut</div>
                <div class="option-item" onclick="selectGenre('Campursari')">Campursari</div>
                <div class="option-item" onclick="selectGenre('Pop Nusantara')">Pop Nusantara</div>
                <div class="option-item" onclick="selectGenre('Etnik Nusantara')">Etnik Nusantara</div>
                <div class="option-item" onclick="selectGenre('Tradisional Melayu')">Tradisional Melayu</div>
                <div class="option-item" onclick="selectGenre('Tradisional Sabah')">Tradisional Sabah</div>
                <div class="option-item" onclick="selectGenre('Tradisional Sarawak')">Tradisional Sarawak</div>
                <div class="option-item" onclick="selectGenre('Minang')">Minang</div>
                <div class="option-item" onclick="selectGenre('Jawa')">Jawa</div>
                <div class="option-item" onclick="selectGenre('Sunda')">Sunda</div>
                <div class="option-item" onclick="selectGenre('Bugis')">Bugis</div>
                <div class="option-item" onclick="selectGenre('Batak')">Batak</div>
                <div class="option-item" onclick="selectGenre('Malay Bounce')">Malay Bounce</div>
                <div class="option-item" onclick="selectGenre('Malay Trap')">Malay Trap</div>
                <div class="option-item" onclick="selectGenre('Malay Phonk')">Malay Phonk</div>
                <div class="option-item" onclick="selectGenre('Malay Electronic')">Malay Electronic</div>
                <div class="option-item" onclick="selectGenre('Nusantara Electronic')">Nusantara Electronic</div>

                <!-- 🎤 Pop -->
                <div class="option-group-title">🎤 Pop</div>
                <div class="option-item" onclick="selectGenre('Pop')">Pop</div>
                <div class="option-item" onclick="selectGenre('Pop Ballad')">Pop Ballad</div>
                <div class="option-item" onclick="selectGenre('Electropop')">Electropop</div>
                <div class="option-item" onclick="selectGenre('Synthpop')">Synthpop</div>
                <div class="option-item" onclick="selectGenre('Dream Pop')">Dream Pop</div>
                <div class="option-item" onclick="selectGenre('Indie Pop')">Indie Pop</div>
                <div class="option-item" onclick="selectGenre('Teen Pop')">Teen Pop</div>
                <div class="option-item" onclick="selectGenre('Adult Contemporary')">Adult Contemporary</div>
                <div class="option-item" onclick="selectGenre('Dance Pop')">Dance Pop</div>
                <div class="option-item" onclick="selectGenre('Power Pop')">Power Pop</div>
                <div class="option-item" onclick="selectGenre('Soft Pop')">Soft Pop</div>
                <div class="option-item" onclick="selectGenre('Retro Pop')">Retro Pop</div>
                <div class="option-item" onclick="selectGenre('City Pop')">City Pop</div>
                <div class="option-item" onclick="selectGenre('Dark Pop')">Dark Pop</div>
                <div class="option-item" onclick="selectGenre('Noir Pop')">Noir Pop</div>
                <div class="option-item" onclick="selectGenre('Future Pop')">Future Pop</div>
                <div class="option-item" onclick="selectGenre('Neon Pop')">Neon Pop</div>
                <div class="option-item" onclick="selectGenre('Experimental Pop')">Experimental Pop</div>

                <!-- 🎸 Rock -->
                <div class="option-group-title">🎸 Rock</div>
                <div class="option-item" onclick="selectGenre('Rock')">Rock</div>
                <div class="option-item" onclick="selectGenre('Soft Rock')">Soft Rock</div>
                <div class="option-item" onclick="selectGenre('Classic Rock')">Classic Rock</div>
                <div class="option-item" onclick="selectGenre('Hard Rock')">Hard Rock</div>
                <div class="option-item" onclick="selectGenre('Alternative Rock')">Alternative Rock</div>
                <div class="option-item" onclick="selectGenre('Indie Rock')">Indie Rock</div>
                <div class="option-item" onclick="selectGenre('Pop Rock')">Pop Rock</div>
                <div class="option-item" onclick="selectGenre('Blues Rock')">Blues Rock</div>
                <div class="option-item" onclick="selectGenre('Progressive Rock')">Progressive Rock</div>
                <div class="option-item" onclick="selectGenre('Psychedelic Rock')">Psychedelic Rock</div>
                <div class="option-item" onclick="selectGenre('Punk Rock')">Punk Rock</div>
                <div class="option-item" onclick="selectGenre('Garage Rock')">Garage Rock</div>
                <div class="option-item" onclick="selectGenre('Grunge')">Grunge</div>
                <div class="option-item" onclick="selectGenre('Post-Rock')">Post-Rock</div>
                <div class="option-item" onclick="selectGenre('Folk Rock')">Folk Rock</div>
                <div class="option-item" onclick="selectGenre('Southern Rock')">Southern Rock</div>
                <div class="option-item" onclick="selectGenre('Glam Rock')">Glam Rock</div>
                <div class="option-item" onclick="selectGenre('Arena Rock')">Arena Rock</div>
                <div class="option-item" onclick="selectGenre('Metal Rock')">Metal Rock</div>

                <!-- 🎤 Hip Hop / Rap -->
                <div class="option-group-title">🎤 Hip Hop / Rap</div>
                <div class="option-item" onclick="selectGenre('Hip Hop')">Hip Hop</div>
                <div class="option-item" onclick="selectGenre('Rap')">Rap</div>
                <div class="option-item" onclick="selectGenre('Old School Hip Hop')">Old School Hip Hop</div>
                <div class="option-item" onclick="selectGenre('Trap')">Trap</div>
                <div class="option-item" onclick="selectGenre('Boom Bap')">Boom Bap</div>
                <div class="option-item" onclick="selectGenre('Lo-Fi Hip Hop')">Lo-Fi Hip Hop</div>
                <div class="option-item" onclick="selectGenre('Gangsta Rap')">Gangsta Rap</div>
                <div class="option-item" onclick="selectGenre('Conscious Rap')">Conscious Rap</div>
                <div class="option-item" onclick="selectGenre('Melodic Rap')">Melodic Rap</div>
                <div class="option-item" onclick="selectGenre('Pop Rap')">Pop Rap</div>
                <div class="option-item" onclick="selectGenre('Alternative Hip Hop')">Alternative Hip Hop</div>
                <div class="option-item" onclick="selectGenre('R&B Rap')">R&B Rap</div>
                <div class="option-item" onclick="selectGenre('Drill')">Drill</div>
                <div class="option-item" onclick=
