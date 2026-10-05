
import streamlit as st
import os
import base64

def get_image_base64(path):
    """Membaca file gambar lokal menjadi Base64"""
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
    # CDN Icons Bootstrap
    st.markdown('<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css">', unsafe_allow_html=True)
    
    # CSS: Background putih, wadah kartu gelap asli poster, khusus font menu tab berwarna biru tua
    custom_css = """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Kanit:wght@300;400;600;700;800&family=Satisfy&display=swap');

        /* Background Utama Putih */
        .stApp {
            background-color: #ffffff !important;
            color: #0f172a !important;
            font-family: 'Kanit', sans-serif !important;
        }

        /* Header */
        .brand-container {
            text-align: center;
            padding: 5px 0;
        }
        .brand-logo-img {
            max-width: 210px;
            width: 100%;
            height: auto;
            border-radius: 12px;
            display: block;
            margin: 0 auto;
        }
        .cursive-title {
            font-family: 'Satisfy', cursive !important;
            color: #e0115f !important;
            font-size: 2.8rem;
            line-height: 1.1;
            margin: 0;
            text-align: left;
        }
        .cursive-subtitle {
            font-family: 'Satisfy', cursive !important;
            color: #002d72 !important;
            font-size: 2.2rem;
            line-height: 1.1;
            margin: 0;
            text-align: right;
        }
        .brand-subtitle {
            font-size: 0.95rem;
            letter-spacing: 4px;
            color: #64748b;
            margin-top: 8px;
            margin-bottom: 20px;
            font-weight: 700;
        }

        /* Bar Fitur Atas Asli Gelap */
        .feature-bar {
            display: flex;
            justify-content: space-around;
            text-align: center;
            margin-bottom: 25px;
            flex-wrap: wrap;
            gap: 12px;
            background: #161b22;
            border: 1px solid #30363d;
            border-radius: 16px;
            padding: 14px 10px;
        }
        .feature-item {
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 4px;
            color: #c9d1d9;
        }

        /* KHUSUS MENU NAVIGASI: FONT DIUBAH BIRU TUA TEGAS */
        div[data-baseweb="tab-list"] {
            gap: 10px !important;
            justify-content: center !important;
            padding-bottom: 14px !important;
            border-bottom: 2px solid #e2e8f0 !important;
        }
        div[data-baseweb="tab"] {
            border-radius: 8px !important;
            padding: 9px 22px !important;
            background-color: #f1f5f9 !important;
            border: 1.5px solid #cbd5e1 !important;
            transition: all 0.2s ease-in-out !important;
        }
        div[data-baseweb="tab"] p, 
        div[data-baseweb="tab"] span {
            color: #002d72 !important; /* Biru Tua */
            font-weight: 800 !important;
            font-size: 0.95rem !important;
        }
        div[data-baseweb="tab"]:hover {
            background-color: #e2e8f0 !important;
            border-color: #002d72 !important;
        }
        div[data-baseweb="tab"][aria-selected="true"] {
            background-color: #002d72 !important;
            border-color: #002d72 !important;
        }
        div[data-baseweb="tab"][aria-selected="true"] p,
        div[data-baseweb="tab"][aria-selected="true"] span {
            color: #ffffff !important;
            font-weight: 800 !important;
        }
        div[data-baseweb="tab-highlight"] {
            background-color: transparent !important;
        }

        /* Kartu Konten (Kembali ke Gelap Asli Poster, Tidak Ada Layer Navy) */
        .card-box {
            border-radius: 12px;
            padding: 18px;
            margin-bottom: 15px;
            height: 100%;
            background-color: #161b22 !important;
            color: #ffffff !important;
            border: 1px solid #30363d;
            transition: transform 0.2s;
        }
        .card-box:hover {
            transform: translateY(-2px);
        }
        .card-featured {
            border: 1.5px solid #e0115f !important;
        }
        .price-badge {
            color: #e0115f !important;
            font-size: 2.4rem;
            font-weight: 800;
            line-height: 1;
        }
        .service-title {
            color: #e0115f !important;
            font-size: 0.95rem;
            font-weight: 700;
            text-transform: uppercase;
            margin-top: 8px;
            margin-bottom: 8px;
            letter-spacing: 0.5px;
        }

        /* Kotak List Game */
        .game-badge {
            background-color: #161b22 !important;
            border: 1px solid #30363d !important;
            border-radius: 8px;
            padding: 8px 12px;
            margin-bottom: 8px;
            font-size: 0.85rem;
            display: flex;
            align-items: center;
            gap: 8px;
        }
        .game-badge:hover {
            border-color: #e0115f !important;
            background-color: #21262d !important;
        }
        .game-num {
            color: #e0115f !important;
            font-weight: 800;
            font-size: 0.85rem;
            min-width: 28px;
        }

        /* Tombol Media Sosial */
        .social-link {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            gap: 8px;
            padding: 10px 16px;
            border-radius: 8px;
            font-weight: 600;
            text-decoration: none !important;
            font-size: 0.9rem;
            margin-bottom: 8px;
            width: 100%;
            text-align: center;
        }
        .btn-wa { background-color: #25D366; color: white !important; }
        .btn-shopee { background-color: #EE4D2D; color: white !important; }
        .btn-tiktok { background-color: #000000; border: 1px solid #30363d; color: white !important; }
        .btn-ig { background: linear-gradient(45deg, #f09433 0%, #e6683c 25%, #dc2743 50%, #cc2366 75%, #bc1888 100%); color: white !important; }
        .btn-yt { background-color: #FF0000; color: white !important; }
        </style>
    """
    st.markdown(custom_css, unsafe_allow_html=True)

