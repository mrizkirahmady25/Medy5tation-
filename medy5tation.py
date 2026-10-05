import streamlit as st
import os
import base64

# -- KONFIGURASI TEMA & WARNA --
THEME = {
    "bg_color": "#0d1117",
    "main_text": "#ffffff",
    "accent_red": "#e0115f",
    "light_gray": "#b0b0b0",
    "card_bg": "#161b22",
    "card_border": "#30363d",
    "font_main": "Kanit",
    "font_accent": "Satisfy",
}

def get_image_base64(path):
    """Membaca file gambar lokal dan mengubahnya menjadi base64 agar tampil aman di Streamlit Cloud"""
    if os.path.exists(path):
        with open(path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode()
    return None

def set_page_styling():
    st.set_page_config(
        page_title="MEDY5TATION - Game Together",
        page_icon="🎮",
        layout="wide",
        initial_sidebar_state="collapsed",
    )
    # Import Bootstrap Icons CDN & Google Fonts
    st.markdown(f"""
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css">
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Kanit:wght@300;400;600;700&family=Satisfy&display=swap');

        .stApp {{
            background-color: {THEME['bg_color']};
            color: {THEME['main_text']};
            font-family: '{THEME['font_main']}', sans-serif;
        }}

        .brand-container {{
            text-align: center;
            padding: 5px 0;
        }}
        .brand-logo-img {{
            max-width: 220px;
            width: 100%;
            height: auto;
            border-radius: 12px;
            display: block;
            margin: 0 auto;
        }}
        .cursive-title {{
            font-family: '{THEME['font_accent']}', cursive;
            color: {THEME['accent_red']};
            font-size: 2.8rem;
            line-height: 1.1;
            margin: 0;
            text-align: left;
        }}
        .cursive-subtitle {{
            font-family: '{THEME['font_accent']}', cursive;
            color: {THEME['main_text']};
            font-size: 2.2rem;
            line-height: 1.1;
            margin: 0;
            text-align: right;
        }}
        .brand-subtitle {{
            font-size: 0.95rem;
            letter-spacing: 4px;
            color: {THEME['light_gray']};
            margin-top: 8px;
            margin-bottom: 20px;
        }}

        .card-box {{
            background-color: {THEME['card_bg']};
            border: 1px solid {THEME['card_border']};
            border-radius: 12px;
            padding: 16px;
            margin-bottom: 15px;
            height: 100%;
        }}
        .card-featured {{
            border: 1.5px solid {THEME['accent_red']};
        }}

        .price-badge {{
            color: {THEME['accent_red']};
            font-size: 2.3rem;
            font-weight: 800;
            line-height: 1;
        }}
        .service-title {{
            color: {THEME['accent_red']};
            font-size: 0.95rem;
            font-weight: 700;
            text-transform: uppercase;
            margin-top: 8px;
            margin-bottom: 8px;
        }}
        .game-list-header {{
            background: linear-gradient(90deg, #b80c44 0%, {THEME['accent_red']} 50%, #b80c44 100%);
            color: white;
            text-align: center;
            padding: 10px;
            border-radius: 8px;
            font-weight: 700;
            font-size: 1.2rem;
            letter-spacing: 1px;
            margin: 25px 0 15px 0;
        }}

        /* Social Media Button Styling */
        .social-link {{
            display: inline-flex;
            align-items: center;
            justify-content: center;
            gap: 8px;
            padding: 10px 16px;
            border-radius: 8px;
            font-weight: 600;
            text-decoration: none !important;
            font-size: 0.9rem;
            transition: opacity 0.2s, transform 0.2s;
            margin-bottom: 8px;
            width: 100%;
            text-align: center;
        }}
        .social-link:hover {{
            opacity: 0.9;
            transform: translateY(-2px);
        }}
        .btn-wa {{
            background-color: #25D366;
            color: white !important;
        }}
        .btn-shopee {{
            background-color: #EE4D2D;
            color: white !important;
        }}
        .btn-tiktok {{
            background-color: #000000;
            border: 1px solid #30363d;
            color: white !important;
        }}
        .btn-ig {{
            background: linear-gradient(45deg, #f09433 0%, #e6683c 25%, #dc2743 50%, #cc2366 75%, #bc1888 100%);
            color: white !important;
        }}
        .btn-yt {{
            background-color: #FF0000;
            color: white !important;
        }}
        </style>
    """, unsafe_allow_html=True)

# Data Game Sesuai Poster
PS4_GAMES = [
    "GOW 3", "GTA 5 MOD SUB INDO", "THE LAST OF US 1", "THE LAST OF US 2", "NARUTO CONNECTION",
    "DAYS GONE", "DEVIL MAY CRY 5", "A WAY OUT", "IT TAKES TWO", "SEKIRO",
    "RESIDENT EVIL 2", "GOD OF WAR 2018", "Hogwarts legacy", "Assasins creed syndicate", "Assasins creed valhala",
    "Resident evil 3", "Resident evil 7", "Resident evil 8", "Watch dog 2", "Resident evil 4",
    "Uncharted 4", "Uncharted lost legacy", "The Witcher", "Stray", "Fatal frame",
    "Kena", "Assasins creed unity", "Elden ring", "Gta SA definitif edition", "Sleeping dog",
    "Assasin creed mirage", "GTA 3 DEFINITIF EDITION", "GTA VICE CITY DEFINITIF EDITION", "Gow Ragnarok", "Assassin creed ezio collection",
    "assassin creed origins", "visage", "Assassin Black Flag", "Bayonetta", "Harvest moon AWL spesial",
    "Harvest moon sth", "Sifu", "Resident evil 5", "Assassin creed 3", "Lies of P",
    "assasins creed Oddyssey", "ghost of tsusima", "Basara 4 sumeragi", "dead island 2", "mafia 1",
    "mafia 2", "mafia 3", "Cyberpunk", "Resident evil 6", "Evil west",
    "Watchdog 1", "nier automata", "plague tale", "persona 3", "The calisto protocol",
    "Bloodborne", "Mortal kombat 11", "Stody of season", "Stars wars jedi survivor", "Tomb raider 1-3 remastered",
    "Gta 5 daeng nuansa Indonesia", "Uncharted nathan Drake", "Immortal hinyx", "Ghost recob", "Lego City Undercover",
    "Death Door", "One piece Oddyssey", "Yakuza 3", "Control"
]

PS4_HEN_UPDATES = ["Monster patch Winter 2026", "Eleven Patch Winter 2026 Final Update", "Daeng patch Summer 2026", "Bitbox patch WINTER 2026", "SGR Patch 2018 WINTER", "SGR Patch 2021 WINTER"]
PS3_BOLA_UPDATES = ["Bitbox patch", "Vr patch"]
ANDROID_SERVICES = ["Spotify mod premium", "Netflix (Nonton film gabungan vidio viu dkk)"]
SWITCH_GAMES = ["DREDGE", "STRAY"]

def main():
    set_page_styling()

    # -- HEADER UTAMA --
    col_h1, col_h2, col_h3 = st.columns([1.2, 3, 1.2])
    with col_h1:
        st.markdown('<p class="cursive-title">Good Games<br>Better Days</p>', unsafe_allow_html=True)
    with col_h2:
        # Menampilkan gambar logo jika ada di direktori
        logo_base64 = None
        for filename in ["logo.png", "logo.jpg", "logo.jpeg"]:
            if os.path.exists(filename):
                logo_base64 = get_image_base64(filename)
                break
        
        if logo_base64:
            st.markdown(f'''
                <div class="brand-container">
                    <img src="data:image/png;base64,{logo_base64}" class="brand-logo-img" alt="MEDY5TATION Logo">
                    <div class="brand-subtitle">PLAY MORE • GAME TOGETHER</div>
                </div>
            ''', unsafe_allow_html=True)
        else:
            st.markdown('''
                <div class="brand-container">
                    <i class="bi bi-controller" style="font-size: 3rem; color: #e0115f;"></i>
                    <h1 style="letter-spacing: 4px; margin: 0; font-size: 3rem;">MEDY5TATION</h1>
                    <div class="brand-subtitle">PLAY MORE • GAME TOGETHER</div>
                </div>
            ''', unsafe_allow_html=True)

    with col_h3:
        st.markdown('''
            <div style="text-align: right; color: #b0b0b0; font-size: 0.85rem; margin-bottom: 10px;">
                <b>PS4 &bull; PS3 &bull; SWITCH &bull; ANDROID</b>
            </div>
            <p class="cursive-subtitle">Game<br>Tanpa<br>Batas</p>
        ''', unsafe_allow_html=True)

    # -- 5 FITUR UTAMA --
    st.markdown('''
        <div style="display: flex; justify-content: space-around; text-align: center; margin-bottom: 25px; flex-wrap: wrap; gap: 10px;">
            <div><i class="bi bi-disc" style="font-size: 1.8rem; color: #e0115f;"></i><br><small style="color:#b0b0b0;">GAME ORIGINAL</small></div>
            <div><i class="bi bi-cloud-arrow-down" style="font-size: 1.8rem; color: #e0115f;"></i><br><small style="color:#b0b0b0;">PATCH SUB INDO</small></div>
            <div><i class="bi bi-device-hdd" style="font-size: 1.8rem; color: #e0115f;"></i><br><small style="color:#b0b0b0;">HDD FULL GAME</small></div>
            <div><i class="bi bi-gear-wide-connected" style="font-size: 1.8rem; color: #e0115f;"></i><br><small style="color:#b0b0b0;">INSTAL LANGSUNG</small></div>
            <div><i class="bi bi-shield-check" style="font-size: 1.8rem; color: #e0115f;"></i><br><small style="color:#b0b0b0;">AMAN & TERPERCAYA</small></div>
        </div>
    ''', unsafe_allow_html=True)

    # -- BARIS PAKET HARGA & LAYANAN --
    p1, p2, p3, p4, p5, p6 = st.columns([1.5, 2, 2, 1.8, 1.8, 2.2])

    with p1:
        st.markdown('''
            <div class="card-box card-featured" style="text-align: center;">
                <i class="bi bi-google-play" style="font-size: 1.8rem; color: white;"></i>
                <div class="service-title">VIA DRIVE</div>
                <div class="price-badge">15K</div>
                <small style="color: #b0b0b0;">PER GAME</small>
                <p style="font-size: 0.75rem; color: #8b949e; margin-top: 10px;">PATCH SUB INDO & LINK SESUAI CUSA GAME</p>
            </div>
        ''', unsafe_allow_html=True)

    with p2:
        st.markdown('''
            <div class="card-box card-featured" style="text-align: center;">
                <i class="bi bi-box-arrow-in-down" style="font-size: 1.8rem; color: white;"></i>
                <div class="service-title">PKG & INSTAL DI PS</div>
                <div class="price-badge">25K</div>
                <small style="color: #b0b0b0;">PER GAME</small>
                <div style="margin-top: 10px; background-color: #e0115f; padding: 4px; border-radius: 4px; font-weight: 600; font-size: 0.8rem;">
                    3 GAME 65K
                </div>
                <small style="color: #8b949e;">LOKASI PALEMBANG</small>
            </div>
        ''', unsafe_allow_html=True)

    with p3:
        st.markdown('''
            <div class="card-box card-featured" style="text-align: center;">
                <i class="bi bi-hdd-network" style="font-size: 1.8rem; color: white;"></i>
                <div class="service-title">HDD FULL GAME SUB INDO</div>
                <div style="display: flex; justify-content: space-around; margin-top: 8px;">
                    <div><span style="background:white; color:#0d1117; padding:2px 6px; border-radius:4px; font-size:0.75rem; font-weight:bold;">500GB</span><br><b style="color:#e0115f; font-size:1.2rem;">350RB</b></div>
                    <div><span style="background:white; color:#0d1117; padding:2px 6px; border-radius:4px; font-size:0.75rem; font-weight:bold;">1TB</span><br><b style="color:#e0115f; font-size:1.2rem;">550RB</b></div>
                </div>
            </div>
        ''', unsafe_allow_html=True)

    with p4:
        st.markdown('''
            <div class="card-box card-featured">
                <i class="bi bi-cpu" style="font-size: 1.6rem; color: white;"></i>
                <div class="service-title">JASA HEN PS4</div>
                <div class="price-badge" style="font-size: 1.8rem;">50K</div>
                <ul style="font-size: 0.75rem; padding-left: 16px; margin: 8px 0 0 0; color: #c9d1d9;">
                    <li>Install HEN</li>
                    <li>Setting & Tes Game</li>
                    <li>Panduan Pemakaian</li>
                </ul>
            </div>
        ''', unsafe_allow_html=True)

    with p5:
        st.markdown('''
            <div class="card-box card-featured">
                <i class="bi bi-thermometer-half" style="font-size: 1.6rem; color: white;"></i>
                <div class="service-title">GANTI PASTA</div>
                <div class="price-badge" style="font-size: 1.8rem;">250RB</div>
                <ul style="font-size: 0.75rem; padding-left: 16px; margin: 8px 0 0 0; color: #c9d1d9;">
                    <li>Bersihin debu</li>
                    <li>Pasta Thermal Premium</li>
                </ul>
            </div>
        ''', unsafe_allow_html=True)

    with p6:
        st.markdown('''
            <div class="card-box card-featured">
                <i class="bi bi-joystick" style="font-size: 1.6rem; color: white;"></i>
                <div class="service-title">SERVIS STIK PS4</div>
                <ul style="font-size: 0.75rem; padding-left: 16px; margin: 8px 0 0 0; color: #c9d1d9;">
                    <li>Analog drift</li>
                    <li>Tombol tidak respons</li>
                    <li>Ganti part / cleaning</li>
                    <li>Custom & upgrade</li>
                </ul>
            </div>
        ''', unsafe_allow_html=True)

    # -- LIST GAME --
    st.markdown('<div class="game-list-header"><i class="bi bi-card-checklist"></i> LIST GAME PATCH SUB INDONESIA (PS4)</div>', unsafe_allow_html=True)

    cols = st.columns(4)
    chunk = (len(PS4_GAMES) + 3) // 4
    for col_idx, col in enumerate(cols):
        with col:
            start_i = col_idx * chunk
            end_i = min(start_i + chunk, len(PS4_GAMES))
            for i in range(start_i, end_i):
                st.markdown(f'<div style="font-size: 0.8rem; padding: 2px 0; color: #e6edf3;"><span style="color:#e0115f; font-weight:bold;">{i+1}.</span> {PS4_GAMES[i]}</div>', unsafe_allow_html=True)

    # -- BARIS UPDATE KATEGORI LAIN --
    st.write("")
    u1, u2, u3, u4 = st.columns(4)

    with u1:
        st.markdown('<div class="card-box"><div class="service-title"><i class="bi bi-dribbble"></i> UPDATE BOLA PS4 HEN</div>', unsafe_allow_html=True)
        for i, up in enumerate(PS4_HEN_UPDATES):
            st.markdown(f'<div style="font-size: 0.75rem; color: #8b949e;">{i+1}. {up}</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with u2:
        st.markdown('<div class="card-box"><div class="service-title"><i class="bi bi-dribbble"></i> UPDATE BOLA PS3</div>', unsafe_allow_html=True)
        for i, up in enumerate(PS3_BOLA_UPDATES):
            st.markdown(f'<div style="font-size: 0.75rem; color: #8b949e;">{i+1}. {up}</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with u3:
        st.markdown('<div class="card-box"><div class="service-title"><i class="bi bi-android2"></i> ANDROID APPS</div>', unsafe_allow_html=True)
        for i, up in enumerate(ANDROID_SERVICES):
            st.markdown(f'<div style="font-size: 0.75rem; color: #8b949e;">{i+1}. {up}</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with u4:
        st.markdown('<div class="card-box"><div class="service-title"><i class="bi bi-nintendo-switch"></i> SWITCH SUB INDO</div>', unsafe_allow_html=True)
        for i, game in enumerate(SWITCH_GAMES):
            st.markdown(f'<div style="font-size: 0.75rem; color: #8b949e;">{i+1}. {game}</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # -- FOOTER & KONTAK LENGKAP --
    st.markdown('<hr style="border-color: #30363d; margin: 35px 0 25px 0;">', unsafe_allow_html=True)
    
    sec_lokasi, sec_order, sec_social = st.columns([1.5, 2, 2.5])

    with sec_lokasi:
        st.markdown('''
            <div style="margin-bottom: 8px;">
                <small style="color: #8b949e; letter-spacing: 1px;">LOKASI WORKSHOP</small>
                <div style="font-weight: 700; font-size: 1.2rem; color: white; margin-top: 4px;">
                    <i class="bi bi-geo-alt-fill" style="color: #e0115f;"></i> PALEMBANG
                </div>
                <div style="font-size: 0.85rem; color: #8b949e; margin-top: 2px;">
                    TEGAL BINANGUN SASANA PATRA
                </div>
            </div>
        ''', unsafe_allow_html=True)

    with sec_order:
        st.markdown('''
            <small style="color: #8b949e; letter-spacing: 1px;">ORDER & STORE</small><br>
            <div style="display: flex; flex-direction: column; gap: 8px; margin-top: 8px;">
                <a href="https://wa.me/6282289421650?text=" target="_blank" class="social-link btn-wa">
                    <i class="bi bi-whatsapp"></i> Chat WhatsApp
                </a>
                <a href="https://id.shp.ee/FdsB8oxh" target="_blank" class="social-link btn-shopee">
                    <i class="bi bi-bag-fill"></i> Shopee Store
                </a>
            </div>
        ''', unsafe_allow_html=True)

    with sec_social:
        st.markdown('''
            <small style="color: #8b949e; letter-spacing: 1px;">SOSIAL MEDIA</small><br>
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 8px; margin-top: 8px;">
                <a href="https://www.tiktok.com/@xtboy?_r=1&_t=ZS-9AIx1XJuxP8" target="_blank" class="social-link btn-tiktok">
                    <i class="bi bi-tiktok"></i> TikTok
                </a>
                <a href="https://www.instagram.com/m.rizkirahmady?stkn=ZGxoZjRxYWc4dWs2" target="_blank" class="social-link btn-ig">
                    <i class="bi bi-instagram"></i> Instagram
                </a>
            </div>
            <a href="https://youtube.com/@medy5tation?si=UhuJ79xJ212_mUGL" target="_blank" class="social-link btn-yt">
                <i class="bi bi-youtube"></i> YouTube Channel
            </a>
        ''', unsafe_allow_html=True)

    # Bottom PlayStation shapes footer
    st.markdown('''
        <div style="display: flex; justify-content: space-between; align-items: center; margin-top: 40px; padding: 15px 0; border-top: 1px solid #21262d; color: #8b949e; font-size: 0.8rem;">
            <div><b>MEDY5TATION</b></div>
            <div>&ldquo; GAME IS ALWAYS A GOOD IDEA &rdquo;</div>
            <div style="letter-spacing: 2px;">&#9651; &#9675; &#10005; &#9633; PLAY &bull; SHARE &bull; TOGETHER</div>
        </div>
    ''', unsafe_allow_html=True)

if __name__ == "__main__":
    main()