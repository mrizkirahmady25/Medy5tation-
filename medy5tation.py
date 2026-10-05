import streamlit as st
import os
import base64
import urllib.parse

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

    # CSS: Background putih, box konten berwarna-warni (pastel/gradient) dengan teks GELAP agar tetap kontras & terbaca
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

        /* Promo Banner - gradient berwarna, teks gelap */
        .promo-banner {
            background: linear-gradient(90deg, #fef3c7, #fde68a, #fef3c7);
            border: 1.5px solid #f59e0b;
            border-radius: 14px;
            padding: 12px 18px;
            text-align: center;
            font-weight: 700;
            color: #78350f !important;
            margin-bottom: 18px;
            font-size: 0.95rem;
        }

        /* Bar Fitur Atas - gradient Navy ke Ungu, teks putih (background tetap gelap jadi kontras aman) */
        .feature-bar {
            display: flex;
            justify-content: space-around;
            text-align: center;
            margin-bottom: 25px;
            flex-wrap: wrap;
            gap: 12px;
            background: linear-gradient(120deg, #001f3f, #1e1b4b 60%, #3b0764) !important;
            border: 1.5px solid #1e3a8a !important;
            border-radius: 16px;
            padding: 14px 10px;
            box-shadow: 0 4px 12px rgba(0, 31, 63, 0.2);
        }
        .feature-item {
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 4px;
            color: #f1f5f9;
            font-weight: 600;
        }

        /* Dashboard statistik - 4 kartu warna beda */
        div[data-testid="stMetric"] {
            background: linear-gradient(135deg, #e0f2fe, #bae6fd);
            border: 1.5px solid #38bdf8;
            border-radius: 14px;
            padding: 14px 10px;
            box-shadow: 0 4px 10px rgba(56,189,248,0.15);
        }
        div[data-testid="stMetric"] label, div[data-testid="stMetric"] div {
            color: #0c4a6e !important;
        }

        /* TAB NAVIGATION */
        [data-testid="stTabs"] div[data-baseweb="tab-list"] {
            gap: 10px !important;
            justify-content: center !important;
            padding-bottom: 14px !important;
            border-bottom: 2px solid #e2e8f0 !important;
            flex-wrap: wrap;
        }
        [data-testid="stTabs"] div[data-baseweb="tab"] {
            border-radius: 8px !important;
            padding: 10px 20px !important;
            background-color: #002244 !important;
            border: 1.5px solid #1e3a8a !important;
            transition: all 0.2s ease-in-out !important;
        }
        [data-testid="stTabs"] div[data-baseweb="tab"] p,
        [data-testid="stTabs"] div[data-baseweb="tab"] span {
            color: #ffffff !important;
            font-weight: 700 !important;
            font-size: 0.9rem !important;
        }
        [data-testid="stTabs"] div[data-baseweb="tab"]:hover {
            background-color: #003366 !important;
            border-color: #38bdf8 !important;
            transform: translateY(-2px);
        }
        [data-testid="stTabs"] div[data-baseweb="tab"][aria-selected="true"] {
            background: linear-gradient(120deg, #e0115f, #be123c) !important;
            border-color: #e0115f !important;
        }
        [data-testid="stTabs"] div[data-baseweb="tab-highlight"] {
            background-color: transparent !important;
        }

        /* ===== KARTU KONTEN WARNA-WARNI (pastel/gradient), TEKS GELAP ===== */
        .card-box {
            border-radius: 12px;
            padding: 20px;
            margin-bottom: 15px;
            height: 100%;
            color: #0f172a !important;
            box-shadow: 0 6px 16px rgba(15, 23, 42, 0.1);
            transition: transform 0.2s, box-shadow 0.2s;
        }
        .card-box:hover {
            transform: translateY(-3px);
            box-shadow: 0 10px 22px rgba(15, 23, 42, 0.18);
        }
        .card-blue {
            background: linear-gradient(135deg, #e0f2fe, #bae6fd);
            border: 1.5px solid #38bdf8 !important;
        }
        .card-purple {
            background: linear-gradient(135deg, #ede9fe, #ddd6fe);
            border: 1.5px solid #a78bfa !important;
        }
        .card-pink {
            background: linear-gradient(135deg, #fce7f3, #fbcfe8);
            border: 1.5px solid #f472b6 !important;
        }
        .card-teal {
            background: linear-gradient(135deg, #ccfbf1, #99f6e4);
            border: 1.5px solid #2dd4bf !important;
        }
        .card-orange {
            background: linear-gradient(135deg, #ffedd5, #fed7aa);
            border: 1.5px solid #fb923c !important;
        }
        .card-green {
            background: linear-gradient(135deg, #dcfce7, #bbf7d0);
            border: 1.5px solid #4ade80 !important;
        }
        .card-featured {
            border-width: 2px !important;
        }
        .price-badge {
            color: #be123c !important;
            font-size: 2.2rem;
            font-weight: 800;
            line-height: 1;
        }
        .service-title {
            font-size: 1rem;
            font-weight: 800;
            text-transform: uppercase;
            margin-top: 8px;
            margin-bottom: 8px;
            letter-spacing: 0.5px;
            color: #0f172a !important;
        }
        .card-box small, .card-box p, .card-box ul, .card-box li, .card-box div {
            color: #1e293b !important;
        }

        /* List Items di dalam Box (Patch Bola dsb) - terang + teks gelap */
        .list-item-box {
            background: rgba(255, 255, 255, 0.55);
            border: 1px solid rgba(15, 23, 42, 0.12);
            padding: 10px 14px;
            border-radius: 8px;
            margin-bottom: 8px;
            font-size: 0.9rem;
            color: #0f172a !important;
            font-weight: 500;
        }

        /* KOTAK LIST GAME - warna gantian per baris, teks gelap */
        .game-badge {
            border-radius: 8px;
            padding: 9px 12px;
            margin-bottom: 8px;
            font-size: 0.85rem;
            display: flex;
            align-items: center;
            gap: 8px;
            transition: all 0.15s ease-in-out;
            color: #0f172a !important;
            font-weight: 600;
        }
        .game-badge:hover {
            transform: scale(1.02);
            filter: brightness(0.97);
        }
        .game-num {
            color: #be123c !important;
            font-weight: 800;
            font-size: 0.85rem;
            min-width: 28px;
        }

        /* FAQ Expander */
        [data-testid="stExpander"] {
            border: 1.5px solid #cbd5e1 !important;
            border-radius: 10px !important;
            margin-bottom: 8px;
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

        /* Badge kecil serba guna */
        .mini-badge {
            display: inline-block;
            padding: 4px 10px;
            border-radius: 20px;
            font-size: 0.72rem;
            font-weight: 700;
            margin: 2px;
        }
        .badge-new { background:#fde68a; color:#78350f !important; }
        .badge-hot { background:#fecaca; color:#7f1d1d !important; }
        .badge-info { background:#bae6fd; color:#0c4a6e !important; }
        </style>
    """
    st.markdown(custom_css, unsafe_allow_html=True)


# Rotasi warna kartu agar tampilan lebih variatif
CARD_COLORS = ["card-blue", "card-purple", "card-pink", "card-teal", "card-orange", "card-green"]

def card_color(i):
    return CARD_COLORS[i % len(CARD_COLORS)]

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

# Daftar layanan untuk kalkulator estimasi harga
# format: (nama tampilan, harga satuan, satuan label, maksimal qty wajar untuk slider)
SERVICES_PRICE = {
    "Via Drive (per game)": 15000,
    "PKG & Instal di PS (per game)": 25000,
    "HDD Full Game 500GB": 350000,
    "HDD Full Game 1TB": 550000,
    "Jasa HEN PS4": 50000,
    "Ganti Pasta Thermal": 250000,
}

FAQ_LIST = [
    ("Apakah data/save game saya aman saat proses instalasi?",
     "Aman. Proses instalasi dan patch dilakukan tanpa menghapus data save game yang sudah ada, kecuali ada permintaan reset khusus dari pelanggan."),
    ("Berapa lama proses pengerjaan untuk instalasi di tempat?",
     "Untuk instal beberapa game biasanya selesai dalam hitungan menit hingga 1 jam tergantung jumlah dan ukuran game yang dipilih."),
    ("Apakah PS4 tetap bisa dipakai untuk main online (PSN)?",
     "Tergantung jenis layanan dan versi firmware konsol. Silakan konsultasikan dulu via WhatsApp agar bisa disesuaikan dengan kebutuhan Anda."),
    ("Apakah bisa request judul game yang belum ada di daftar?",
     "Bisa. Silakan chat admin untuk cek ketersediaan patch bahasa Indonesia atau game yang diminta."),
    ("Apakah layanan HDD Full Game bisa langsung dipakai tanpa instal ulang?",
     "Ya, HDD Full Game bersifat Plug and Play sehingga tinggal dicolok dan langsung bisa dimainkan."),
]

TESTIMONI_CONTOH = [
    ("Pelanggan A", "⭐⭐⭐⭐⭐", "Prosesnya cepat dan game banyak pilihan patch sub indo, recommended!"),
    ("Pelanggan B", "⭐⭐⭐⭐⭐", "HDD 1TB isinya lengkap, PS4 jadi berasa baru lagi setelah ganti pasta."),
    ("Pelanggan C", "⭐⭐⭐⭐", "Pelayanan ramah, dibantu sampai paham cara pakainya."),
]


def render_card(col, color_class, icon, title, price_html, bullets, featured=False):
    featured_class = "card-featured" if featured else ""
    bullets_html = "".join([f"<li>{b}</li>" for b in bullets])
    col.markdown(f'''
        <div class="card-box {color_class} {featured_class}">
            <i class="bi {icon}" style="font-size: 1.8rem;"></i>
            <div class="service-title">{title}</div>
            {price_html}
            <ul style="font-size: 0.82rem; padding-left: 18px; margin: 10px 0 0 0; line-height: 1.6;">
                {bullets_html}
            </ul>
        </div>
    ''', unsafe_allow_html=True)


def main():
    set_page_styling()

    if "favorit_games" not in st.session_state:
        st.session_state.favorit_games = []

    # -- PROMO BANNER --
    st.markdown('''
        <div class="promo-banner">
            🔥 PROMO BULAN INI: Paket 3 Game PKG & Instal hanya <b>65K</b> • Gratis konsultasi pemilihan game sebelum order! 🔥
        </div>
    ''', unsafe_allow_html=True)

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
                    <i class="bi bi-controller" style="font-size: 3.2rem; color: #002244;"></i>
                    <h1 style="letter-spacing: 4px; margin: 0; font-size: 3rem; color: #001f3f;">MEDY5TATION</h1>
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
            <div class="feature-item"><i class="bi bi-disc" style="font-size: 1.6rem; color: #38bdf8;"></i><small>GAME ORIGINAL</small></div>
            <div class="feature-item"><i class="bi bi-cloud-arrow-down" style="font-size: 1.6rem; color: #a78bfa;"></i><small>PATCH SUB INDO</small></div>
            <div class="feature-item"><i class="bi bi-device-hdd" style="font-size: 1.6rem; color: #f472b6;"></i><small>HDD FULL GAME</small></div>
            <div class="feature-item"><i class="bi bi-gear-wide-connected" style="font-size: 1.6rem; color: #2dd4bf;"></i><small>INSTAL LANGSUNG</small></div>
            <div class="feature-item"><i class="bi bi-shield-check" style="font-size: 1.6rem; color: #fb923c;"></i><small>AMAN & TERPERCAYA</small></div>
        </div>
    ''', unsafe_allow_html=True)

    # -- DASHBOARD STATISTIK SINGKAT --
    st.caption("Ganti angka-angka berikut dengan data asli sesuai riwayat toko Anda.")
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("🎮 Total Game Patch", f"{len(PS4_GAMES)}+")
    m2.metric("⚽ Update Patch Bola", f"{len(PS4_HEN_UPDATES) + len(PS3_BOLA_UPDATES)}")
    m3.metric("⭐ Game Favoritmu", f"{len(st.session_state.favorit_games)}")
    m4.metric("📍 Lokasi Workshop", "Palembang")

    st.write("")

    # -- NAVIGASI MENU --
    tab_beranda, tab_games, tab_bola, tab_extra, tab_kalkulator, tab_info = st.tabs([
        "🏠 Paket & Layanan",
        f"🎮 List Game Sub Indo ({len(PS4_GAMES)})",
        "⚽ Update Patch Bola",
        "📱 Android & Switch",
        "💰 Estimasi Harga & Order",
        "💬 Testimoni & FAQ",
    ])

    # === TAB 1: PAKET & LAYANAN ===
    with tab_beranda:
        st.write("")
        p1, p2, p3 = st.columns([1.8, 2.2, 2.2])
        with p1:
            st.markdown('''
                <div class="card-box card-blue card-featured" style="text-align: center;">
                    <i class="bi bi-google-play" style="font-size: 2rem; color:#0369a1;"></i>
                    <div class="service-title">VIA DRIVE</div>
                    <div class="price-badge">15K</div>
                    <small>PER GAME</small>
                    <p style="font-size: 0.82rem; margin-top: 12px;">Patch Sub Indo & Link Download sesuai CUSA game</p>
                </div>
            ''', unsafe_allow_html=True)

        with p2:
            st.markdown('''
                <div class="card-box card-purple card-featured" style="text-align: center;">
                    <i class="bi bi-box-arrow-in-down" style="font-size: 2rem; color:#6d28d9;"></i>
                    <div class="service-title">PKG & INSTAL DI PS</div>
                    <div class="price-badge">25K</div>
                    <small>PER GAME</small>
                    <div style="margin-top: 10px; background: linear-gradient(90deg,#e0115f,#be123c); padding: 6px; border-radius: 6px; font-weight: 700; font-size: 0.85rem; color: white !important;">
                        3 GAME 65K
                    </div>
                    <small style="display: block; margin-top: 8px;">Lokasi Palembang</small>
                </div>
            ''', unsafe_allow_html=True)

        with p3:
            st.markdown('''
                <div class="card-box card-teal card-featured" style="text-align: center;">
                    <i class="bi bi-hdd-network" style="font-size: 2rem; color:#0f766e;"></i>
                    <div class="service-title">HDD FULL GAME (PKG/PNP)</div>
                    <div style="display: flex; justify-content: space-around; margin-top: 10px;">
                        <div>
                            <span style="background:#0f172a; color:white; padding:3px 8px; border-radius:4px; font-size:0.75rem; font-weight:bold;">500GB</span>
                            <div style="color:#be123c; font-size:1.5rem; font-weight:800; margin-top:4px;">350RB</div>
                        </div>
                        <div>
                            <span style="background:#0f172a; color:white; padding:3px 8px; border-radius:4px; font-size:0.75rem; font-weight:bold;">1TB</span>
                            <div style="color:#be123c; font-size:1.5rem; font-weight:800; margin-top:4px;">550RB</div>
                        </div>
                    </div>
                    <small style="display: block; margin-top: 10px;">Plug and Play / Siap Main</small>
                </div>
            ''', unsafe_allow_html=True)

        st.write("")
        s1, s2, s3 = st.columns(3)
        render_card(s1, "card-orange", "bi-cpu", "JASA HEN PS4", '<div class="price-badge">50K</div>', [
            "Install Sistem HEN",
            "Setting & Tes Game Lengkap",
            "Panduan Pemakaian Sampai Paham",
        ])
        render_card(s2, "card-pink", "bi-thermometer-half", "GANTI PASTA THERMAL", '<div class="price-badge">250RB</div>', [
            "Deep Cleaning / Pembersihan Debu Mesin",
            "Aplikasi Thermal Paste Premium Berkualitas",
            "Meredam Kipas Bising & Mengatasi Overheat",
        ])
        render_card(s3, "card-green", "bi-joystick", "SERVIS STIK PS4", '<div class="price-badge" style="font-size: 1.4rem;">KONSULTASI</div>', [
            "Perbaikan Analog Drift / Tidak Stabil",
            "Tombol Keras atau Tidak Responsif",
            "Ganti Part / Jalur / Cleaning",
            "Kustomisasi & Upgrade Mod",
        ])

        st.write("")
        st.markdown('''
            <div class="card-box card-blue" style="text-align:center;">
                <span class="mini-badge badge-new">BARU</span>
                <span class="mini-badge badge-hot">PALING LARIS</span>
                <span class="mini-badge badge-info">GARANSI ULANG INSTAL</span>
                &nbsp; Semua layanan instalasi mendapat garansi ulang pasang gratis bila terjadi kendala teknis dari pihak kami.
            </div>
        ''', unsafe_allow_html=True)

    # === TAB 2: KATALOG GAME SUB INDO ===
    with tab_games:
        st.write("")
        fc1, fc2 = st.columns([2.5, 1.5])
        with fc1:
            search_query = st.text_input("🔍 Cari Judul Game Patch Bahasa Indonesia:", placeholder="Contoh: God of War, Spiderman, Resident Evil...")
        with fc2:
            urutkan = st.selectbox("Urutkan", ["Default", "A - Z", "Z - A"])

        filtered_games = [g for g in PS4_GAMES if search_query.lower() in g.lower()] if search_query else list(PS4_GAMES)

        if urutkan == "A - Z":
            filtered_games = sorted(filtered_games, key=str.lower)
        elif urutkan == "Z - A":
            filtered_games = sorted(filtered_games, key=str.lower, reverse=True)

        st.caption(f"Menampilkan {len(filtered_games)} dari {len(PS4_GAMES)} game.")

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
                        game_name = filtered_games[i]
                        actual_idx = PS4_GAMES.index(game_name) + 1
                        color_hex = ["#bae6fd", "#ddd6fe", "#fbcfe8", "#99f6e4", "#fed7aa", "#bbf7d0"][actual_idx % 6]
                        st.markdown(f'''
                            <div class="game-badge" style="background-color:{color_hex};">
                                <span class="game-num">#{actual_idx}</span>
                                <span>{game_name}</span>
                            </div>
                        ''', unsafe_allow_html=True)

        st.write("")
        st.markdown("##### ⭐ Pilih Game Favorit (untuk disertakan saat order)")
        pilihan_favorit = st.multiselect(
            "Cari dan tandai game yang kamu incar:",
            options=PS4_GAMES,
            default=st.session_state.favorit_games,
        )
        st.session_state.favorit_games = pilihan_favorit
        if pilihan_favorit:
            st.success(f"Kamu menandai {len(pilihan_favorit)} game favorit. Lihat tab 💰 Estimasi Harga & Order untuk langsung order.")

    # === TAB 3: UPDATE PATCH BOLA ===
    with tab_bola:
        st.write("")
        b1, b2 = st.columns(2)
        with b1:
            items_html = "".join([
                f'''<div class="list-item-box">
                    <b style="color:#0f766e;">{i+1}.</b> {up}
                </div>''' for i, up in enumerate(PS4_HEN_UPDATES)
            ])
            st.markdown(f'''
                <div class="card-box card-teal">
                    <div class="service-title" style="font-size: 1.1rem; margin-bottom: 15px;">
                        <i class="bi bi-dribbble"></i> UPDATE BOLA PS4 HEN (SUMMER 2027)
                    </div>
                    {items_html}
                </div>
            ''', unsafe_allow_html=True)

        with b2:
            items_html_ps3 = "".join([
                f'''<div class="list-item-box">
                    <b style="color:#6d28d9;">{i+1}.</b> {up}
                </div>''' for i, up in enumerate(PS3_BOLA_UPDATES)
            ])
            st.markdown(f'''
                <div class="card-box card-purple">
                    <div class="service-title" style="font-size: 1.1rem; margin-bottom: 15px;">
                        <i class="bi bi-dribbble"></i> UPDATE BOLA PS3
                    </div>
                    {items_html_ps3}
                </div>
            ''', unsafe_allow_html=True)

    # === TAB 4: ANDROID & NINTENDO SWITCH ===
    with tab_extra:
        st.write("")
        ex1, ex2 = st.columns(2)
        with ex1:
            items_html_android = "".join([
                f'''<div class="list-item-box">
                    <b style="color:#15803d;">{i+1}.</b> {up}
                </div>''' for i, up in enumerate(ANDROID_SERVICES)
            ])
            st.markdown(f'''
                <div class="card-box card-green">
                    <div class="service-title" style="font-size: 1.1rem; margin-bottom: 15px;">
                        <i class="bi bi-android2"></i> ANDROID APPS & STREAMING
                    </div>
                    {items_html_android}
                </div>
            ''', unsafe_allow_html=True)

        with ex2:
            items_html_switch = "".join([
                f'''<div class="list-item-box">
                    <b style="color:#be123c;">{i+1}.</b> {game}
                </div>''' for i, game in enumerate(SWITCH_GAMES)
            ])
            st.markdown(f'''
                <div class="card-box card-pink">
                    <div class="service-title" style="font-size: 1.1rem; margin-bottom: 15px;">
                        <i class="bi bi-nintendo-switch"></i> NINTENDO SWITCH SUB INDO
                    </div>
                    {items_html_switch}
                </div>
            ''', unsafe_allow_html=True)

    # === TAB 5: ESTIMASI HARGA & ORDER (FITUR BARU) ===
    with tab_kalkulator:
        st.write("")
        k1, k2 = st.columns([1.3, 1.7])

        with k1:
            st.markdown('''
                <div class="card-box card-orange">
                    <div class="service-title" style="font-size:1.05rem;"><i class="bi bi-calculator"></i> KALKULATOR ESTIMASI HARGA</div>
            ''', unsafe_allow_html=True)
            layanan_pilih = st.selectbox("Pilih jenis layanan:", list(SERVICES_PRICE.keys()))
            satuan_per_game = "per game" in layanan_pilih.lower()
            qty = 1
            if satuan_per_game:
                qty = st.slider("Jumlah game:", min_value=1, max_value=10, value=1)
            harga_satuan = SERVICES_PRICE[layanan_pilih]
            total_harga = harga_satuan * qty
            st.markdown(f'''
                <div style="margin-top:14px; background: rgba(255,255,255,0.6); border-radius:10px; padding:12px;">
                    <small>Estimasi Total</small>
                    <div class="price-badge" style="font-size:1.8rem;">Rp {total_harga:,.0f}</div>
                </div>
                </div>
            '''.replace(",", "."), unsafe_allow_html=True)

        with k2:
            st.markdown('''
                <div class="card-box card-blue">
                    <div class="service-title" style="font-size:1.05rem;"><i class="bi bi-whatsapp"></i> FORM ORDER CEPAT (VIA WHATSAPP)</div>
            ''', unsafe_allow_html=True)
            with st.form("form_order"):
                nama = st.text_input("Nama kamu:")
                platform_pilih = st.selectbox("Platform:", ["PS4", "PS3", "Nintendo Switch", "Android"])
                catatan = st.text_area("Catatan tambahan (opsional):", placeholder="Contoh: mau order 3 game, tolong rekomendasikan judulnya")
                submitted = st.form_submit_button("📩 Buat Pesan Order")

            if submitted:
                game_terpilih = ", ".join(st.session_state.favorit_games) if st.session_state.favorit_games else "-"
                pesan = (
                    f"Halo MEDY5TATION, saya {nama or '(nama)'} ingin order.\n"
                    f"Layanan: {layanan_pilih} x{qty}\n"
                    f"Estimasi harga: Rp {total_harga:,.0f}\n".replace(",", ".") +
                    f"Platform: {platform_pilih}\n"
                    f"Game favorit: {game_terpilih}\n"
                    f"Catatan: {catatan or '-'}"
                )
                wa_link = "https://wa.me/6282289421650?text=" + urllib.parse.quote(pesan)
                st.success("Pesan siap dikirim! Klik tombol di bawah untuk lanjut ke WhatsApp.")
                st.markdown(f'<a href="{wa_link}" target="_blank" class="social-link btn-wa">💬 Kirim ke WhatsApp</a>', unsafe_allow_html=True)
                st.text_area("Preview pesan:", pesan, height=140)
            st.markdown("</div>", unsafe_allow_html=True)

    # === TAB 6: TESTIMONI & FAQ (FITUR BARU) ===
    with tab_info:
        st.write("")
        st.markdown("##### 💬 Testimoni Pelanggan")
        st.caption("Contoh tampilan testimoni — silakan ganti dengan testimoni asli dari pelanggan Anda.")
        t1, t2, t3 = st.columns(3)
        for col, (nama, rating, isi) in zip([t1, t2, t3], TESTIMONI_CONTOH):
            idx = TESTIMONI_CONTOH.index((nama, rating, isi))
            col.markdown(f'''
                <div class="card-box {card_color(idx)}">
                    <div style="font-weight:800;">{nama}</div>
                    <div style="color:#f59e0b; margin:4px 0;">{rating}</div>
                    <div style="font-size:0.85rem;">"{isi}"</div>
                </div>
            ''', unsafe_allow_html=True)

        st.write("")
        st.markdown("##### ❓ Pertanyaan yang Sering Ditanyakan (FAQ)")
        for q, a in FAQ_LIST:
            with st.expander(q):
                st.write(a)

    # -- FOOTER & KONTAK LENGKAP --
    st.markdown('<hr style="border-color: #e2e8f0; margin: 35px 0 25px 0;">', unsafe_allow_html=True)

    sec_lokasi, sec_order, sec_social = st.columns([1.5, 2, 2.5])

    with sec_lokasi:
        st.markdown('''
            <div style="margin-bottom: 8px;">
                <small style="color: #64748b; letter-spacing: 1px; font-weight:700;">LOKASI WORKSHOP</small>
                <div style="font-weight: 800; font-size: 1.25rem; color: #001f3f; margin-top: 4px;">
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
        <div style="display: flex; justify-content: space-between; align-items: center; margin-top: 40px; padding: 15px 0; border-top: 1px solid #e2e8f0; color: #64748b; font-size: 0.8rem; font-weight:600; flex-wrap: wrap; gap: 8px;">
            <div><b>MEDY5TATION</b></div>
            <div>&ldquo; GAME IS ALWAYS A GOOD IDEA &rdquo;</div>
            <div style="letter-spacing: 2px; color: #002d72;">&#9651; &#9675; &#10005; &#9633; PLAY &bull; SHARE &bull; TOGETHER</div>
        </div>
    ''', unsafe_allow_html=True)

if __name__ == "__main__":
    main()