import streamlit as st
import os
import io
import json
import html
import base64
import random
import string
from datetime import datetime, date
from urllib.parse import quote

try:
    from zoneinfo import ZoneInfo
    WIB = ZoneInfo("Asia/Jakarta")
except Exception:  # pragma: no cover
    WIB = None

# =====================================================================
# KONFIGURASI TOKO  (ubah di sini)
# =====================================================================
WA_NUMBER = "6282289421650"
OPEN_HOUR, CLOSE_HOUR = 10, 21          # jam buka toko (WIB)
OPEN_DAYS = [0, 1, 2, 3, 4, 5, 6]       # 0=Senin ... 6=Minggu
STORE_LAT, STORE_LON = -2.9761, 104.7754  # titik peta (sesuaikan dengan lokasi workshop)
DATA_DIR = "data"
ORDERS_FILE = os.path.join(DATA_DIR, "orders.json")
REVIEWS_FILE = os.path.join(DATA_DIR, "reviews.json")

STATUS_FLOW = [
    "Diterima",
    "Sedang Dicek",
    "Menunggu Persetujuan",
    "Dikerjakan",
    "Selesai",
    "Sudah Diambil",
]

SERVICES = {
    "Jasa HEN PS4": 50_000,
    "Ganti Pasta Thermal": 250_000,
}

# =====================================================================
# UTILITAS
# =====================================================================
def now():
    return datetime.now(WIB) if WIB else datetime.now()


def rupiah(n):
    return "Rp " + f"{int(n):,}".replace(",", ".")


def wa_link(text=""):
    return f"https://wa.me/{WA_NUMBER}?text={quote(text)}"


def html_block(s):
    """Render HTML tanpa indentasi supaya tidak dibaca sebagai code block markdown."""
    clean = "\n".join(line.strip() for line in s.splitlines() if line.strip())
    st.markdown(clean, unsafe_allow_html=True)


