import streamlit as st
import os
import base64
from urllib.parse import quote
 
WA_NUMBER = "6282289421650"
 
def get_image_base64(path):
    if os.path.exists(path):
        with open(path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    return None
 
def wa_link(text):
    return f"https://wa.me/{WA_NUMBER}?text={quote(text)}"
 
def set_page_styling():
    st.set_page_config(page_title="MEDY5TATION - Game Together", page_icon="🎮",
                       layout="wide", initial_sidebar_state="collapsed")
    st.markdown('<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css">', unsafe_allow_html=True)
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Kanit:wght@300;400;600;700;800&family=Satisfy&display=swap');
    :root{
        --navy-1:#0a2a5e;   /* layer luar */
        --navy-2:#0f3a7a;   /* layer tengah */
        --navy-3:#164a94;   /* layer dalam / item */
        --line:#1e4fa3;
        --accent:#38bdf8;
        --pink:#e0115f;
    }
    .stApp{background:#ffffff !important;color:#0f172a !important;font-family:'Kanit',sans-serif !important;}
    .brand-container{text-align:center;padding:5px 0;}
    .brand-logo-img{max-width:210px;width:100%;height:auto;border-radius:12px;display:block;margin:0 auto;}
    .cursive-title{font-family:'Satisfy',cursive !important;color:var(--pink) !important;font-size:2.8rem;line-height:1.1;margin:0;}
    .cursive-subtitle{font-family:'Satisfy',cursive !important;color:#002d72 !important;font-size:2.2rem;line-height:1.1;margin:0;text-align:right;}
    .brand-subtitle{font-size:.95rem;letter-spacing:4px;color:#64748b;margin:8px 0 20px;font-weight:700;}
 
    /* ===== LAYER BOX BIRU TUA (3 lapis) ===== */
    .layer-outer{background:var(--navy-1);border:1.5px solid var(--line);border-radius:18px;padding:10px;
        box-shadow:0 6px 18px rgba(10,42,94,.25);margin-bottom:14px;}
    .layer-inner{background:var(--navy-2);border:1px solid var(--line);border-radius:12px;padding:14px;}
    .layer-title{color:var(--accent);font-weight:700;font-size:1.05rem;text-transform:uppercase;
        letter-spacing:.5px;margin:0 0 12px;display:flex;align-items:center;gap:8px;}
    .list-item-box{background:var(--navy-3);border:1px solid #2a63b8;padding:10px 14px;border-radius:8px;
        margin-bottom:8px;font-size:.9rem;color:#fff;display:flex;align-items:center;gap:10px;transition:all .15s;}
    .list-item-box:hover{border-color:var(--accent);transform:translateX(3px);}
    .item-no{color:var(--accent);font-weight:800;min-width:26px;}
    .item-tag{margin-left:auto;background:rgba(56,189,248,.18);color:#bae6fd;font-size:.7rem;
        padding:2px 8px;border-radius:20px;font-weight:600;}
 
    /* Feature bar */
    .feature-bar{display:flex;justify-content:space-around;text-align:center;margin-bottom:25px;flex-wrap:wrap;gap:12px;
        background:var(--navy-1);border:1.5px solid var(--line);border-radius:16px;padding:12px;}
    .feature-item{display:flex;flex-direction:column;align-items:center;gap:4px;color:#f1f5f9;font-weight:600;
        background:var(--navy-2);border:1px solid var(--line);border-radius:10px;padding:10px 16px;min-width:130px;}
 
    /* ===== NAVIGASI TAB: layer luar + box tiap tab ===== */
    [data-testid="stTabs"] div[data-baseweb="tab-list"]{
        gap:10px !important;justify-content:center !important;flex-wrap:wrap;
        background:var(--navy-1) !important;border:1.5px solid var(--line) !important;
        border-radius:16px !important;padding:10px !important;
        box-shadow:0 6px 18px rgba(10,42,94,.25);margin-bottom:18px;}
    [data-testid="stTabs"] div[data-baseweb="tab"]{
        border-radius:10px !important;padding:10px 22px !important;height:auto !important;
        background:var(--navy-2) !important;border:1.5px solid var(--line) !important;transition:all .2s !important;}
    [data-testid="stTabs"] div[data-baseweb="tab"] p,[data-testid="stTabs"] div[data-baseweb="tab"] span{
        color:#fff !important;font-weight:700 !important;font-size:.95rem !important;}
    [data-testid="stTabs"] div[data-baseweb="tab"]:hover{background:var(--navy-3) !important;border-color:var(--accent) !important;transform:translateY(-2px);}
    [data-testid="stTabs"] div[data-baseweb="tab"][aria-selected="true"]{background:var(--pink) !important;border-color:var(--pink) !important;}
    [data-testid="stTabs"] div[data-baseweb="tab-highlight"],[data-testid="stTabs"] div[data-baseweb="tab-border"]{background:transparent !important;}
 
    /* Kartu paket */
    .card-box{border-radius:12px;padding:20px;margin-bottom:15px;height:100%;background:var(--navy-2);color:#fff;
        border:1.5px solid var(--line);box-shadow:0 6px 16px rgba(10,42,94,.18);transition:transform .2s;}
    .card-box:hover{transform:translateY(-3px);}
    .card-featured{border:1.5px solid var(--pink);}
    .price-badge{color:#ff6b95;font-size:2.3rem;font-weight:800;line-height:1;}
    .service-title{color:var(--accent);font-size:1rem;font-weight:700;text-transform:uppercase;margin:8px 0;}
    .game-badge{background:var(--navy-3);border:1px solid #2a63b8;border-radius:8px;padding:9px 12px;margin-bottom:8px;
        font-size:.85rem;display:flex;align-items:center;gap:8px;transition:all .15s;}
    .game-badge:hover{border-color:var(--accent);transform:scale(1.02);}
    .game-num{color:var(--accent);font-weight:800;min-width:28px;}
 
    /* Tombol sosial (tanpa hitam) */
    .social-link{display:inline-flex;align-items:center;justify-content:center;gap:8px;padding:10px 16px;border-radius:8px;
        font-weight:600;text-decoration:none !important;font-size:.9rem;margin-bottom:8px;width:100%;color:#fff !important;}
    .btn-wa{background:#25D366;} .btn-shopee{background:#EE4D2D;}
    .btn-tiktok{background:var(--navy-1);border:1px solid var(--line);}
    .btn-ig{background:linear-gradient(45deg,#f09433,#dc2743,#bc1888);} .btn-yt{background:#FF0000;}
 
    /* Tombol WA melayang */
    .wa-float{position:fixed;right:22px;bottom:22px;z-index:999;background:#25D366;color:#fff !important;
        width:56px;height:56px;border-radius:50%;display:flex;align-items:center;justify-content:center;
        font-size:1.8rem;box-shadow:0 6px 16px rgba(0,0,0,.25);text-decoration:none !important;}
    /* Input & expander biru tua */
    [data-testid="stExpander"]{background:var(--navy-1);border:1.5px solid var(--line);border-radius:12px;}
    [data-testid="stExpander"] summary p{color:#fff !important;font-weight:600;}
    [data-testid="stExpander"] div[data-testid="stMarkdownContainer"] p{color:#e2e8f0;}
    [data-testid="stMetric"]{background:var(--navy-1);border:1.5px solid var(--line);border-radius:12px;padding:12px 16px;}
    [data-testid="stMetricLabel"] p{color:var(--accent) !important;}
    [data-testid="stMetricValue"]{color:#fff !important;}
    </style>""", unsafe_allow_html=True)
 
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
PS4_HEN_UPDATES = ["Monster patch summer 2027", "Eleven Patch summer 2027 Final Update",
                   "Bitbox patch summer 2027", "Leader patch summer 2027", "monster 2018 patch summer 2027"]
PS3_BOLA_UPDATES = ["Bitbox patch", "Vr patch"]
ANDROID_SERVICES = ["Spotify mod premium", "Netflix (Nonton film gabungan vidio viu dkk)"]
SWITCH_GAMES = ["DREDGE", "STRAY", "RDR", "Zelda BOTW"]
 
def layered_box(title, icon, items, accent="#38bdf8", tag="Tersedia"):
    """Box 3 lapis biru tua: luar > tengah > item."""
    rows = "".join(
        f'<div class="list-item-box"><span class="item-no" style="color:{accent};">{i+1}.</span>'
        f'<span>{it}</span><span class="item-tag">{tag}</span></div>'
        for i, it in enumerate(items))
    if not items:
        rows = '<div class="list-item-box">Tidak ada hasil.</div>'
    return (f'<div class="layer-outer"><div class="layer-inner">'
            f'<div class="layer-title" style="color:{accent};"><i class="bi {icon}"></i> {title}</div>'
            f'{rows}</div></div>')
 
def filter_list(items, q):
    return [x for x in items if q.lower() in x.lower()] if q else items
 
def hitung_pkg(n):
    """25K/game, paket 3 game = 65K."""
    return (n // 3) * 65000 + (n % 3) * 25000
 
def rupiah(n):
    return "Rp " + f"{n:,}".replace(",", ".")
 
def main():
    set_page_styling()
 
    # Tombol WhatsApp melayang
    st.markdown(f'<a class="wa-float" href="{wa_link("Halo Medy5tation, saya mau tanya layanan")}" target="_blank"><i class="bi bi-whatsapp"></i></a>', unsafe_allow_html=True)
 
    # HEADER
    c1, c2, c3 = st.columns([1.2, 3, 1.2])
    with c1:
        st.markdown('<p class="cursive-title">Good Games<br>Better Days</p>', unsafe_allow_html=True)
    with c2:
        logo = None
        for fn in ["logo.png", "logo.jpg", "logo.jpeg"]:
            if os.path.exists(fn):
                logo = get_image_base64(fn); break
        if logo:
            st.markdown(f'<div class="brand-container"><img src="data:image/png;base64,{logo}" class="brand-logo-img"><div class="brand-subtitle">PLAY MORE • GAME TOGETHER</div></div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="brand-container"><i class="bi bi-controller" style="font-size:3.2rem;color:#0a2a5e;"></i><h1 style="letter-spacing:4px;margin:0;font-size:3rem;color:#0a2a5e;">MEDY5TATION</h1><div class="brand-subtitle">PLAY MORE • GAME TOGETHER</div></div>', unsafe_allow_html=True)
    with c3:
        st.markdown('<div style="text-align:right;color:#002d72;font-size:.85rem;margin-bottom:8px;"><b>PS4 &bull; PS3 &bull; SWITCH &bull; ANDROID</b></div><p class="cursive-subtitle">Game<br>Tanpa<br>Batas</p>', unsafe_allow_html=True)
 
    # FITUR UTAMA
    feats = [("bi-disc","GAME ORIGINAL"),("bi-cloud-arrow-down","PATCH SUB INDO"),("bi-device-hdd","HDD FULL GAME"),
             ("bi-gear-wide-connected","INSTAL LANGSUNG"),("bi-shield-check","AMAN & TERPERCAYA")]
    st.markdown('<div class="feature-bar">' + "".join(
        f'<div class="feature-item"><i class="bi {i}" style="font-size:1.6rem;color:#38bdf8;"></i><small>{t}</small></div>'
        for i, t in feats) + '</div>', unsafe_allow_html=True)
 
    # STATISTIK
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Game PS4 Sub Indo", len(PS4_GAMES))
    m2.metric("Patch Bola PS4", len(PS4_HEN_UPDATES))
    m3.metric("Game Switch", len(SWITCH_GAMES))
    m4.metric("Layanan Android", len(ANDROID_SERVICES))
    st.write("")
 
    tab_home, tab_games, tab_calc, tab_bola, tab_extra = st.tabs([
        "🏠 Paket & Layanan", f"🎮 List Game ({len(PS4_GAMES)})",
        "🛒 Kalkulator Order", "⚽ Update Patch Bola", "📱 Android & Switch"])
 
    # TAB 1
    with tab_home:
        p1, p2, p3 = st.columns([1.8, 2.2, 2.2])
        with p1:
            st.markdown('<div class="card-box card-featured" style="text-align:center;"><i class="bi bi-google-play" style="font-size:2rem;color:#38bdf8;"></i><div class="service-title">VIA DRIVE</div><div class="price-badge">15K</div><small style="color:#bae6fd;">PER GAME</small><p style="font-size:.82rem;color:#e2e8f0;margin-top:12px;">Patch Sub Indo & Link Download sesuai CUSA game</p></div>', unsafe_allow_html=True)
        with p2:
            st.markdown('<div class="card-box card-featured" style="text-align:center;"><i class="bi bi-box-arrow-in-down" style="font-size:2rem;color:#38bdf8;"></i><div class="service-title">PKG & INSTAL DI PS</div><div class="price-badge">25K</div><small style="color:#bae6fd;">PER GAME</small><div style="margin-top:10px;background:#e0115f;padding:6px;border-radius:6px;font-weight:700;font-size:.85rem;color:white;">3 GAME 65K</div><small style="color:#e2e8f0;display:block;margin-top:8px;">Lokasi Palembang</small></div>', unsafe_allow_html=True)
        with p3:
            st.markdown('<div class="card-box card-featured" style="text-align:center;"><i class="bi bi-hdd-network" style="font-size:2rem;color:#38bdf8;"></i><div class="service-title">HDD FULL GAME (PKG/PNP)</div><div style="display:flex;justify-content:space-around;margin-top:10px;"><div><span style="background:white;color:#0a2a5e;padding:3px 8px;border-radius:4px;font-size:.75rem;font-weight:bold;">500GB</span><div style="color:#ff6b95;font-size:1.6rem;font-weight:800;margin-top:4px;">350RB</div></div><div><span style="background:white;color:#0a2a5e;padding:3px 8px;border-radius:4px;font-size:.75rem;font-weight:bold;">1TB</span><div style="color:#ff6b95;font-size:1.6rem;font-weight:800;margin-top:4px;">550RB</div></div></div><small style="color:#e2e8f0;display:block;margin-top:10px;">Plug and Play / Siap Main</small></div>', unsafe_allow_html=True)
 
        st.write("")
        s1, s2, s3 = st.columns(3)
        ul = 'style="font-size:.82rem;padding-left:18px;margin:10px 0 0;color:#e2e8f0;line-height:1.6;"'
        with s1:
            st.markdown(f'<div class="card-box"><i class="bi bi-cpu" style="font-size:1.8rem;color:#38bdf8;"></i><div class="service-title">JASA HEN PS4</div><div class="price-badge">50K</div><ul {ul}><li>Install Sistem HEN</li><li>Setting & Tes Game Lengkap</li><li>Panduan Pemakaian Sampai Paham</li></ul></div>', unsafe_allow_html=True)
        with s2:
            st.markdown(f'<div class="card-box"><i class="bi bi-thermometer-half" style="font-size:1.8rem;color:#38bdf8;"></i><div class="service-title">GANTI PASTA THERMAL</div><div class="price-badge">250RB</div><ul {ul}><li>Deep Cleaning / Pembersihan Debu Mesin</li><li>Aplikasi Thermal Paste Premium</li><li>Meredam Kipas Bising & Overheat</li></ul></div>', unsafe_allow_html=True)
        with s3:
            st.markdown(f'<div class="card-box"><i class="bi bi-joystick" style="font-size:1.8rem;color:#38bdf8;"></i><div class="service-title">SERVIS STIK PS4</div><div class="price-badge" style="font-size:1.6rem;">KONSULTASI</div><ul {ul}><li>Perbaikan Analog Drift</li><li>Tombol Keras / Tidak Responsif</li><li>Ganti Part / Jalur / Cleaning</li><li>Kustomisasi & Upgrade Mod</li></ul></div>', unsafe_allow_html=True)
 
        st.write("")
        st.markdown("##### ❓ Pertanyaan yang Sering Ditanyakan")
        with st.expander("Apa bedanya Via Drive dan PKG & Instal di PS?"):
            st.write("Via Drive: kamu dapat patch & link download, install sendiri. PKG & Instal: game langsung dipasang di PS4 kamu (lokasi Palembang).")
        with st.expander("PS4 saya harus sudah HEN?"):
            st.write("Ya, untuk game PKG konsol perlu sistem HEN. Belum punya? Gunakan Jasa HEN PS4 (50K).")
        with st.expander("Bagaimana cara order?"):
            st.write("Pilih game di tab **Kalkulator Order**, lalu klik tombol kirim ke WhatsApp.")
 
    # TAB 2: LIST GAME
    with tab_games:
        q = st.text_input("🔍 Cari Judul Game Patch Bahasa Indonesia:", placeholder="Contoh: God of War, Spiderman, Resident Evil...")
        sort_az = st.toggle("Urutkan A–Z", value=False)
        games = filter_list(PS4_GAMES, q)
        if sort_az:
            games = sorted(games, key=str.lower)
        st.caption(f"Menampilkan {len(games)} dari {len(PS4_GAMES)} game")
        if not games:
            st.info("Game yang dicari belum tersedia. Hubungi kami via WhatsApp untuk request!")
            st.markdown(f'<a href="{wa_link("Halo, saya request game: " + q)}" target="_blank" class="social-link btn-wa" style="max-width:260px;"><i class="bi bi-whatsapp"></i> Request Game</a>', unsafe_allow_html=True)
        else:
            cols = st.columns(4)
            chunk = (len(games) + 3) // 4
            for ci, col in enumerate(cols):
                with col:
                    for g in games[ci*chunk:(ci+1)*chunk]:
                        no = PS4_GAMES.index(g) + 1
                        st.markdown(f'<div class="game-badge"><span class="game-num">#{no}</span><span style="color:#fff;font-weight:500;">{g}</span></div>', unsafe_allow_html=True)
 
    # TAB 3: KALKULATOR ORDER
    with tab_calc:
        st.markdown('<div class="layer-outer"><div class="layer-inner"><div class="layer-title"><i class="bi bi-cart3"></i> Pilih Game & Hitung Total</div></div></div>', unsafe_allow_html=True)
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
 
    # TAB 4: BOLA
    with tab_bola:
        qb = st.text_input("🔍 Cari patch bola:", key="qb", placeholder="Contoh: Monster, Bitbox...")
        b1, b2 = st.columns(2)
        with b1:
            st.markdown(layered_box("Update Bola PS4 HEN (Summer 2027)", "bi-dribbble", filter_list(PS4_HEN_UPDATES, qb), tag="Terbaru"), unsafe_allow_html=True)
        with b2:
            st.markdown(layered_box("Update Bola PS3", "bi-dribbble", filter_list(PS3_BOLA_UPDATES, qb)), unsafe_allow_html=True)
        st.markdown(f'<a href="{wa_link("Halo, saya mau order update patch bola")}" target="_blank" class="social-link btn-wa" style="max-width:300px;"><i class="bi bi-whatsapp"></i> Order Patch Bola</a>', unsafe_allow_html=True)
 
    # TAB 5: ANDROID & SWITCH
    with tab_extra:
        qe = st.text_input("🔍 Cari layanan / game:", key="qe", placeholder="Contoh: Spotify, Zelda...")
        e1, e2 = st.columns(2)
        with e1:
            st.markdown(layered_box("Android Apps & Streaming", "bi-android2", filter_list(ANDROID_SERVICES, qe), accent="#34d399", tag="Aktif"), unsafe_allow_html=True)
        with e2:
            st.markdown(layered_box("Nintendo Switch Sub Indo", "bi-nintendo-switch", filter_list(SWITCH_GAMES, qe), accent="#ff6b95"), unsafe_allow_html=True)
        st.markdown(f'<a href="{wa_link("Halo, saya mau order layanan Android/Switch")}" target="_blank" class="social-link btn-wa" style="max-width:300px;"><i class="bi bi-whatsapp"></i> Order Android / Switch</a>', unsafe_allow_html=True)
 
    # FOOTER
    st.markdown('<hr style="border-color:#e2e8f0;margin:35px 0 25px;">', unsafe_allow_html=True)
    f1, f2, f3 = st.columns([1.5, 2, 2.5])
    with f1:
        st.markdown('<small style="color:#64748b;letter-spacing:1px;font-weight:700;">LOKASI WORKSHOP</small><div style="font-weight:800;font-size:1.25rem;color:#0a2a5e;margin-top:4px;"><i class="bi bi-geo-alt-fill" style="color:#e0115f;"></i> PALEMBANG</div><div style="font-size:.88rem;color:#475569;">TEGAL BINANGUN SASANA PATRA</div>', unsafe_allow_html=True)
    with f2:
        st.markdown(f'<small style="color:#64748b;letter-spacing:1px;font-weight:700;">ORDER & STORE</small><div style="display:flex;flex-direction:column;gap:8px;margin-top:8px;"><a href="{wa_link("Halo Medy5tation")}" target="_blank" class="social-link btn-wa"><i class="bi bi-whatsapp"></i> Chat WhatsApp</a><a href="https://id.shp.ee/FdsB8oxh" target="_blank" class="social-link btn-shopee"><i class="bi bi-bag-fill"></i> Shopee Store</a></div>', unsafe_allow_html=True)
    with f3:
        st.markdown('<small style="color:#64748b;letter-spacing:1px;font-weight:700;">SOSIAL MEDIA</small><div style="display:grid;grid-template-columns:1fr 1fr;gap:8px;margin-top:8px;"><a href="https://www.tiktok.com/@xtboy?_r=1&_t=ZS-9AIx1XJuxP8" target="_blank" class="social-link btn-tiktok"><i class="bi bi-tiktok"></i> TikTok</a><a href="https://www.instagram.com/m.rizkirahmady?stkn=ZGxoZjRxYWc4dWs2" target="_blank" class="social-link btn-ig"><i class="bi bi-instagram"></i> Instagram</a></div><a href="https://youtube.com/@medy5tation?si=UhuJ79xJ212_mUGL" target="_blank" class="social-link btn-yt"><i class="bi bi-youtube"></i> YouTube Channel</a>', unsafe_allow_html=True)
 
    st.markdown('<div style="display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:8px;margin-top:40px;padding:15px 0;border-top:1px solid #e2e8f0;color:#64748b;font-size:.8rem;font-weight:600;"><div><b>MEDY5TATION</b></div><div>&ldquo; GAME IS ALWAYS A GOOD IDEA &rdquo;</div><div style="letter-spacing:2px;color:#002d72;">&#9651; &#9675; &#10005; &#9633; PLAY &bull; SHARE &bull; TOGETHER</div></div>', unsafe_allow_html=True)
 
if __name__ == "__main__":
    main()