# Data 82 Game Patch Sub Indonesia
PS4_GAMES = [
    "GOW 3", "GTA 5 MOD SUB INDO", "THE LAST OF US 1", "THE LAST OF US 2", "NARUTO CONNECTION",
    "DAYS GONE", "DEVIL MAY CRY 5", "A WAY OUT", "IT TAKES TWO", "SEKIRO",
    "RESIDENT EVIL 2", "GOD OF WAR 2018", "Hogwarts legacy", "Assasins creed syndicate", "Assasins creed valhala",
    "Resident evil 3", "Resident evil 7", "Resident evil 8", "Watch dog 2", "Resident evil 4",
    "Uncharted 4", "Uncharted lost legacy", "The Witcher", "Stray", "Fatal frame",
    "Kena", "Assasins creed unity", "Elden ring", "Gta SA definitif edition", "Sleeping dog",
    "Assasin creed mirage", "GTA 3 DEFINITIF EDITION", "GTA VICE CITY DEFINITIF EDITION", "Gow Ragnarok", "Assassin creed ezio collection",
    "assassin creed origins", "visage", "Assassin Black Flag", "Bayonetta", "Harvest moon AWL spesial",
    "Harvest moon sth", "Sifu", "Resident evil 5", "Assassin creed 3", "Lies op P",
    "assasins creed Oddysey", "ghost of tsusima", "Basara 4 sumeragi", "dead island 2", "mafia 1",
    "mafia 2", "mafia 3", "Cyberpunk", "Resident evil 6", "Evil west",
    "Watchdog 1", "nier automata", "plague tale", "persona 3", "The calisto protocol",
    "Bloodborne", "Mortal kombat 11", "Stody of season", "Stars wars jedi survivor", "Tomb raider 1-3 remastered",
    "Gta 5 daeng nuansa Indonesia", "Uncharted nathan Drake", "Immortal hinyx", "Ghost recob", "Lego City Undercover",
    "Death Door", "One piece Oddysey", "Yakuza 3", "Control", "Judghment",
    "Horizon zero down", "Spiderman", "Spiderman Miles morales", "detroit", "death stranding"
]

PS4_HEN_UPDATES = [
    "Monster patch summer 2027",
    "Eleven Patch summer 2027 Final Update",
    "Bitbox patch summer 2027",
    "Leader patch summer 2027",
    "monster 2018 patch summer 2027"
]

PS3_BOLA_UPDATES = [
    "Bitbox patch",
    "Vr patch"
]

ANDROID_SERVICES = [
    "Spotify mod premium",
    "Netflix (Nonton film gabungan vidio viu dkk)"
]

SWITCH_GAMES = [
    "DREDGE",
    "STRAY",
    "RDR",
    "Zelda BOTW"
]