def get_image_base64(path):
    if os.path.exists(path):
        with open(path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    return None


def load_json(path, default):
    try:
        if os.path.exists(path):
            with open(path, "r", encoding="utf-8") as f:
                return json.load(f)
    except Exception:
        pass
    return default


def save_json(path, data):
    try:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        return True
    except Exception:
        return False


def new_ticket(existing):
    while True:
        code = "MD-" + "".join(random.choices(string.ascii_uppercase + string.digits, k=5))
        if code not in existing:
            return code


def admin_password():
    try:
        pw = st.secrets.get("ADMIN_PASSWORD")
        if pw:
            return pw
    except Exception:
        pass
    return os.environ.get("ADMIN_PASSWORD", "medy5admin")


def store_status():
    t = now()
    is_open = t.weekday() in OPEN_DAYS and OPEN_HOUR <= t.hour < CLOSE_HOUR
    return is_open, t


# =====================================================================
# LOGO STIK (SVG)
# =====================================================================
CONTROLLER_SVG = """
<svg class="controller-logo" viewBox="0 0 240 140" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Logo stik MEDY5TATION">
  <defs>
    <linearGradient id="mdGrad" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#ff2a6d"/>
      <stop offset="100%" stop-color="#05d9e8"/>
    </linearGradient>
    <linearGradient id="mdFill" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#151c2e"/>
      <stop offset="100%" stop-color="#0b0f19"/>
    </linearGradient>
  </defs>
  <path d="M62 30 C42 30 27 45 19 80 C13 110 19 126 33 126 C47 126 55 113 67 99 L173 99 C185 113 193 126 207 126 C221 126 227 110 221 80 C213 45 198 30 178 30 Z"
        fill="url(#mdFill)" stroke="url(#mdGrad)" stroke-width="4" stroke-linejoin="round"/>
  <rect x="98" y="41" width="44" height="22" rx="6" fill="none" stroke="#334155" stroke-width="2"/>
  <line x1="104" y1="33" x2="136" y2="33" stroke="#05d9e8" stroke-width="3" stroke-linecap="round"/>
  <g fill="#e2e8f0">
    <rect x="55" y="55" width="8" height="26" rx="2"/>
    <rect x="46" y="64" width="26" height="8" rx="2"/>
  </g>
  <g fill="none" stroke-width="3" stroke-linecap="round" stroke-linejoin="round">
    <path d="M180 41 L174.5 50 L185.5 50 Z" stroke="#10b981"/>
    <circle cx="196" cy="62" r="5.5" stroke="#ff2a6d"/>
    <path d="M175 66 L185 76 M185 66 L175 76" stroke="#05d9e8"/>
    <rect x="157" y="57" width="10" height="10" rx="1.5" stroke="#c084fc"/>
  </g>
  <circle cx="88" cy="86" r="12" fill="#0b0f19" stroke="#475569" stroke-width="2.5"/>
  <circle cx="88" cy="86" r="5" fill="#475569"/>
  <circle cx="152" cy="86" r="12" fill="#0b0f19" stroke="#475569" stroke-width="2.5"/>
  <circle cx="152" cy="86" r="5" fill="#475569"/>
</svg>
"""

# =====================================================================
# STYLING
# =====================================================================
def set_page_styling():
    st.set_page_config(
        page_title="MEDY5TATION - Game Together",
        page_icon="🎮",
        layout="wide",
        initial_sidebar_state="collapsed",
    )
    st.markdown(
        '<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css">',
        unsafe_allow_html=True,
    )
    custom_css = """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Kanit:wght@300;400;600;700;800&family=Satisfy&display=swap');

        .stApp { background-color: #0b0f19 !important; color: #ffffff !important; font-family: 'Kanit', sans-serif !important; }
        .stApp label, .stApp p, .stApp span, .stApp li { font-family: 'Kanit', sans-serif; }

        .brand-container { text-align: center; padding: 5px 0; }
        .controller-logo {
            width: 150px; max-width: 60%; height: auto; display: block; margin: 0 auto 6px auto;
            filter: drop-shadow(0 0 10px rgba(255,42,109,.45)) drop-shadow(0 0 18px rgba(5,217,232,.30));
        }
        @media (prefers-reduced-motion: no-preference) {
            .controller-logo { animation: mdFloat 4s ease-in-out infinite; }
            @keyframes mdFloat { 0%,100% { transform: translateY(0); } 50% { transform: translateY(-5px); } }
        }
        .brand-logo-img { max-width: 210px; width: 100%; height: auto; border-radius: 12px; display: block; margin: 0 auto; }
        .brand-title { letter-spacing: 5px; margin: 0; font-size: 2.8rem; color: #fff; font-weight: 800; }
        .brand-title b { background: linear-gradient(90deg,#ff2a6d,#05d9e8); -webkit-background-clip: text; background-clip: text; color: transparent; }
        .cursive-title { font-family: 'Satisfy', cursive !important; color: #ff2a6d !important; font-size: 2.8rem; line-height: 1.1; margin: 0; text-align: left; }
        .cursive-subtitle { font-family: 'Satisfy', cursive !important; color: #05d9e8 !important; font-size: 2.2rem; line-height: 1.1; margin: 0; text-align: right; }
        .brand-subtitle { font-size: .95rem; letter-spacing: 4px; color: #94a3b8; margin-top: 8px; margin-bottom: 20px; font-weight: 700; }

        .status-pill { display: inline-flex; align-items: center; gap: 8px; padding: 6px 14px; border-radius: 999px; font-size: .85rem; font-weight: 600; border: 1px solid; }
        .status-open { color: #10b981; border-color: #10b981; background: rgba(16,185,129,.08); }
        .status-closed { color: #f87171; border-color: #f87171; background: rgba(248,113,113,.08); }
        .dot { width: 8px; height: 8px; border-radius: 50%; background: currentColor; display: inline-block; }

        .feature-bar { display: flex; justify-content: space-around; text-align: center; margin-bottom: 25px; flex-wrap: wrap; gap: 12px; background: #111827; border: 1px solid #1f2937; border-radius: 16px; padding: 14px 10px; }
        .feature-item { display: flex; flex-direction: column; align-items: center; gap: 4px; color: #e2e8f0; font-size: .8rem; font-weight: 600; }

        div[data-baseweb="tab-list"] { gap: 10px !important; justify-content: flex-start !important; padding-bottom: 10px !important; border-bottom: 1px solid #1f2937 !important; background: transparent !important; overflow-x: auto; }
        div[data-baseweb="tab"] { background: transparent !important; border: none !important; padding: 8px 12px !important; white-space: nowrap; }
        div[data-baseweb="tab"] p, div[data-baseweb="tab"] span { color: #cbd5e1 !important; font-weight: 600 !important; font-size: .92rem !important; }
        div[data-baseweb="tab"][aria-selected="true"] p, div[data-baseweb="tab"][aria-selected="true"] span { color: #ff2a6d !important; font-weight: 700 !important; }
        div[data-baseweb="tab-highlight"] { background-color: #ff2a6d !important; height: 2px !important; }

        .card-box { border-radius: 14px; padding: 22px 18px; margin-bottom: 15px; height: 100%; background-color: #111827; color: #fff; transition: transform .2s; }
        .card-box:hover { transform: translateY(-3px); }
        .border-cyan { border: 1.5px solid #05d9e8 !important; }
        .border-pink { border: 1.5px solid #ff2a6d !important; }
        .border-purple { border: 1.5px solid #a855f7 !important; }
        .border-green { border: 1.5px solid #10b981 !important; }

        .price-badge-cyan { color: #05d9e8 !important; font-size: 2.2rem; font-weight: 800; line-height: 1.1; }
        .price-badge-pink { color: #ff2a6d !important; font-size: 2.2rem; font-weight: 800; line-height: 1.1; }
        .price-badge-purple { color: #c084fc !important; font-size: 1.6rem; font-weight: 800; }
        .promo-banner { background: linear-gradient(90deg,#ff2a6d,#d91b5c); color: #fff; font-size: .8rem; font-weight: 700; padding: 6px; border-radius: 6px; margin-top: 12px; letter-spacing: .5px; }

        .list-item-dark { background: rgba(255,255,255,.05); border: 1px solid rgba(255,255,255,.1); padding: 10px 14px; border-radius: 8px; margin-bottom: 8px; font-size: .88rem; color: #fff; }

        .game-badge { background-color: #111827 !important; border: 1px solid #1f2937 !important; border-radius: 8px; padding: 8px 12px; margin-bottom: 8px; font-size: .85rem; display: flex; align-items: center; gap: 8px; }
        .game-badge:hover { border-color: #ff2a6d !important; background-color: #1f2937 !important; }
        .game-num { color: #ff2a6d !important; font-weight: 800; font-size: .85rem; min-width: 28px; }

        .social-link { display: inline-flex; align-items: center; justify-content: center; gap: 8px; padding: 10px 16px; border-radius: 8px; font-weight: 600; text-decoration: none !important; font-size: .9rem; margin-bottom: 8px; width: 100%; text-align: center; }
        .btn-wa { background-color: #25D366; color: #fff !important; }
        .btn-shopee { background-color: #EE4D2D; color: #fff !important; }
        .btn-tiktok { background-color: #000; border: 1px solid #374151; color: #fff !important; }
        .btn-ig { background: linear-gradient(45deg,#f09433 0%,#e6683c 25%,#dc2743 50%,#cc2366 75%,#bc1888 100%); color: #fff !important; }
        .btn-yt { background-color: #f00; color: #fff !important; }

        /* Tracker */
        .track { display: flex; gap: 6px; margin: 14px 0 6px 0; }
        .track .step { flex: 1; height: 8px; border-radius: 4px; background: #1f2937; }
        .track .step.done { background: linear-gradient(90deg,#ff2a6d,#05d9e8); }
        .ticket-code { font-size: 2rem; font-weight: 800; letter-spacing: 3px; color: #05d9e8; }

        .review { background: #111827; border: 1px solid #1f2937; border-left: 3px solid #ff2a6d; border-radius: 10px; padding: 12px 16px; margin-bottom: 10px; }
        .review .stars { color: #f59e0b; letter-spacing: 2px; }
        .review small { color: #94a3b8; }

        .total-box { background: #111827; border: 1.5px solid #05d9e8; border-radius: 14px; padding: 18px; text-align: center; }
        .total-box .amount { font-size: 2.4rem; font-weight: 800; color: #05d9e8; }

        /* Tombol WhatsApp melayang */
        .wa-float { position: fixed; right: 18px; bottom: 18px; z-index: 9999; background: #25D366; color: #fff !important; width: 54px; height: 54px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 1.7rem; text-decoration: none !important; box-shadow: 0 6px 18px rgba(0,0,0,.5); }

        /* Input gelap */
        .stTextInput input, .stTextArea textarea, .stSelectbox div[data-baseweb="select"] > div, .stDateInput input, .stNumberInput input { background-color: #111827 !important; color: #fff !important; }
        </style>
    """
    st.markdown(custom_css, unsafe_allow_html=True)


# =====================================================================
# DATA KATALOG
# =====================================================================
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
    "Horizon zero down", "Spiderman", "Spiderman Miles morales", "detroit", "death stranding",
]

