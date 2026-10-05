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
    # CDN Icons
    st.markdown('<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css">', unsafe_allow_html=True)
    
    # Custom CSS: Latar luar putih, tabel/kotak berwarna Biru Tua gelap dengan font warna awal (terang)
    custom_css = """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Kanit:wght@300;400;600;700;800&family=Satisfy&display=swap');

        .stApp {
            background-color: #f8fafc !important;
            color: #0f172a !important;
            font-family: 'Kanit', sans-serif !important;
        }

        /* Header Branding */
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
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.12);
        }
        .cursive-title {
            font-family: 'Satisfy', cursive !important;
            color: #ff2a70 !important;
            font-size: 2.8rem;
            line-height: 1.1;
            margin: 0;
            text-align: left;
        }
        .cursive-subtitle {
            font-family: 'Satisfy', cursive !important;
            color: #00d2ff !important;
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

        /* Bar Fitur Atas - Tema Biru Tua dengan Teks Putih */
        .feature-bar {
            display: flex;
            justify-content: space-around;
            text-align: center;
            margin-bottom: 25px;
            flex-wrap: wrap;
            gap: 12px;
            background: #111827;
            border: 1px solid #1f2937;
            border-radius: 16px;
            padding: 14px 10px;
            box-shadow: 0 6px 18px rgba(0, 0, 0, 0.1);
        }
        .feature-item {
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 4px;
            color: #ffffff !important;
        }

        /* Kartu / Kotak Tabel: Latar Biru Tua Gelap, Teks Warna Asli (Putih & Terang) */
        .card-box {
            border-radius: 14px;
            padding: 18px;
            margin-bottom: 15px;
            height: 100%;
            background: #111827 !important;
            color: #ffffff !important;
            transition: transform 0.2s, box-shadow 0.2s;
        }
        .card-box:hover {
            transform: translateY(-3px);
        }
        
        .card-crimson {
            border: 1.5px solid #ff2a70 !important;
            box-shadow: 0 6px 20px rgba(255, 42, 112, 0.2);
        }
        .card-cyan {
            border: 1.5px solid #00d2ff !important;
            box-shadow: 0 6px 20px rgba(0, 210, 255, 0.2);
        }
        .card-purple {
            border: 1.5px solid #a855f7 !important;
            box-shadow: 0 6px 20px rgba(168, 85, 247, 0.2);
        }
        .card-amber {
            border: 1.5px solid #f59e0b !important;
            box-shadow: 0 6px 20px rgba(245, 158, 11, 0.2);
        }
        .card-emerald {
            border: 1.5px solid #10b981 !important;
            box-shadow: 0 6px 20px rgba(16, 185, 129, 0.2);
        }
        .card-pink {
            border: 1.5px solid #ec4899 !important;
            box-shadow: 0 6px 20px rgba(236, 72, 153, 0.2);
        }

        .price-badge-crimson { color: #ff2a70 !important; font-size: 2.3rem; font-weight: 800; line-height: 1; }
        .price-badge-cyan { color: #00d2ff !important; font-size: 2.3rem; font-weight: 800; line-height: 1; }
        .price-badge-amber { color: #f59e0b !important; font-size: 2.3rem; font-weight: 800; line-height: 1; }

        .service-title {
            font-size: 0.95rem;
            font-weight: 700;
            text-transform: uppercase;
            margin-top: 8px;
            margin-bottom: 8px;
            letter-spacing: 0.5px;
        }

        /* Kotak / Badge List Game - Latar Gelap & Teks Putih */
        .game-badge {
            background: #111827 !important;
            border: 1px solid #1f2937 !important;
            border-radius: 8px;
            padding: 8px 12px;
            margin-bottom: 8px;
            font-size: 0.85rem;
            display: flex;
            align-items: center;
            gap: 8px;
            transition: all 0.2s;
        }
        .game-badge:hover {
            border-color: #ff2a70 !important;
            background: #1f293d !important;
        }
        .game-num {
            color: #ff2a70 !important;
            font-weight: 800;
            font-size: 0.85rem;
            min-width: 28px;
        }

        /* Social Link Buttons */
        .social-link {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            gap: 8px;
            padding: 10px 16px;
            border-radius: 10px;
            font-weight: 600;
            text-decoration: none !important;
            font-size: 0.9rem;
            transition: opacity 0.2s, transform 0.2s;
            margin-bottom: 8px;
            width: 100%;
            text-align: center;
        }
        .social-link:hover {
            opacity: 0.92;
            transform: translateY(-2px);
        }
        .btn-wa { background: linear-gradient(135deg, #25D366, #128C7E); color: white !important; }
        .btn-shopee { background: linear-gradient(135deg, #EE4D2D, #ff5722); color: white !important; }
        .btn-tiktok { background: #000000; border: 1px solid #374151; color: white !important; }
        .btn-ig { background: linear-gradient(45deg, #f09433 0%, #e6683c 25%, #dc2743 50%, #cc2366 75%, #bc1888 100%); color: white !important; }
        .btn-yt { background: linear-gradient(135deg, #FF0000, #cc0000); color: white !important; }

        /* Custom Tabs Styling: Tab Biru Tua Modern */
        div[data-baseweb="tab-list"] {
            gap: 8px;
            justify-content: center;
            padding-bottom: 12px;
        }
        div[data-baseweb="tab"] {
            border-radius: 8px !important;
            padding: 8px 20px !important;
            font-weight: 700 !important;
            background-color: #111827 !important;
            color: #94a3b8 !important;
            border: 1px solid #1f2937 !important;
        }
        div[data-baseweb="tab"][aria-selected="true"] {
            background-color: #002d72 !important;
            color: #ffffff !important;
            border-color: #00d2ff !important;
            box-shadow: 0 4px 12px rgba(0, 45, 114, 0.3) !important;
        }
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
                    <i class="bi bi-controller" style="font-size: 3.2rem; color: #ff2a70;"></i>
                    <h1 style="letter-spacing: 4px; margin: 0; font-size: 3rem; color: #0f172a;">MEDY5TATION</h1>
                    <div class="brand-subtitle">PLAY MORE • GAME TOGETHER</div>
                </div>
            ''', unsafe_allow_html=True)

    with col_h3:
        st.markdown('''
            <div style="text-align: right; color: #64748b; font-size: 0.85rem; margin-bottom: 8px;">
                <b>PS4 &bull; PS3 &bull; SWITCH &bull; ANDROID</b>
            </div>
            <p class="cursive-subtitle">Game<br>Tanpa<br>Batas</p>
        ''', unsafe_allow_html=True)

    # -- BAR FITUR UTAMA (Latar Biru Tua, Teks Putih Terang) --
    st.markdown('''
        <div class="feature-bar">
            <div class="feature-item"><i class="bi bi-disc" style="font-size: 1.6rem; color: #ff2a70;"></i><small style="font-weight:700;">GAME ORIGINAL</small></div>
            <div class="feature-item"><i class="bi bi-cloud-arrow-down" style="font-size: 1.6rem; color: #00d2ff;"></i><small style="font-weight:700;">PATCH SUB INDO</small></div>
            <div class="feature-item"><i class="bi bi-device-hdd" style="font-size: 1.6rem; color: #a855f7;"></i><small style="font-weight:700;">HDD FULL GAME</small></div>
            <div class="feature-item"><i class="bi bi-gear-wide-connected" style="font-size: 1.6rem; color: #f59e0b;"></i><small style="font-weight:700;">INSTAL LANGSUNG</small></div>
            <div class="feature-item"><i class="bi bi-shield-check" style="font-size: 1.6rem; color: #10b981;"></i><small style="font-weight:700;">AMAN & TERPERCAYA</small></div>
        </div>
    ''', unsafe_allow_html=True)

    # -- NAVIGASI MENU / TABS --
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
                <div class="card-box card-cyan" style="text-align: center;">
                    <i class="bi bi-google-play" style="font-size: 2rem; color: #00d2ff;"></i>
                    <div class="service-title" style="color: #00d2ff;">VIA DRIVE</div>
                    <div class="price-badge-cyan">15K</div>
                    <small style="color: #94a3b8; font-weight:700;">PER GAME</small>
                    <p style="font-size: 0.82rem; color: #cbd5e1; margin-top: 14px;">Patch Sub Indo & Link Download sesuai CUSA game</p>
                </div>
            ''', unsafe_allow_html=True)

        with p2:
            st.markdown('''
                <div class="card-box card-crimson" style="text-align: center;">
                    <i class="bi bi-box-arrow-in-down" style="font-size: 2rem; color: #ff2a70;"></i>
                    <div class="service-title" style="color: #ff2a70;">PKG & INSTAL DI PS</div>
                    <div class="price-badge-crimson">25K</div>
                    <small style="color: #94a3b8; font-weight:700;">PER GAME</small>
                    <div style="margin-top: 10px; background: linear-gradient(90deg, #ff2a70, #be123c); padding: 5px; border-radius: 6px; font-weight: 700; font-size: 0.85rem; color: white;">
                        PROMO: 3 GAME 65K
                    </div>
                    <small style="color: #94a3b8; display: block; margin-top: 6px; font-weight:600;">Lokasi Palembang</small>
                </div>
            ''', unsafe_allow_html=True)

        with p3:
            st.markdown('''
                <div class="card-box card-purple" style="text-align: center;">
                    <i class="bi bi-hdd-network" style="font-size: 2rem; color: #a855f7;"></i>
                    <div class="service-title" style="color: #a855f7;">HDD FULL GAME (PKG/PNP)</div>
                    <div style="display: flex; justify-content: space-around; margin-top: 12px;">
                        <div>
                            <span style="background:white; color:#111827; padding:3px 8px; border-radius:4px; font-size:0.75rem; font-weight:800;">500GB</span>
                            <div style="color:#a855f7; font-size:1.6rem; font-weight:800; margin-top:4px;">350RB</div>
                        </div>
                        <div>
                            <span style="background:white; color:#111827; padding:3px 8px; border-radius:4px; font-size:0.75rem; font-weight:800;">1TB</span>
                            <div style="color:#a855f7; font-size:1.6rem; font-weight:800; margin-top:4px;">550RB</div>
                        </div>
                    </div>
                    <small style="color: #94a3b8; display: block; margin-top: 8px; font-weight:600;">Plug and Play / Siap Main</small>
                </div>
            ''', unsafe_allow_html=True)

        st.write("")
        s1, s2, s3 = st.columns(3)
        with s1:
            st.markdown('''
                <div class="card-box card-amber">
                    <div style="display: flex; align-items: center; gap: 10px;">
                        <i class="bi bi-cpu" style="font-size: 1.8rem; color: #f59e0b;"></i>
                        <div>
                            <div class="service-title" style="color: #f59e0b; margin: 0;">JASA HEN PS4</div>
                            <div class="price-badge-amber">50K</div>
                        </div>
                    </div>
                    <ul style="font-size: 0.82rem; padding-left: 18px; margin: 12px 0 0 0; color: #cbd5e1; line-height: 1.6;">
                        <li>Install Sistem HEN</li>
                        <li>Setting & Tes Game Lengkap</li>
                        <li>Panduan Pemakaian Sampai Paham</li>
                    </ul>
                </div>
            ''', unsafe_allow_html=True)

        with s2:
            st.markdown('''
                <div class="card-box card-emerald">
                    <div style="display: flex; align-items: center; gap: 10px;">
                        <i class="bi bi-thermometer-half" style="font-size: 1.8rem; color: #10b981;"></i>
                        <div>
                            <div class="service-title" style="color: #10b981; margin: 0;">GANTI PASTA THERMAL</div>
                            <div style="color: #10b981; font-size: 2.3rem; font-weight: 800; line-height: 1;">250RB</div>
                        </div>
                    </div>
                    <ul style="font-size: 0.82rem; padding-left: 18px; margin: 12px 0 0 0; color: #cbd5e1; line-height: 1.6;">
                        <li>Deep Cleaning / Pembersihan Debu Mesin</li>
                        <li>Aplikasi Thermal Paste Premium Berkualitas</li>
                        <li>Meredam Kipas Bising & Mengatasi Overheat</li>
                    </ul>
                </div>
            ''', unsafe_allow_html=True)

        with s3:
            st.markdown('''
                <div class="card-box card-pink">
                    <div style="display: flex; align-items: center; gap: 10px;">
                        <i class="bi bi-joystick" style="font-size: 1.8rem; color: #ec4899;"></i>
                        <div>
                            <div class="service-title" style="color: #ec4899; margin: 0;">SERVIS STIK PS4</div>
                            <small style="color: #94a3b8; font-weight: 700;">Diagnosa Cepat & Rapi</small>
                        </div>
                    </div>
                    <ul style="font-size: 0.82rem; padding-left: 18px; margin: 12px 0 0 0; color: #cbd5e1; line-height: 1.6;">
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
                                <span style="color:#ffffff; font-weight:600;">{filtered_games[i]}</span>
                            </div>
                        ''', unsafe_allow_html=True)

    # === TAB 3: UPDATE PATCH BOLA ===
    with tab_bola:
        st.write("")
        b1, b2 = st.columns(2)
        with b1:
            st.markdown('''
                <div class="card-box card-crimson">
                    <div class="service-title" style="color: #ff2a70; font-size: 1.1rem;">
                        <i class="bi bi-dribbble"></i> UPDATE BOLA PS4 HEN (SUMMER 2027)
                    </div>
            ''', unsafe_allow_html=True)
            for i, up in enumerate(PS4_HEN_UPDATES):
                st.markdown(f'''
                    <div style="background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.1); padding: 10px 14px; border-radius: 8px; margin-bottom: 8px; font-size: 0.88rem; color: #ffffff;">
                        <b style="color: #ff2a70;">{i+1}.</b> {up}
                    </div>
                ''', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

        with b2:
            st.markdown('''
                <div class="card-box card-cyan">
                    <div class="service-title" style="color: #00d2ff; font-size: 1.1rem;">
                        <i class="bi bi-dribbble"></i> UPDATE BOLA PS3
                    </div>
            ''', unsafe_allow_html=True)
            for i, up in enumerate(PS3_BOLA_UPDATES):
                st.markdown(f'''
                    <div style="background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.1); padding: 10px 14px; border-radius: 8px; margin-bottom: 8px; font-size: 0.88rem; color: #ffffff;">
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
                <div class="card-box card-emerald">
                    <div class="service-title" style="color: #10b981; font-size: 1.1rem;">
                        <i class="bi bi-android2"></i> ANDROID APPS & STREAMING
                    </div>
            ''', unsafe_allow_html=True)
            for i, up in enumerate(ANDROID_SERVICES):
                st.markdown(f'''
                    <div style="background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.1); padding: 10px 14px; border-radius: 8px; margin-bottom: 8px; font-size: 0.88rem; color: #ffffff;">
                        <b style="color: #10b981;">{i+1}.</b> {up}
                    </div>
                ''', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

        with ex2:
            st.markdown('''
                <div class="card-box" style="border: 1.5px solid #ef4444; box-shadow: 0 6px 20px rgba(239, 68, 68, 0.2);">
                    <div class="service-title" style="color: #ef4444; font-size: 1.1rem;">
                        <i class="bi bi-nintendo-switch"></i> NINTENDO SWITCH SUB INDO
                    </div>
            ''', unsafe_allow_html=True)
            for i, game in enumerate(SWITCH_GAMES):
                st.markdown(f'''
                    <div style="background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.1); padding: 10px 14px; border-radius: 8px; margin-bottom: 8px; font-size: 0.88rem; color: #ffffff;">
                        <b style="color: #ef4444;">{i+1}.</b> {game}
                    </div>
                ''', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

    # -- FOOTER & KONTAK LENGKAP --
    st.markdown('<hr style="border-color: #cbd5e1; margin: 35px 0 25px 0;">', unsafe_allow_html=True)
    
    sec_lokasi, sec_order, sec_social = st.columns([1.5, 2, 2.5])

    with sec_lokasi:
        st.markdown('''
            <div style="margin-bottom: 8px;">
                <small style="color: #0f172a; letter-spacing: 1px; font-weight:800;">LOKASI WORKSHOP</small>
                <div style="font-weight: 800; font-size: 1.25rem; color: #0f172a; margin-top: 4px;">
                    <i class="bi bi-geo-alt-fill" style="color: #ff2a70;"></i> PALEMBANG
                </div>
                <div style="font-size: 0.88rem; color: #475569; margin-top: 2px; font-weight:600;">
                    TEGAL BINANGUN SASANA PATRA
                </div>
            </div>
        ''', unsafe_allow_html=True)

    with sec_order:
        st.markdown('''
            <small style="color: #0f172a; letter-spacing: 1px; font-weight:800;">ORDER & STORE</small><br>
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
            <small style="color: #0f172a; letter-spacing: 1px; font-weight:800;">SOSIAL MEDIA</small><br>
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
        <div style="display: flex; justify-content: space-between; align-items: center; margin-top: 40px; padding: 15px 0; border-top: 2px solid #cbd5e1; color: #475569; font-size: 0.8rem; font-weight:700;">
            <div><b>MEDY5TATION</b></div>
            <div>&ldquo; GAME IS ALWAYS A GOOD IDEA &rdquo;</div>
            <div style="letter-spacing: 2px; color: #ff2a70;">&#9651; &#9675; &#10005; &#9633; PLAY &bull; SHARE &bull; TOGETHER</div>
        </div>
    ''', unsafe_allow_html=True)

if __name__ == "__main__":
    main()