def main():
    set_page_styling()

    # -- HEADER UTAMA --
    col_h1, col_h2, col_h3 = st.columns([1.2, 3, 1.2])
    with col_h1:
        st.markdown('<p class="cursive-title">Good Games<br>Better Days</p>', unsafe_allow_html=True)
    with col_h2:
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
                    <i class="bi bi-controller" style="font-size: 3.2rem; color: #e0115f;"></i>
                    <h1 style="letter-spacing: 4px; margin: 0; font-size: 3rem; color: #0f172a;">MEDY5TATION</h1>
                    <div class="brand-subtitle">PLAY MORE • GAME TOGETHER</div>
                </div>
            ''', unsafe_allow_html=True)

    with col_h3:
        st.markdown('''
            <div style="text-align: right; color: #002d72; font-size: 0.85rem; margin-bottom: 8px;">
                <b>PS4 &bull; PS3 &bull; SWITCH &bull; ANDROID</b>
            </div>
            <p class="cursive-subtitle">Game<br>Tanpa<br>Batas</p>
        ''', unsafe_allow_html=True)

    # -- 5 FITUR UTAMA --
    st.markdown('''
        <div class="feature-bar">
            <div class="feature-item"><i class="bi bi-disc" style="font-size: 1.6rem; color: #e0115f;"></i><small>GAME ORIGINAL</small></div>
            <div class="feature-item"><i class="bi bi-cloud-arrow-down" style="font-size: 1.6rem; color: #e0115f;"></i><small>PATCH SUB INDO</small></div>
            <div class="feature-item"><i class="bi bi-device-hdd" style="font-size: 1.6rem; color: #e0115f;"></i><small>HDD FULL GAME</small></div>
            <div class="feature-item"><i class="bi bi-gear-wide-connected" style="font-size: 1.6rem; color: #e0115f;"></i><small>INSTAL LANGSUNG</small></div>
            <div class="feature-item"><i class="bi bi-shield-check" style="font-size: 1.6rem; color: #e0115f;"></i><small>AMAN & TERPERCAYA</small></div>
        </div>
    ''', unsafe_allow_html=True)

    # -- NAVIGASI MENU (FONT BIRU TUA) --
    tab_beranda, tab_games, tab_bola, tab_extra = st.tabs([
        "🏠 Paket & Layanan",
        f"🎮 List Game Sub Indo ({len(PS4_GAMES)})",
        "⚽ Update Patch Bola",
        "📱 Android & Switch"
    ])

    # === TAB 1: PAKET & LAYANAN ===
    with tab_beranda:
        st.write("")
        p1, p2, p3 = st.columns([1.8, 2.2, 2.2])
        with p1:
            st.markdown('''
                <div class="card-box card-featured" style="text-align: center;">
                    <i class="bi bi-google-play" style="font-size: 2rem; color: white;"></i>
                    <div class="service-title">VIA DRIVE</div>
                    <div class="price-badge">15K</div>
                    <small style="color: #b0b0b0;">PER GAME</small>
                    <p style="font-size: 0.8rem; color: #8b949e; margin-top: 12px;">Patch Sub Indo & Link Download sesuai CUSA game</p>
                </div>
            ''', unsafe_allow_html=True)

        with p2:
            st.markdown('''
                <div class="card-box card-featured" style="text-align: center;">
                    <i class="bi bi-box-arrow-in-down" style="font-size: 2rem; color: white;"></i>
                    <div class="service-title">PKG & INSTAL DI PS</div>
                    <div class="price-badge">25K</div>
                    <small style="color: #b0b0b0;">PER GAME</small>
                    <div style="margin-top: 10px; background-color: #e0115f; padding: 5px; border-radius: 6px; font-weight: 700; font-size: 0.85rem; color: white;">
                        3 GAME 65K
                    </div>
                    <small style="color: #8b949e; display: block; margin-top: 6px;">Lokasi Palembang</small>
                </div>
            ''', unsafe_allow_html=True)

        with p3:
            st.markdown('''
                <div class="card-box card-featured" style="text-align: center;">
                    <i class="bi bi-hdd-network" style="font-size: 2rem; color: white;"></i>
                    <div class="service-title">HDD FULL GAME (PKG/PNP)</div>
                    <div style="display: flex; justify-content: space-around; margin-top: 10px;">
                        <div>
                            <span style="background:white; color:#0d1117; padding:3px 8px; border-radius:4px; font-size:0.75rem; font-weight:bold;">500GB</span>
                            <div style="color:#e0115f; font-size:1.6rem; font-weight:800; margin-top:4px;">350RB</div>
                        </div>
                        <div>
                            <span style="background:white; color:#0d1117; padding:3px 8px; border-radius:4px; font-size:0.75rem; font-weight:bold;">1TB</span>
                            <div style="color:#e0115f; font-size:1.6rem; font-weight:800; margin-top:4px;">550RB</div>
                        </div>
                    </div>
                    <small style="color: #8b949e; display: block; margin-top: 8px;">Plug and Play / Siap Main</small>
                </div>
            ''', unsafe_allow_html=True)

        st.write("")
        s1, s2, s3 = st.columns(3)
        with s1:
            st.markdown('''
                <div class="card-box card-featured">
                    <i class="bi bi-cpu" style="font-size: 1.8rem; color: white;"></i>
                    <div class="service-title">JASA HEN PS4</div>
                    <div class="price-badge">50K</div>
                    <ul style="font-size: 0.8rem; padding-left: 18px; margin: 10px 0 0 0; color: #c9d1d9; line-height: 1.6;">
                        <li>Install Sistem HEN</li>
                        <li>Setting & Tes Game Lengkap</li>
                        <li>Panduan Pemakaian Sampai Paham</li>
                    </ul>
                </div>
            ''', unsafe_allow_html=True)

        with s2:
            st.markdown('''
                <div class="card-box card-featured">
                    <i class="bi bi-thermometer-half" style="font-size: 1.8rem; color: white;"></i>
                    <div class="service-title">GANTI PASTA THERMAL</div>
                    <div class="price-badge">250RB</div>
                    <ul style="font-size: 0.8rem; padding-left: 18px; margin: 10px 0 0 0; color: #c9d1d9; line-height: 1.6;">
                        <li>Deep Cleaning / Pembersihan Debu Mesin</li>
                        <li>Aplikasi Thermal Paste Premium Berkualitas</li>
                        <li>Meredam Kipas Bising & Mengatasi Overheat</li>
                    </ul>
                </div>
            ''', unsafe_allow_html=True)

        with s3:
            st.markdown('''
                <div class="card-box card-featured">
                    <i class="bi bi-joystick" style="font-size: 1.8rem; color: white;"></i>
                    <div class="service-title">SERVIS STIK PS4</div>
                    <ul style="font-size: 0.8rem; padding-left: 18px; margin: 10px 0 0 0; color: #c9d1d9; line-height: 1.6;">
                        <li>Perbaikan Analog Drift / Tidak Stabil</li>
                        <li>Tombol Keras atau Tidak Responsif</li>
                        <li>Ganti Part / Jalur / Cleaning</li>
                        <li>Kustomisasi & Upgrade Mod</li>
                    </ul>
                </div>
            ''', unsafe_allow_html=True)

    # === TAB 2: KATALOG 82 GAME SUB INDO ===
    with tab_games:
        st.write("")
        search_query = st.text_input("🔍 Cari Judul Game Patch Bahasa Indonesia:", placeholder="Contoh: God of War, Spiderman, Resident Evil...")
        
        filtered_games = [g for g in PS4_GAMES if search_query.lower() in g.lower()] if search_query else PS4_GAMES

        if not filtered_games:
            st.info("Game yang dicari belum tersedia dalam daftar.")
        else:
            cols = st.columns(4)
            chunk = (len(filtered_games) + 3) // 4
            for col_idx, col in enumerate(cols):
                with col:
                    start_i = col_idx * chunk
                    end_i = min(start_i + chunk, len(filtered_games))
                    for i in range(start_i, end_i):
                        actual_idx = PS4_GAMES.index(filtered_games[i]) + 1
                        st.markdown(f'''
                            <div class="game-badge">
                                <span class="game-num">#{actual_idx}</span>
                                <span style="color:#ffffff; font-weight:500;">{filtered_games[i]}</span>
                            </div>
                        ''', unsafe_allow_html=True)

    # === TAB 3: UPDATE PATCH BOLA ===
    with tab_bola:
        st.write("")
        b1, b2 = st.columns(2)
        with b1:
            st.markdown('''
                <div class="card-box">
                    <div class="service-title" style="font-size: 1.1rem;">
                        <i class="bi bi-dribbble"></i> UPDATE BOLA PS4 HEN (SUMMER 2027)
                    </div>
            ''', unsafe_allow_html=True)
            for i, up in enumerate(PS4_HEN_UPDATES):
                st.markdown(f'''
                    <div style="background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.08); padding: 10px 14px; border-radius: 8px; margin-bottom: 8px; font-size: 0.88rem; color: #ffffff;">
                        <b style="color: #e0115f;">{i+1}.</b> {up}
                    </div>
                ''', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

        with b2:
            st.markdown('''
                <div class="card-box">
                    <div class="service-title" style="font-size: 1.1rem;">
                        <i class="bi bi-dribbble"></i> UPDATE BOLA PS3
                    </div>
            ''', unsafe_allow_html=True)
            for i, up in enumerate(PS3_BOLA_UPDATES):
                st.markdown(f'''
                    <div style="background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.08); padding: 10px 14px; border-radius: 8px; margin-bottom: 8px; font-size: 0.88rem; color: #ffffff;">
                        <b style="color: #00d2ff;">{i+1}.</b> {up}
                    </div>
                ''', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

    # === TAB 4: ANDROID & NINTENDO SWITCH ===
    with tab_extra:
        st.write("")
        ex1, ex2 = st.columns(2)
        with ex1:
            st.markdown('''
                <div class="card-box">
                    <div class="service-title" style="font-size: 1.1rem; color: #10b981;">
                        <i class="bi bi-android2"></i> ANDROID APPS & STREAMING
                    </div>
            ''', unsafe_allow_html=True)
            for i, up in enumerate(ANDROID_SERVICES):
                st.markdown(f'''
                    <div style="background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.08); padding: 10px 14px; border-radius: 8px; margin-bottom: 8px; font-size: 0.88rem; color: #ffffff;">
                        <b style="color: #10b981;">{i+1}.</b> {up}
                    </div>
                ''', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

        with ex2:
            st.markdown('''
                <div class="card-box">
                    <div class="service-title" style="font-size: 1.1rem;">
                        <i class="bi bi-nintendo-switch"></i> NINTENDO SWITCH SUB INDO
                    </div>
            ''', unsafe_allow_html=True)
            for i, game in enumerate(SWITCH_GAMES):
                st.markdown(f'''
                    <div style="background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.08); padding: 10px 14px; border-radius: 8px; margin-bottom: 8px; font-size: 0.88rem; color: #ffffff;">
                        <b style="color: #e0115f;">{i+1}.</b> {game}
                    </div>
                ''', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

    # -- FOOTER & KONTAK LENGKAP --
    st.markdown('<hr style="border-color: #e2e8f0; margin: 35px 0 25px 0;">', unsafe_allow_html=True)
    
    sec_lokasi, sec_order, sec_social = st.columns([1.5, 2, 2.5])

    with sec_lokasi:
        st.markdown('''
            <div style="margin-bottom: 8px;">
                <small style="color: #64748b; letter-spacing: 1px; font-weight:700;">LOKASI WORKSHOP</small>
                <div style="font-weight: 800; font-size: 1.25rem; color: #0f172a; margin-top: 4px;">
                    <i class="bi bi-geo-alt-fill" style="color: #e0115f;"></i> PALEMBANG
                </div>
                <div style="font-size: 0.88rem; color: #475569; margin-top: 2px;">
                    TEGAL BINANGUN SASANA PATRA
                </div>
            </div>
        ''', unsafe_allow_html=True)

    with sec_order:
        st.markdown('''
            <small style="color: #64748b; letter-spacing: 1px; font-weight:700;">ORDER & STORE</small><br>
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
            <small style="color: #64748b; letter-spacing: 1px; font-weight:700;">SOSIAL MEDIA</small><br>
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

    # Bottom Footer
    st.markdown('''
        <div style="display: flex; justify-content: space-between; align-items: center; margin-top: 40px; padding: 15px 0; border-top: 1px solid #e2e8f0; color: #64748b; font-size: 0.8rem; font-weight:600;">
            <div><b>MEDY5TATION</b></div>
            <div>&ldquo; GAME IS ALWAYS A GOOD IDEA &rdquo;</div>
            <div style="letter-spacing: 2px; color: #002d72;">&#9651; &#9675; &#10005; &#9633; PLAY &bull; SHARE &bull; TOGETHER</div>
        </div>
    ''', unsafe_allow_html=True)

if __name__ == "__main__":
    main()