PS4_HEN_UPDATES = [
    "Monster patch summer 2027",
    "Eleven Patch summer 2027 Final Update",
    "Bitbox patch summer 2027",
    "Leader patch summer 2027",
    "monster 2018 patch summer 2027",
]
PS3_BOLA_UPDATES = ["Bitbox patch", "Vr patch"]
ANDROID_SERVICES = ["Spotify mod premium", "Netflix (Nonton film gabungan vidio viu dkk)"]
SWITCH_GAMES = ["DREDGE", "STRAY", "RDR", "Zelda BOTW"]

FAQ = [
    ("Berapa lama pengerjaan servis?",
     "Tergantung jenis dan tingkat kerusakan. Ganti pasta thermal dan servis stik biasanya lebih cepat dari kerusakan mesin. "
     "Estimasi pasti diberikan setelah unit dicek lewat WhatsApp atau di workshop."),
    ("Apakah bisa konsultasi dulu sebelum servis?",
     "Bisa. Kirim keluhan dan foto/video kondisi unit lewat WhatsApp, lalu kami bantu perkiraan penyebab dan biayanya."),
    ("Bagaimana cara memantau progres servis?",
     "Setelah booking lewat tab Booking Servis, kamu mendapat kode tiket. Masukkan kode itu di tab Cek Status kapan saja."),
    ("Apa saja yang dikerjakan di Jasa HEN PS4?",
     "Instalasi sistem HEN, setting dan tes game lengkap, serta panduan pemakaian sampai paham."),
    ("Kapan sebaiknya ganti pasta thermal?",
     "Jika kipas makin bising, mesin cepat panas, atau game mulai patah-patah dan konsol mati sendiri."),
    ("Bagaimana cara order?",
     "Lewat tab Booking Servis, tombol WhatsApp, atau Shopee Store. Datang langsung ke workshop juga bisa pada jam buka."),
]

TROUBLESHOOT = {
    "PS4 cepat panas / kipas bising": [
        "Pastikan ventilasi belakang dan samping tidak tertutup, jarak minimal 10 cm dari dinding.",
        "Letakkan konsol di tempat datar dan tidak di dalam rak tertutup.",
        "Bersihkan debu pada lubang udara dengan blower atau vacuum dari luar.",
        "Jika masih panas atau bising, kemungkinan pasta thermal sudah kering dan perlu diganti.",
    ],
    "Stik drift (kursor bergerak sendiri)": [
        "Masuk Settings > Devices > Controllers dan cek apakah gerakan muncul tanpa disentuh.",
        "Matikan stik, lepas dari charger, lalu tekan tombol reset kecil di bagian belakang stik.",
        "Bersihkan area sekitar analog dengan isopropil alkohol.",
        "Jika masih drift, modul analog biasanya perlu diganti lewat Servis Stik.",
    ],
    "Stik tidak mau connect / cepat habis": [
        "Pakai kabel USB yang bagus, sambungkan ke konsol, lalu tekan tombol PS.",
        "Lakukan reset stik dengan jarum pada lubang reset di belakang.",
        "Baterai yang drop cepat biasanya perlu diganti.",
    ],
    "Konsol mati sendiri saat main": [
        "Cek suhu dan ventilasi lebih dulu.",
        "Coba kabel power lain dan stop kontak lain.",
        "Jika berulang, bawa untuk dicek: bisa karena panas berlebih atau masalah power supply.",
    ],
    "Download / loading game lambat": [
        "Cek ruang penyimpanan, kosongkan jika hampir penuh.",
        "Gunakan kabel LAN, bukan Wi-Fi, untuk download.",
        "HDD lama yang sudah melambat bisa diganti SSD atau HDD baru.",
    ],
}

