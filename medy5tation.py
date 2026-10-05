import streamlit as st
import os
import base64
from urllib.parse import quote

WA_NUMBER = "6282289421650"

def get_image_base64(path):
    """Membaca file gambar lokal menjadi Base64"""
    if os.path.exists(path):
        with open(path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode()
    return None


def controller_svg(color="#c8264d", width=150):
    """[BARU] Gambar stik PS (outline merah hati seperti logo)"""
    return f'''
    <svg width="{width}" viewBox="0 0 200 120" fill="none" stroke="{color}" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round" xmlns="http://www.w3.org/2000/svg">
        <path d="M50 22 Q62 12 82 18 L118 18 Q138 12 150 22 Q176 30 188 76 Q196 108 174 110 Q158 110 144 86 L56 86 Q42 110 26 110 Q4 108 12 76 Q24 30 50 22 Z"/>
        <rect x="76" y="26" width="48" height="28" rx="4"/>
        <path d="M50 38 v20 M40 48 h20"/>
        <circle cx="150" cy="38" r="4.5" stroke="#34d399"/><circle cx="164" cy="50" r="4.5"/>
        <circle cx="150" cy="62" r="4.5"/><circle cx="136" cy="50" r="4.5"/>
        <circle cx="82" cy="74" r="11"/><circle cx="118" cy="74" r="11"/>
        <path d="M92 60 h16"/>
    </svg>'''

def wa_link(text=""):
    """[BARU] Membuat link WhatsApp dengan pesan otomatis"""
    return f"https://wa.me/{WA_NUMBER}?text={quote(text)}"

def set_page_styling():
    st.set_page_config(
        page_title="MEDY5TATION - Game Together",
        page_icon="🎮",
        layout="wide",
        initial_sidebar_state="collapsed",
    )
    # CDN Icons Bootstrap
    st.markdown('<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css">', unsafe_allow_html=True)

    # CSS: Background putih, seluruh layer box Biru Tua (Navy) - tanpa hitam
    custom_css = """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Kanit:wght@300;400;600;700;800&family=Satisfy&display=swap');

        /* [BARU] Palet layering biru tua: luar > tengah > dalam */
        :root {
            --navy-1: #0a2a5e;
            --navy-2: #0f3a7a;
            --navy-3: #164a94;
            --navy-line: #1e4fa3;
            --accent: #38bdf8;
            --pink: #c8264d;
            --heart: #c8264d;
        }

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
            color: #c8264d !important;
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

        /* Bar Fitur Atas - Layer Box Biru Tua (luar) + tiap item (dalam) */
        .feature-bar {
            display: flex;
            justify-content: space-around;
            text-align: center;
            margin-bottom: 25px;
            flex-wrap: wrap;
            gap: 12px;
            background: var(--navy-1) !important;
            border: 1.5px solid var(--navy-line) !important;
            border-radius: 16px;
            padding: 12px 10px;
            box-shadow: 0 4px 12px rgba(10, 42, 94, 0.25);
        }
        .feature-item {
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 4px;
            color: #f1f5f9;
            font-weight: 600;
            background: var(--navy-2);
            border: 1px solid var(--navy-line);
            border-radius: 10px;
            padding: 10px 16px;
            min-width: 130px;
        }

        /* TAB NAVIGATION - Layer luar (wadah) + Box tiap tab Biru Tua */
        [data-baseweb="tab-list"] {
            gap: 12px !important;
            justify-content: center !important;
            padding: 10px !important;
            flex-wrap: wrap;
            background: var(--navy-1) !important;               /* [BARU] layer luar navigasi */
            border: 1.5px solid var(--navy-line) !important;
            border-radius: 16px !important;
            box-shadow: 0 4px 12px rgba(10, 42, 94, 0.25);
            margin-bottom: 18px;
        }
        [data-baseweb="tab"] {
            border-radius: 10px !important;
            padding: 10px 24px !important;
            height: auto !important;
            background-color: var(--navy-2) !important; /* Box Biru Tua (layer dalam) */
            border: 1.5px solid var(--navy-line) !important;
            transition: all 0.2s ease-in-out !important;
        }
        [data-baseweb="tab"] p,
        [data-baseweb="tab"] span {
            color: #ffffff !important;
            font-weight: 700 !important;
            font-size: 0.95rem !important;
        }
        [data-baseweb="tab"]:hover {
            background-color: var(--navy-3) !important;
            border-color: var(--accent) !important;
            transform: translateY(-2px);
        }
        [data-baseweb="tab"][aria-selected="true"] {
            background-color: #c8264d !important; /* Aksen Aktif Magenta/Merah */
            border-color: #c8264d !important;
        }
        [data-baseweb="tab-highlight"],
        [data-baseweb="tab-border"] {
            background-color: transparent !important;
        }

        /* KARTU KONTEN - SEMUA LAYER BOX BIRU TUA */
        .card-box {
            border-radius: 12px;
            padding: 20px;
            margin-bottom: 15px;
            height: 100%;
            background-color: var(--navy-2) !important; /* Biru Tua Navy */
            color: #ffffff !important;
            border: 1.5px solid var(--navy-line) !important;
            box-shadow: 0 6px 16px rgba(10, 42, 94, 0.18);
            transition: transform 0.2s, box-shadow 0.2s;
        }
        .card-box:hover {
            transform: translateY(-3px);
            box-shadow: 0 8px 20px rgba(10, 42, 94, 0.28);
        }
        .card-featured {
            border: 1.5px solid #c8264d !important;
        }
        .price-badge {
            color: #ff8fa5 !important;
            font-size: 2.3rem;
            font-weight: 800;
            line-height: 1;
        }
        .service-title {
            color: #38bdf8 !important; /* Aksen Biru Terang untuk Judul di Dalam Box Biru Tua */
            font-size: 1rem;
            font-weight: 700;
            text-transform: uppercase;
            margin-top: 8px;
            margin-bottom: 8px;
            letter-spacing: 0.5px;
        }

        /* [BARU] LAYERING BOX 3 LAPIS: luar > tengah > item (untuk Bola, Android, Switch) */
        .layer-outer {
            background: var(--navy-1);
            border: 1.5px solid var(--navy-line);
            border-radius: 18px;
            padding: 10px;
            margin-bottom: 15px;
            box-shadow: 0 6px 18px rgba(10, 42, 94, 0.25);
        }
        .layer-inner {
            background: var(--navy-2);
            border: 1px solid var(--navy-line);
            border-radius: 12px;
            padding: 14px;
        }
        .item-tag {
            margin-left: auto;
            background: rgba(56, 189, 248, 0.18);
            color: #bae6fd;
            font-size: 0.7rem;
            padding: 2px 8px;
            border-radius: 20px;
            font-weight: 600;
        }

        /* List Items di dalam Box Bola / Extra (layer item) */
        .list-item-box {
            background: var(--navy-3);
            border: 1px solid #2a63b8;
            padding: 10px 14px;
            border-radius: 8px;
            margin-bottom: 8px;
            font-size: 0.9rem;
            color: #ffffff;
            display: flex;
            align-items: center;
            gap: 8px;
            transition: all 0.15s ease-in-out;
        }
        .list-item-box:hover {
            border-color: var(--accent);
            transform: translateX(3px);
        }

        /* KOTAK LIST GAME - LAYER BOX BIRU TUA */
        .game-badge {
            background-color: var(--navy-3) !important;
            border: 1px solid #2a63b8 !important;
            border-radius: 8px;
            padding: 9px 12px;
            margin-bottom: 8px;
            font-size: 0.85rem;
            display: flex;
            align-items: center;
            gap: 8px;
            transition: all 0.15s ease-in-out;
        }
        .game-badge:hover {
            border-color: #38bdf8 !important;
            background-color: #1a56a8 !important;
            transform: scale(1.02);
        }
        .game-num {
            color: #38bdf8 !important;
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
        .btn-tiktok { background-color: var(--navy-1); border: 1px solid var(--navy-line); color: white !important; } /* bukan hitam lagi */
        .btn-ig { background: linear-gradient(45deg, #f09433 0%, #e6683c 25%, #dc2743 50%, #cc2366 75%, #bc1888 100%); color: white !important; }
        .btn-yt { background-color: #FF0000; color: white !important; }

        /* [BARU] Tombol WhatsApp melayang */
        .wa-float {
            position: fixed; right: 22px; bottom: 22px; z-index: 999;
            background: #25D366; color: #fff !important;
            width: 56px; height: 56px; border-radius: 50%;
            display: flex; align-items: center; justify-content: center;
            font-size: 1.8rem; text-decoration: none !important;
            box-shadow: 0 6px 16px rgba(0, 0, 0, 0.25);
        }

        /* [BARU] Metric & Expander biru tua */
        [data-testid="stMetric"] {
            background: var(--navy-1); border: 1.5px solid var(--navy-line);
            border-radius: 12px; padding: 12px 16px;
        }
        [data-testid="stMetricLabel"] p { color: var(--accent) !important; }
        [data-testid="stMetricValue"] { color: #ffffff !important; }
        [data-testid="stExpander"] {
            background: var(--navy-1); border: 1.5px solid var(--navy-line); border-radius: 12px;
        }
        [data-testid="stExpander"] summary p { color: #ffffff !important; font-weight: 600; }
        [data-testid="stExpander"] div[data-testid="stMarkdownContainer"] p { color: #e2e8f0; }

        /* [BARU] Teks tab dipaksa putih (tidak tabrakan dengan background navy) */
        [data-baseweb="tab"], [data-baseweb="tab"] *, button[role="tab"], button[role="tab"] * {
            color: #ffffff !important;
            opacity: 1 !important;
        }
        [data-baseweb="tab"][aria-selected="true"] { box-shadow: 0 4px 14px rgba(200, 38, 77, 0.45); }
        /* [BARU] Aksen merah hati (sesuai logo) */
        .layer-outer { border-top: 3px solid var(--heart); }
        .card-box { border-top: 3px solid var(--heart) !important; }
        .feature-bar { border-top: 3px solid var(--heart) !important; }
        .brand-logo-img { border: 2px solid var(--heart); box-shadow: 0 6px 18px rgba(10, 42, 94, 0.3); }
        .stick-wrap { text-align: center; opacity: 0.95; }
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

# ---------- [BARU] Fungsi bantu ----------
def filter_list(items, q):
    """Filter list berdasarkan kata kunci pencarian"""
    return [x for x in items if q.lower() in x.lower()] if q else items

def hitung_pkg(n):
    """PKG & Instal: 25K per game, paket 3 game = 65K"""
    return (n // 3) * 65000 + (n % 3) * 25000

def rupiah(n):
    return "Rp " + f"{n:,}".replace(",", ".")

def layered_box(title, icon, items, number_color="#38bdf8", title_color="#38bdf8", tag="Tersedia"):
    """Box layering 3 lapis biru tua: layer luar > layer tengah > item"""
    if items:
        items_html = "".join([
            f'''<div class="list-item-box">
                <b style="color: {number_color};">{i+1}.</b> {it}
                <span class="item-tag">{tag}</span>
            </div>''' for i, it in enumerate(items)
        ])
    else:
        items_html = '<div class="list-item-box">Tidak ada hasil yang cocok.</div>'
    return f'''
        <div class="layer-outer">
            <div class="layer-inner">
                <div class="service-title" style="font-size: 1.1rem; color: {title_color} !important; margin-bottom: 15px;">
                    <i class="bi {icon}"></i> {title}
                </div>
                {items_html}
            </div>
        </div>
    '''

def main():
    set_page_styling()

    # [BARU] Tombol WhatsApp melayang
    st.markdown(f'<a class="wa-float" href="{wa_link("Halo Medy5tation, saya mau tanya layanan")}" target="_blank"><i class="bi bi-whatsapp"></i></a>', unsafe_allow_html=True)

    # -- HEADER UTAMA --
    col_h1, col_h2, col_h3 = st.columns([1.2, 3, 1.2])
    with col_h1:
        st.markdown('<p class="cursive-title">Good Games<br>Better Days</p>', unsafe_allow_html=True)
        st.markdown(f'<div class="stick-wrap" style="text-align:left;margin-top:10px;">{controller_svg(width=130)}</div>', unsafe_allow_html=True)
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
                    <div class="stick-wrap">'''+controller_svg(width=120)+'''</div>
                    <h1 style="letter-spacing: 4px; margin: 0; font-size: 3rem; color: #0a2a5e;">MEDY5TATION</h1>
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

    # -- 5 FITUR UTAMA (BOX BIRU TUA) --
    st.markdown('''
        <div class="feature-bar">
            <div class="feature-item"><i class="bi bi-disc" style="font-size: 1.6rem; color: #38bdf8;"></i><small>GAME ORIGINAL</small></div>
            <div class="feature-item"><i class="bi bi-cloud-arrow-down" style="font-size: 1.6rem; color: #38bdf8;"></i><small>PATCH SUB INDO</small></div>
            <div class="feature-item"><i class="bi bi-device-hdd" style="font-size: 1.6rem; color: #38bdf8;"></i><small>HDD FULL GAME</small></div>
            <div class="feature-item"><i class="bi bi-gear-wide-connected" style="font-size: 1.6rem; color: #38bdf8;"></i><small>INSTAL LANGSUNG</small></div>
            <div class="feature-item"><i class="bi bi-shield-check" style="font-size: 1.6rem; color: #38bdf8;"></i><small>AMAN & TERPERCAYA</small></div>
        </div>
    ''', unsafe_allow_html=True)

    # -- [BARU] STATISTIK RINGKAS --
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Game PS4 Sub Indo", len(PS4_GAMES))
    m2.metric("Patch Bola PS4", len(PS4_HEN_UPDATES))
    m3.metric("Game Switch", len(SWITCH_GAMES))
    m4.metric("Layanan Android", len(ANDROID_SERVICES))
    st.write("")

    # -- NAVIGASI MENU (+ tab baru Kalkulator Order) --
    tab_beranda, tab_games, tab_calc, tab_bola, tab_extra = st.tabs([
        "🏠 Paket & Layanan",
        f"🎮 List Game Sub Indo ({len(PS4_GAMES)})",
        "🛒 Kalkulator Order",
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
                    <i class="bi bi-google-play" style="font-size: 2rem; color: #38bdf8;"></i>
                    <div class="service-title">VIA DRIVE</div>
                    <div class="price-badge">15K</div>
                    <small style="color: #bae6fd;">PER GAME</small>
                    <p style="font-size: 0.82rem; color: #e2e8f0; margin-top: 12px;">Patch Sub Indo & Link Download sesuai CUSA game</p>
                </div>
            ''', unsafe_allow_html=True)

        with p2:
            st.markdown('''
                <div class="card-box card-featured" style="text-align: center;">
                    <i class="bi bi-box-arrow-in-down" style="font-size: 2rem; color: #38bdf8;"></i>
                    <div class="service-title">PKG & INSTAL DI PS</div>
                    <div class="price-badge">25K</div>
                    <small style="color: #bae6fd;">PER GAME</small>
                    <div style="margin-top: 10px; background-color: #c8264d; padding: 6px; border-radius: 6px; font-weight: 700; font-size: 0.85rem; color: white;">
                        3 GAME 65K
                    </div>
                    <small style="color: #e2e8f0; display: block; margin-top: 8px;">Lokasi Palembang</small>
                </div>
            ''', unsafe_allow_html=True)

        with p3:
            st.markdown('''
                <div class="card-box card-featured" style="text-align: center;">
                    <i class="bi bi-hdd-network" style="font-size: 2rem; color: #38bdf8;"></i>
                    <div class="service-title">HDD FULL GAME (PKG/PNP)</div>
                    <div style="display: flex; justify-content: space-around; margin-top: 10px;">
                        <div>
                            <span style="background:white; color:#0a2a5e; padding:3px 8px; border-radius:4px; font-size:0.75rem; font-weight:bold;">500GB</span>
                            <div style="color:#ff8fa5; font-size:1.6rem; font-weight:800; margin-top:4px;">350RB</div>
                        </div>
                        <div>
                            <span style="background:white; color:#0a2a5e; padding:3px 8px; border-radius:4px; font-size:0.75rem; font-weight:bold;">1TB</span>
                            <div style="color:#ff8fa5; font-size:1.6rem; font-weight:800; margin-top:4px;">550RB</div>
                        </div>
                    </div>
                    <small style="color: #e2e8f0; display: block; margin-top: 10px;">Plug and Play / Siap Main</small>
                </div>
            ''', unsafe_allow_html=True)

        st.write("")
        s1, s2, s3 = st.columns(3)
        with s1:
            st.markdown('''
                <div class="card-box">
                    <i class="bi bi-cpu" style="font-size: 1.8rem; color: #38bdf8;"></i>
                    <div class="service-title">JASA HEN PS4</div>
                    <div class="price-badge">50K</div>
                    <ul style="font-size: 0.82rem; padding-left: 18px; margin: 10px 0 0 0; color: #e2e8f0; line-height: 1.6;">
                        <li>Install Sistem HEN</li>
                        <li>Setting & Tes Game Lengkap</li>
                        <li>Panduan Pemakaian Sampai Paham</li>
                    </ul>
                </div>
            ''', unsafe_allow_html=True)

        with s2:
            st.markdown('''
                <div class="card-box">
                    <i class="bi bi-thermometer-half" style="font-size: 1.8rem; color: #38bdf8;"></i>
                    <div class="service-title">GANTI PASTA THERMAL</div>
                    <div class="price-badge">250RB</div>
                    <ul style="font-size: 0.82rem; padding-left: 18px; margin: 10px 0 0 0; color: #e2e8f0; line-height: 1.6;">
                        <li>Deep Cleaning / Pembersihan Debu Mesin</li>
                        <li>Aplikasi Thermal Paste Premium Berkualitas</li>
                        <li>Meredam Kipas Bising & Mengatasi Overheat</li>
                    </ul>
                </div>
            ''', unsafe_allow_html=True)

        with s3:
            st.markdown('''
                <div class="card-box">
                    <i class="bi bi-joystick" style="font-size: 1.8rem; color: #38bdf8;"></i>
                    <div class="service-title">SERVIS STIK PS4</div>
                    <div class="price-badge" style="font-size: 1.6rem; margin-bottom: 6px;">KONSULTASI</div>
                    <ul style="font-size: 0.82rem; padding-left: 18px; margin: 6px 0 0 0; color: #e2e8f0; line-height: 1.6;">
                        <li>Perbaikan Analog Drift / Tidak Stabil</li>
                        <li>Tombol Keras atau Tidak Responsif</li>
                        <li>Ganti Part / Jalur / Cleaning</li>
                        <li>Kustomisasi & Upgrade Mod</li>
                    </ul>
                </div>
            ''', unsafe_allow_html=True)

        # [BARU] FAQ
        st.write("")
        st.markdown("##### ❓ Pertanyaan yang Sering Ditanyakan")
        with st.expander("Apa bedanya Via Drive dan PKG & Instal di PS?"):
            st.write("Via Drive: kamu mendapat patch & link download, lalu install sendiri. PKG & Instal: game langsung dipasang di PS4 kamu (lokasi Palembang).")
        with st.expander("Apakah PS4 saya harus sudah HEN?"):
            st.write("Untuk game PKG, konsol perlu sistem HEN. Belum punya? Gunakan Jasa HEN PS4 (50K).")
        with st.expander("Bagaimana cara order?"):
            st.write("Pilih game di tab **Kalkulator Order**, lalu klik tombol kirim ke WhatsApp.")

    # === TAB 2: KATALOG 82 GAME SUB INDO ===
    with tab_games:
        st.write("")
        search_query = st.text_input("🔍 Cari Judul Game Patch Bahasa Indonesia:", placeholder="Contoh: God of War, Spiderman, Resident Evil...")
        sort_az = st.toggle("Urutkan A–Z", value=False)  # [BARU]

        filtered_games = [g for g in PS4_GAMES if search_query.lower() in g.lower()] if search_query else PS4_GAMES
        if sort_az:
            filtered_games = sorted(filtered_games, key=str.lower)
        st.caption(f"Menampilkan {len(filtered_games)} dari {len(PS4_GAMES)} game")  # [BARU]

        if not filtered_games:
            st.info("Game yang dicari belum tersedia dalam daftar.")
            # [BARU] Tombol request game
            st.markdown(f'<a href="{wa_link("Halo, saya request game: " + search_query)}" target="_blank" class="social-link btn-wa" style="max-width:260px;"><i class="bi bi-whatsapp"></i> Request Game</a>', unsafe_allow_html=True)
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

    # === [BARU] TAB 3: KALKULATOR ORDER ===
    with tab_calc:
        st.write("")
        st.markdown('''
            <div class="layer-outer"><div class="layer-inner">
                <div class="service-title" style="font-size: 1.1rem; margin: 0;"><i class="bi bi-cart3"></i> PILIH GAME & HITUNG TOTAL</div>
            </div></div>
        ''', unsafe_allow_html=True)
        picks = st.multiselect("Pilih game yang ingin dipesan:", PS4_GAMES)
        metode = st.radio("Metode:", ["Via Drive (15K/game)", "PKG & Instal di PS (25K/game, 3 game 65K)"], horizontal=True)
        n = len(picks)
        total = n * 15000 if metode.startswith("Via") else hitung_pkg(n)
        k1, k2 = st.columns(2)
        k1.metric("Jumlah Game", n)
        k2.metric("Estimasi Total", rupiah(total))
        if n:
            msg = f"Halo Medy5tation, saya mau order:\nMetode: {metode}\n" + "\n".join(f"- {g}" for g in picks) + f"\nTotal: {rupiah(total)}"
            st.markdown(f'<a href="{wa_link(msg)}" target="_blank" class="social-link btn-wa"><i class="bi bi-whatsapp"></i> Kirim Pesanan ke WhatsApp</a>', unsafe_allow_html=True)
        else:
            st.info("Pilih minimal 1 game untuk melihat total & tombol order.")

    # === TAB 4: UPDATE PATCH BOLA (LAYERING BOX BIRU TUA) ===
    with tab_bola:
        st.write("")
        qb = st.text_input("🔍 Cari patch bola:", key="qb", placeholder="Contoh: Monster, Bitbox...")  # [BARU]
        b1, b2 = st.columns(2)
        with b1:
            st.markdown(layered_box("UPDATE BOLA PS4 HEN (SUMMER 2027)", "bi-dribbble",
                                    filter_list(PS4_HEN_UPDATES, qb), tag="Terbaru"), unsafe_allow_html=True)
        with b2:
            st.markdown(layered_box("UPDATE BOLA PS3", "bi-dribbble",
                                    filter_list(PS3_BOLA_UPDATES, qb)), unsafe_allow_html=True)
        st.markdown(f'<a href="{wa_link("Halo, saya mau order update patch bola")}" target="_blank" class="social-link btn-wa" style="max-width:300px;"><i class="bi bi-whatsapp"></i> Order Patch Bola</a>', unsafe_allow_html=True)

    # === TAB 5: ANDROID & NINTENDO SWITCH (LAYERING BOX BIRU TUA) ===
    with tab_extra:
        st.write("")
        qe = st.text_input("🔍 Cari layanan / game:", key="qe", placeholder="Contoh: Spotify, Zelda...")  # [BARU]
        ex1, ex2 = st.columns(2)
        with ex1:
            st.markdown(layered_box("ANDROID APPS & STREAMING", "bi-android2",
                                    filter_list(ANDROID_SERVICES, qe),
                                    number_color="#10b981", title_color="#34d399", tag="Aktif"), unsafe_allow_html=True)
        with ex2:
            st.markdown(layered_box("NINTENDO SWITCH SUB INDO", "bi-nintendo-switch",
                                    filter_list(SWITCH_GAMES, qe),
                                    number_color="#ff8fa5"), unsafe_allow_html=True)
        st.markdown(f'<a href="{wa_link("Halo, saya mau order layanan Android/Switch")}" target="_blank" class="social-link btn-wa" style="max-width:300px;"><i class="bi bi-whatsapp"></i> Order Android / Switch</a>', unsafe_allow_html=True)

    # -- FOOTER & KONTAK LENGKAP --
    st.markdown('<hr style="border-color: #e2e8f0; margin: 35px 0 25px 0;">', unsafe_allow_html=True)

    sec_lokasi, sec_order, sec_social = st.columns([1.5, 2, 2.5])

    with sec_lokasi:
        st.markdown('''
            <div style="margin-bottom: 8px;">
                <small style="color: #64748b; letter-spacing: 1px; font-weight:700;">LOKASI WORKSHOP</small>
                <div style="font-weight: 800; font-size: 1.25rem; color: #0a2a5e; margin-top: 4px;">
                    <i class="bi bi-geo-alt-fill" style="color: #c8264d;"></i> PALEMBANG
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

    # [BARU] Stik PS di footer
    st.markdown(f'<div class="stick-wrap" style="margin-top:30px;">{controller_svg(width=90)}</div>', unsafe_allow_html=True)

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