# =====================================================================
# KOMPONEN HALAMAN
# =====================================================================
def render_header():
    col_h1, col_h2, col_h3 = st.columns([1.2, 3, 1.2])
    with col_h1:
        st.markdown('<p class="cursive-title">Good Games<br>Better Days</p>', unsafe_allow_html=True)
    with col_h2:
        logo_base64 = None
        for filename in ["logo.png", "logo.jpg", "logo.jpeg"]:
            if os.path.exists(filename):
                logo_base64 = get_image_base64(filename)
                break
        title_html = (
            f'<img src="data:image/png;base64,{logo_base64}" class="brand-logo-img" alt="MEDY5TATION Logo">'
            if logo_base64
            else '<h1 class="brand-title">MEDY<b>5</b>TATION</h1>'
        )
        html_block(
            f'<div class="brand-container">{CONTROLLER_SVG}{title_html}'
            '<div class="brand-subtitle">PLAY MORE • GAME TOGETHER</div></div>'
        )
    with col_h3:
        st.markdown(
            '''
            <div style="text-align: right; color: #94a3b8; font-size: 0.85rem; margin-bottom: 8px;">
                <b>PS4 &bull; PS3 &bull; SWITCH &bull; ANDROID</b>
            </div>
            <p class="cursive-subtitle">Game<br>Tanpa<br>Batas</p>
            ''',
            unsafe_allow_html=True,
        )

    is_open, t = store_status()
    cls, label = ("status-open", f"Buka sekarang · tutup {CLOSE_HOUR}:00 WIB") if is_open else (
        "status-closed", f"Tutup · buka {OPEN_HOUR}:00 WIB")
    html_block(
        f'<div style="text-align:center; margin-bottom:16px;">'
        f'<span class="status-pill {cls}"><span class="dot"></span>{label}</span></div>'
    )


def render_feature_bar():
    html_block('''
        <div class="feature-bar">
            <div class="feature-item"><i class="bi bi-disc" style="font-size:1.5rem;color:#ff2a6d;"></i><span>GAME ORIGINAL</span></div>
            <div class="feature-item"><i class="bi bi-cloud-arrow-down" style="font-size:1.5rem;color:#05d9e8;"></i><span>PATCH SUB INDO</span></div>
            <div class="feature-item"><i class="bi bi-device-hdd" style="font-size:1.5rem;color:#a855f7;"></i><span>HDD FULL GAME</span></div>
            <div class="feature-item"><i class="bi bi-gear-wide-connected" style="font-size:1.5rem;color:#f59e0b;"></i><span>INSTAL LANGSUNG</span></div>
            <div class="feature-item"><i class="bi bi-shield-check" style="font-size:1.5rem;color:#10b981;"></i><span>AMAN &amp; TERPERCAYA</span></div>
        </div>
    ''')


def tab_paket():
    st.write("")
    p1, p2, p3 = st.columns(3)
    with p1:
        html_block('''
            <div class="card-box border-cyan" style="text-align:center;">
                <i class="bi bi-play-circle" style="font-size:2.2rem;color:#05d9e8;"></i>
                <div style="font-size:.95rem;font-weight:700;margin-top:10px;">VIA DRIVE</div>
                <div class="price-badge-cyan">15K</div>
                <small style="color:#94a3b8;font-weight:600;">PER GAME</small>
                <p style="font-size:.8rem;color:#94a3b8;margin-top:16px;">Patch Sub Indo &amp; Link Download sesuai CUSA game</p>
            </div>''')
    with p2:
        html_block('''
            <div class="card-box border-pink" style="text-align:center;">
                <i class="bi bi-box-arrow-in-down" style="font-size:2.2rem;color:#ff2a6d;"></i>
                <div style="font-size:.95rem;font-weight:700;margin-top:10px;">PKG &amp; INSTAL DI PS</div>
                <div class="price-badge-pink">25K</div>
                <small style="color:#94a3b8;font-weight:600;">PER GAME</small>
                <div class="promo-banner">PROMO: 3 GAME 65K</div>
                <small style="color:#94a3b8;display:block;margin-top:10px;">Lokasi Palembang</small>
            </div>''')
    with p3:
        html_block('''
            <div class="card-box border-purple" style="text-align:center;">
                <i class="bi bi-hdd-network" style="font-size:2.2rem;color:#a855f7;"></i>
                <div style="font-size:.95rem;font-weight:700;margin-top:10px;">HDD FULL GAME (PKG/PNP)</div>
                <div style="display:flex;justify-content:space-around;margin-top:12px;">
                    <div><span style="background:#fff;color:#0b0f19;padding:2px 8px;border-radius:4px;font-size:.75rem;font-weight:800;">500GB</span>
                    <div class="price-badge-purple" style="margin-top:4px;">350RB</div></div>
                    <div><span style="background:#fff;color:#0b0f19;padding:2px 8px;border-radius:4px;font-size:.75rem;font-weight:800;">1TB</span>
                    <div class="price-badge-purple" style="margin-top:4px;">550RB</div></div>
                </div>
                <small style="color:#94a3b8;display:block;margin-top:16px;">Plug and Play / Siap Main</small>
            </div>''')

    st.write("")
    s1, s2, s3 = st.columns(3)
    with s1:
        html_block('''
            <div class="card-box border-cyan">
                <i class="bi bi-cpu" style="font-size:1.8rem;color:#05d9e8;"></i>
                <div style="font-size:.95rem;font-weight:700;margin-top:8px;">JASA HEN PS4</div>
                <div class="price-badge-cyan">50K</div>
                <ul style="font-size:.82rem;padding-left:18px;margin:10px 0 0 0;color:#cbd5e1;line-height:1.6;">
                    <li>Install Sistem HEN</li><li>Setting &amp; Tes Game Lengkap</li><li>Panduan Pemakaian Sampai Paham</li>
                </ul>
            </div>''')
    with s2:
        html_block('''
            <div class="card-box border-pink">
                <i class="bi bi-thermometer-half" style="font-size:1.8rem;color:#ff2a6d;"></i>
                <div style="font-size:.95rem;font-weight:700;margin-top:8px;">GANTI PASTA THERMAL</div>
                <div class="price-badge-pink">250RB</div>
                <ul style="font-size:.82rem;padding-left:18px;margin:10px 0 0 0;color:#cbd5e1;line-height:1.6;">
                    <li>Deep Cleaning / Pembersihan Debu Mesin</li><li>Aplikasi Thermal Paste Premium Berkualitas</li><li>Meredam Kipas Bising &amp; Mengatasi Overheat</li>
                </ul>
            </div>''')
    with s3:
        html_block('''
            <div class="card-box border-purple">
                <i class="bi bi-joystick" style="font-size:1.8rem;color:#a855f7;"></i>
                <div style="font-size:.95rem;font-weight:700;margin-top:8px;">SERVIS STIK PS4</div>
                <div class="price-badge-purple" style="margin-bottom:6px;">KONSULTASI</div>
                <ul style="font-size:.82rem;padding-left:18px;margin:6px 0 0 0;color:#cbd5e1;line-height:1.6;">
                    <li>Perbaikan Analog Drift / Tidak Stabil</li><li>Tombol Keras atau Tidak Responsif</li><li>Ganti Part / Jalur / Cleaning</li><li>Kustomisasi &amp; Upgrade Mod</li>
                </ul>
            </div>''')


def tab_games():
    st.write("")
    c1, c2 = st.columns([3, 1])
    with c1:
        q = st.text_input("🔍 Cari Judul Game Patch Bahasa Indonesia:",
                          placeholder="Contoh: God of War, Spiderman, Resident Evil...")
    with c2:
        sort_mode = st.selectbox("Urutkan", ["Sesuai daftar", "A → Z", "Z → A"])

    items = [(i + 1, g) for i, g in enumerate(PS4_GAMES)]
    if q:
        items = [(n, g) for n, g in items if q.lower() in g.lower()]
    if sort_mode == "A → Z":
        items.sort(key=lambda x: x[1].lower())
    elif sort_mode == "Z → A":
        items.sort(key=lambda x: x[1].lower(), reverse=True)

    st.caption(f"Menampilkan {len(items)} dari {len(PS4_GAMES)} judul")
    if not items:
        st.info("Game yang dicari belum tersedia. Tanyakan lewat WhatsApp, siapa tahu bisa dicarikan.")
        st.link_button("Tanya via WhatsApp", wa_link(f"Halo MEDY5TATION, apakah ada game: {q}?"))
        return

    cols = st.columns(4)
    chunk = (len(items) + 3) // 4
    for ci, col in enumerate(cols):
        with col:
            for n, g in items[ci * chunk:(ci + 1) * chunk]:
                html_block(f'''
                    <div class="game-badge"><span class="game-num">#{n}</span>
                    <span style="color:#fff;font-weight:500;">{html.escape(g)}</span></div>''')


def _list_card(title, icon, color_cls, color, rows):
    items = "".join(
        f'<div class="list-item-dark"><b style="color:{color};">{i + 1}.</b> {html.escape(r)}</div>'
        for i, r in enumerate(rows)
    )
    html_block(f'''
        <div class="card-box {color_cls}">
            <div style="font-size:1.05rem;font-weight:700;color:{color};margin-bottom:15px;">
                <i class="bi {icon}"></i> {title}
            </div>{items}
        </div>''')


def tab_bola():
    st.write("")
    b1, b2 = st.columns(2)
    with b1:
        _list_card("UPDATE BOLA PS4 HEN (SUMMER 2027)", "bi-dribbble", "border-pink", "#ff2a6d", PS4_HEN_UPDATES)
    with b2:
        _list_card("UPDATE BOLA PS3", "bi-dribbble", "border-cyan", "#05d9e8", PS3_BOLA_UPDATES)


def tab_extra():
    st.write("")
    e1, e2 = st.columns(2)
    with e1:
        _list_card("ANDROID APPS &amp; STREAMING", "bi-android2", "border-green", "#10b981", ANDROID_SERVICES)
    with e2:
        _list_card("NINTENDO SWITCH SUB INDO", "bi-nintendo-switch", "border-pink", "#ff2a6d", SWITCH_GAMES)


# ---------------- Kalkulator Biaya ----------------
def tab_kalkulator():
    st.write("")
    st.subheader("🧮 Kalkulator Biaya Servis")
    st.caption("Hitung estimasi biaya layanan, lalu kirim rinciannya ke WhatsApp.")
    left, right = st.columns([2, 1])
    with left:
        lines = []
        for name, price in SERVICES.items():
            c1, c2 = st.columns([3, 1])
            with c1:
                use = st.checkbox(f"{name} · {rupiah(price)}", key=f"calc_{name}")
            with c2:
                qty = st.number_input("Jumlah", 1, 10, 1, key=f"qty_{name}", label_visibility="collapsed",
                                      disabled=not use)
            if use:
                lines.append((name, qty, price))
        stik_qty = st.number_input("Servis stik (harga konsultasi, tidak dihitung)", 0, 10, 0)
        if stik_qty:
            st.info("Servis stik dihargai setelah dicek. Rinciannya akan ikut di pesan WhatsApp.")

    total = sum(q * p for _, q, p in lines)
    with right:
        html_block(f'''
            <div class="total-box"><small style="color:#94a3b8;">ESTIMASI TOTAL</small>
            <div class="amount">{rupiah(total)}</div></div>''')
        if lines or stik_qty:
            msg = "Halo MEDY5TATION, saya mau order:\n"
            for n, q, p in lines:
                msg += f"- {n} x{q} = {rupiah(q * p)}\n"
            if stik_qty:
                msg += f"- Servis Stik PS4 x{stik_qty} (konsultasi)\n"
            msg += f"Total estimasi: {rupiah(total)}"
            st.link_button("Kirim ke WhatsApp", wa_link(msg), use_container_width=True)
        else:
            st.caption("Pilih layanan di sebelah kiri.")


# ---------------- Booking Servis ----------------
def tab_booking():
    st.write("")
    st.subheader("🔧 Booking Servis")
    st.caption("Isi data unit kamu. Kamu akan mendapat kode tiket untuk memantau progres.")
    with st.form("booking_form", clear_on_submit=True):
        c1, c2 = st.columns(2)
        with c1:
            nama = st.text_input("Nama *")
            wa = st.text_input("Nomor WhatsApp *", placeholder="08xxxxxxxxxx")
            perangkat = st.selectbox("Perangkat", ["PS4", "PS4 Slim", "PS4 Pro", "PS3", "Stik PS4", "Stik PS5", "Nintendo Switch", "Lainnya"])
        with c2:
            layanan = st.selectbox("Layanan", ["Jasa HEN PS4", "Ganti Pasta Thermal", "Servis Stik PS4", "Cek / Diagnosa", "Lainnya"])
            tgl = st.date_input("Rencana datang / antar", min_value=date.today())
            keluhan = st.text_area("Keluhan / catatan", placeholder="Contoh: kipas bising, mati sendiri setelah 30 menit")
        kirim = st.form_submit_button("Buat Tiket Servis")

    if kirim:
        if not nama.strip() or not wa.strip():
            st.error("Nama dan nomor WhatsApp wajib diisi.")
            return
        orders = load_json(ORDERS_FILE, {})
        code = new_ticket(orders)
        orders[code] = {
            "nama": nama.strip(), "wa": wa.strip(), "perangkat": perangkat, "layanan": layanan,
            "tanggal": str(tgl), "keluhan": keluhan.strip(), "status": STATUS_FLOW[0],
            "catatan": "", "dibuat": now().strftime("%Y-%m-%d %H:%M"),
        }
        saved = save_json(ORDERS_FILE, orders)
        st.session_state["last_ticket"] = code
        st.session_state["last_ticket_saved"] = saved
        st.session_state["last_ticket_msg"] = (
            f"Halo MEDY5TATION, saya {nama.strip()}. Booking servis {layanan} untuk {perangkat}. "
            f"Tiket: {code}. Rencana datang: {tgl}. Keluhan: {keluhan.strip() or '-'}"
        )

    if st.session_state.get("last_ticket"):
        code = st.session_state["last_ticket"]
        html_block(f'''
            <div class="card-box border-cyan" style="text-align:center;height:auto;">
                <small style="color:#94a3b8;">KODE TIKET KAMU</small>
                <div class="ticket-code">{code}</div>
                <small style="color:#94a3b8;">Simpan kode ini untuk cek status di tab Cek Status.</small>
            </div>''')
        if not st.session_state.get("last_ticket_saved"):
            st.warning("Tiket belum bisa disimpan di server. Kirim lewat WhatsApp agar tercatat.")
        st.link_button("Konfirmasi lewat WhatsApp", wa_link(st.session_state["last_ticket_msg"]))


# ---------------- Cek Status ----------------
def tab_status():
    st.write("")
    st.subheader("🔎 Cek Status Servis")
    code = st.text_input("Masukkan kode tiket", placeholder="MD-XXXXX").strip().upper()
    if not code:
        st.caption("Kode tiket diberikan setelah kamu booking servis.")
        return
    orders = load_json(ORDERS_FILE, {})
    o = orders.get(code)
    if not o:
        st.error("Kode tiket tidak ditemukan. Periksa lagi penulisannya atau hubungi kami lewat WhatsApp.")
        return
    idx = STATUS_FLOW.index(o["status"]) if o["status"] in STATUS_FLOW else 0
    steps = "".join(f'<div class="step {"done" if i <= idx else ""}"></div>' for i in range(len(STATUS_FLOW)))
    note = f'<p style="color:#cbd5e1;margin:8px 0 0 0;">Catatan teknisi: {html.escape(o["catatan"])}</p>' if o.get("catatan") else ""
    html_block(f'''
        <div class="card-box border-pink" style="height:auto;">
            <small style="color:#94a3b8;">TIKET {code}</small>
            <div style="font-size:1.4rem;font-weight:800;color:#ff2a6d;">{html.escape(o["status"])}</div>
            <div class="track">{steps}</div>
            <small style="color:#94a3b8;">{idx + 1} dari {len(STATUS_FLOW)} tahap</small>
            <p style="margin:12px 0 0 0;">{html.escape(o["layanan"])} · {html.escape(o["perangkat"])}</p>
            <small style="color:#94a3b8;">Dibuat {o["dibuat"]}</small>{note}
        </div>''')
    st.link_button("Tanya progres via WhatsApp", wa_link(f"Halo MEDY5TATION, mau tanya progres tiket {code}."))


# ---------------- Bantuan ----------------
def tab_bantuan():
    st.write("")
    c1, c2 = st.columns([3, 2])
    with c1:
        st.subheader("❓ Pertanyaan Umum")
        for q, a in FAQ:
            with st.expander(q):
                st.write(a)
        st.subheader("🩺 Diagnosa Mandiri")
        masalah = st.selectbox("Pilih masalah yang kamu alami", list(TROUBLESHOOT.keys()))
        for step in TROUBLESHOOT[masalah]:
            st.markdown(f"- {step}")
        st.caption("Kalau langkah di atas belum menyelesaikan masalah, booking servis atau konsultasi lewat WhatsApp.")
    with c2:
        st.subheader("📍 Lokasi & Jam Buka")
        html_block(f'''
            <div class="card-box border-purple" style="height:auto;">
                <b><i class="bi bi-geo-alt-fill" style="color:#ff2a6d;"></i> TEGAL BINANGUN SASANA PATRA</b>
                <p style="color:#94a3b8;margin:4px 0 10px 0;">Palembang</p>
                <p style="margin:0;">Jam buka: {OPEN_HOUR}:00 – {CLOSE_HOUR}:00 WIB</p>
            </div>''')
        st.map({"lat": [STORE_LAT], "lon": [STORE_LON]}, zoom=11)
        st.caption("Titik peta perkiraan. Ubah STORE_LAT dan STORE_LON di bagian konfigurasi agar tepat.")


# ---------------- Testimoni ----------------
def tab_testimoni():
    st.write("")
    reviews = load_json(REVIEWS_FILE, [])
    st.subheader("⭐ Testimoni Pelanggan")
    if reviews:
        avg = sum(r["rating"] for r in reviews) / len(reviews)
        st.markdown(f"**{avg:.1f} / 5** dari {len(reviews)} ulasan")
    left, right = st.columns([2, 1])
    with left:
        if not reviews:
            st.info("Belum ada ulasan. Jadilah yang pertama.")
        for r in reversed(reviews[-20:]):
            stars = "★" * r["rating"] + "☆" * (5 - r["rating"])
            html_block(f'''
                <div class="review"><div class="stars">{stars}</div>
                <div>{html.escape(r["teks"])}</div>
                <small>{html.escape(r["nama"])} · {r["waktu"]}</small></div>''')
    with right:
        with st.form("review_form", clear_on_submit=True):
            nama = st.text_input("Nama")
            rating = st.slider("Rating", 1, 5, 5)
            teks = st.text_area("Ulasan", max_chars=300)
            ok = st.form_submit_button("Kirim ulasan")
        if ok:
            if not nama.strip() or not teks.strip():
                st.error("Nama dan ulasan wajib diisi.")
            else:
                reviews.append({"nama": nama.strip()[:40], "rating": rating, "teks": teks.strip(),
                                "waktu": now().strftime("%d %b %Y")})
                if save_json(REVIEWS_FILE, reviews):
                    st.success("Terima kasih atas ulasanmu.")
                    st.rerun()
                else:
                    st.error("Ulasan belum bisa disimpan di server.")


# ---------------- Admin ----------------
def tab_admin():
    st.write("")
    st.subheader("🔐 Panel Admin")
    if not st.session_state.get("is_admin"):
        pw = st.text_input("Password admin", type="password")
        if st.button("Masuk"):
            if pw == admin_password():
                st.session_state["is_admin"] = True
                st.rerun()
            else:
                st.error("Password salah.")
        st.caption("Atur password lewat ADMIN_PASSWORD di st.secrets atau environment variable.")
        return

    if st.button("Keluar admin"):
        st.session_state["is_admin"] = False
        st.rerun()

    orders = load_json(ORDERS_FILE, {})
    reviews = load_json(REVIEWS_FILE, [])

    m1, m2, m3 = st.columns(3)
    m1.metric("Total tiket", len(orders))
    m2.metric("Sedang berjalan", sum(1 for o in orders.values() if o["status"] not in STATUS_FLOW[-2:]))
    m3.metric("Ulasan", len(reviews))

    st.markdown("#### Kelola tiket")
    if not orders:
        st.info("Belum ada tiket.")
    else:
        filt = st.selectbox("Filter status", ["Semua"] + STATUS_FLOW)
        rows = [{"Tiket": k, **v} for k, v in orders.items() if filt == "Semua" or v["status"] == filt]
        st.dataframe(rows, use_container_width=True, hide_index=True)

        pick = st.selectbox("Pilih tiket", list(orders.keys()))
        o = orders[pick]
        c1, c2 = st.columns(2)
        with c1:
            new_status = st.selectbox("Status", STATUS_FLOW, index=STATUS_FLOW.index(o["status"]) if o["status"] in STATUS_FLOW else 0)
        with c2:
            new_note = st.text_input("Catatan untuk pelanggan", value=o.get("catatan", ""))
        b1, b2, b3 = st.columns(3)
        if b1.button("Simpan perubahan"):
            orders[pick]["status"] = new_status
            orders[pick]["catatan"] = new_note
            save_json(ORDERS_FILE, orders)
            st.success("Tersimpan.")
            st.rerun()
        wa_to = "".join(ch for ch in o["wa"] if ch.isdigit())
        if wa_to.startswith("0"):
            wa_to = "62" + wa_to[1:]
        b2.link_button("Chat pelanggan", f"https://wa.me/{wa_to}?text=" + quote(
            f"Halo {o['nama']}, update servis tiket {pick}: {new_status}. {new_note}"))
        if b3.button("Hapus tiket"):
            orders.pop(pick, None)
            save_json(ORDERS_FILE, orders)
            st.rerun()

        # Ekspor CSV
        buf = io.StringIO()
        buf.write("tiket,nama,wa,perangkat,layanan,tanggal,status,catatan,dibuat,keluhan\n")
        for k, v in orders.items():
            vals = [k, v["nama"], v["wa"], v["perangkat"], v["layanan"], v["tanggal"], v["status"],
                    v.get("catatan", ""), v["dibuat"], v["keluhan"]]
            buf.write(",".join('"' + str(x).replace('"', '""') + '"' for x in vals) + "\n")
        st.download_button("Unduh semua tiket (CSV)", buf.getvalue(), "tiket_servis.csv", "text/csv")

    st.markdown("#### Moderasi ulasan")
    for i, r in enumerate(reviews):
        c1, c2 = st.columns([6, 1])
        c1.write(f"{'★' * r['rating']} {r['nama']}: {r['teks']}")
        if c2.button("Hapus", key=f"delrev_{i}"):
            reviews.pop(i)
            save_json(REVIEWS_FILE, reviews)
            st.rerun()
    st.caption("Catatan: di Streamlit Community Cloud, file data bisa hilang saat aplikasi restart. "
               "Untuk penyimpanan permanen, sambungkan ke database (misalnya Google Sheets atau Supabase).")


# ---------------- Footer ----------------
def render_footer():
    st.markdown('<hr style="border-color:#1f2937;margin:35px 0 25px 0;">', unsafe_allow_html=True)
    sec_lokasi, sec_order, sec_social = st.columns([1.5, 2, 2.5])
    with sec_lokasi:
        html_block('''
            <div style="margin-bottom:8px;">
                <small style="color:#94a3b8;letter-spacing:1px;font-weight:700;">LOKASI WORKSHOP</small>
                <div style="font-weight:800;font-size:1.25rem;margin-top:4px;">
                    <i class="bi bi-geo-alt-fill" style="color:#ff2a6d;"></i> PALEMBANG</div>
                <div style="font-size:.88rem;color:#94a3b8;margin-top:2px;">TEGAL BINANGUN SASANA PATRA</div>
            </div>''')
    with sec_order:
        html_block(f'''
            <small style="color:#94a3b8;letter-spacing:1px;font-weight:700;">ORDER &amp; STORE</small><br>
            <div style="display:flex;flex-direction:column;gap:8px;margin-top:8px;">
                <a href="{wa_link()}" target="_blank" class="social-link btn-wa"><i class="bi bi-whatsapp"></i> Chat WhatsApp</a>
                <a href="https://id.shp.ee/FdsB8oxh" target="_blank" class="social-link btn-shopee"><i class="bi bi-bag-fill"></i> Shopee Store</a>
            </div>''')
    with sec_social:
        html_block('''
            <small style="color:#94a3b8;letter-spacing:1px;font-weight:700;">SOSIAL MEDIA</small><br>
            <div style="display:grid;grid-template-columns:1fr 1fr;gap:8px;margin-top:8px;">
                <a href="https://www.tiktok.com/@xtboy?_r=1&_t=ZS-9AIx1XJuxP8" target="_blank" class="social-link btn-tiktok"><i class="bi bi-tiktok"></i> TikTok</a>
                <a href="https://www.instagram.com/m.rizkirahmady?stkn=ZGxoZjRxYWc4dWs2" target="_blank" class="social-link btn-ig"><i class="bi bi-instagram"></i> Instagram</a>
            </div>
            <a href="https://youtube.com/@medy5tation?si=UhuJ79xJ212_mUGL" target="_blank" class="social-link btn-yt"><i class="bi bi-youtube"></i> YouTube Channel</a>''')

    html_block('''
        <div style="display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:8px;margin-top:40px;padding:15px 0;border-top:1px solid #1f2937;color:#64748b;font-size:.8rem;font-weight:600;">
            <div><b>MEDY5TATION</b> &copy; ''' + str(now().year) + '''</div>
            <div>&ldquo; GAME IS ALWAYS A GOOD IDEA &rdquo;</div>
            <div style="letter-spacing:2px;color:#05d9e8;">&#9651; &#9675; &#10005; &#9633; PLAY &bull; SHARE &bull; TOGETHER</div>
        </div>
        <a class="wa-float" href="''' + wa_link("Halo MEDY5TATION, saya mau tanya.") + '''" target="_blank" aria-label="Chat WhatsApp"><i class="bi bi-whatsapp"></i></a>''')


# =====================================================================
def main():
    set_page_styling()
    render_header()
    render_feature_bar()

    tabs = st.tabs([
        "📦 Paket & Layanan",
        f"🎮 List Game Sub Indo ({len(PS4_GAMES)})",
        "⚽ Update Patch Bola",
        "📱 Android & Switch",
        "🧮 Kalkulator",
        "🔧 Booking Servis",
        "🔎 Cek Status",
        "❓ Bantuan & Lokasi",
        "⭐ Testimoni",
        "🔐 Admin",
    ])
    for tab, fn in zip(tabs, [tab_paket, tab_games, tab_bola, tab_extra, tab_kalkulator,
                              tab_booking, tab_status, tab_bantuan, tab_testimoni, tab_admin]):
        with tab:
            fn()

    render_footer()


if __name__ == "__main__":
    main()