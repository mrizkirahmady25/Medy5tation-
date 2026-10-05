import streamlit as st

# -- STYLING CONFIGURATION (TO MATCH THE IMAGE THEME) --

# Colors and Fonts
THEME = {
    "bg_color": "#0d1117",  # Very dark blue/black background
    "main_text": "#ffffff",  # White
    "accent_red": "#e0115f", # Hot red for prices/highlights
    "light_gray": "#b0b0b0",  # Lighter gray for subtext
    "card_bg": "#161b22",     # Darker box background
    "font_main": "Kanit",      # Clean modern sans-serif
    "font_accent": "Satisfy", # For the cursive titles
}

def set_dark_mode():
    st.set_page_config(
        page_title="MEDY5TATION - Game Together",
        page_icon="🎮",
        layout="wide",
        initial_sidebar_state="collapsed",
    )
    # Inject Custom CSS
    st.markdown(f"""
        <style>
        /* Load Fonts from Google */
        @import url('https://fonts.googleapis.com/css2?family=Kanit:wght@400;700&family=Satisfy&display=swap');

        /* Main Page Styling */
        .main {{
            background-color: {THEME['bg_color']};
            color: {THEME['main_text']};
            font-family: '{THEME['font_main']}', sans-serif;
        }}
        
        /* Custom Container Styles */
        [data-testid="stVerticalBlock"] > div:has(div.box) {{
            background-color: {THEME['card_bg']};
            border-radius: 10px;
            padding: 20px;
            margin-bottom: 20px;
            border: 1px solid rgba(255,255,255,0.1);
        }}

        /* Typography */
        .cursive-title {{
            font-family: '{THEME['font_accent']}', cursive;
            color: {THEME['accent_red']};
            font-size: 2.8em;
            text-align: center;
            line-height: 1.2;
            margin-bottom: 0px;
        }}
        .cursive-subtitle {{
            font-family: '{THEME['font_accent']}', cursive;
            color: {THEME['main_text']};
            font-size: 1.8em;
            text-align: right;
            line-height: 1.2;
        }}
        .main-brand-title {{
            text-align: center;
            font-size: 3.5em;
            font-weight: 700;
            color: {THEME['main_text']};
            margin-top: -10px;
            letter-spacing: 1px;
        }}
        .brand-subtitle {{
            text-align: center;
            font-size: 1.2em;
            color: {THEME['light_gray']};
            margin-top: -15px;
            margin-bottom: 10px;
        }}
        
        .price {{
            color: {THEME['accent_red']};
            font-size: 2.8em;
            font-weight: 700;
            margin: 0px;
        }}
        .price-per-game {{
            color: {THEME['light_gray']};
            font-size: 0.8em;
            margin-top: -10px;
        }}
        .service-title {{
            color: {THEME['accent_red']};
            font-size: 1.1em;
            font-weight: 700;
            margin-bottom: 5px;
        }}
        .service-list {{
            list-style-type: '✅ ';
            padding-left: 20px;
            color: {THEME['main_text']};
        }}
        .game-list-header {{
            background-color: {THEME['accent_red']};
            color: white;
            text-align: center;
            padding: 10px;
            border-radius: 5px;
            font-weight: 700;
            font-size: 1.2em;
            margin-top: 15px;
            margin-bottom: 15px;
        }}
        .footer-logo {{
            text-align: left;
            font-size: 1.5em;
            font-weight: 700;
            color: {THEME['light_gray']};
        }}
        
        /* Layout overrides */
        [data-testid="stSidebar"] {{
            background-color: {THEME['card_bg']};
        }}
        button[kind="primary"] {{
            background-color: {THEME['accent_red']};
            border-color: {THEME['accent_red']};
            color: white;
        }}
        button[kind="primary"]:hover {{
            background-color: white;
            color: {THEME['accent_red']};
        }}
        </style>
    """, unsafe_allow_html=True)

# Define content data for easier updating
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
    "Bloodborne", "Mortal kombat 11", "Study of season", "Stars wars jedi survivor", "Tomb raider 1-3 remastered",
    "Gta 5 daeng nuansa Indonesia", "Uncharted nathan Drake", "Immortal hinyx", "Ghost recob", "Lego City Undercover",
    "Death Door", "One piece Oddyssey", "Yakuza 3", "Control"
]

PS4_HEN_UPDATES = ["Monster patch Winter 2026", "Eleven Patch Winter 2026 Final Update", "Daeng patch Summer 2026", "Bitbox patch WINTER 2026", "SGR Patch 2018 WINTER", "SGR Patch 2021 WINTER"]
PS3_BOLA_UPDATES = ["Bitbox patch", "Vr patch"]
ANDROID_SERVICES = ["Spotify mod premium", "Netflix (Nonton film gabungan vidio viu dkk)"]
SWITCH_GAMES = ["DREDGE", "STRAY"]

# -- APP CONTENT RENDERING --

def main():
    set_dark_mode()

    # -- HEADER SECTION --
    col_header_1, col_header_2 = st.columns([2, 1])
    
    with col_header_1:
        st.markdown('<p class="cursive-title">Good Games<br>Better Days</p>', unsafe_allow_html=True)
        st.markdown('<div class="box"><p class="main-brand-title">MEDY5TATION</p>', unsafe_allow_html=True)
        st.markdown('<p class="brand-subtitle">PLAY MORE • GAME TOGETHER</p></div>', unsafe_allow_html=True)

    with col_header_2:
        st.markdown('<p class="cursive-subtitle">Game<br>Tanpa<br>Batas</p>', unsafe_allow_html=True)

    # -- SERVICES ROW 1 (The Five Main Services) --
    col_v1, col_v2, col_v3, col_v4, col_v5 = st.columns(5)
    
    with col_v1:
        st.markdown('<div class="box" style="text-align: center;">🎮<br><span style="font-size:0.8em;color:{THEME["light_gray"]};">GAME ORIGINAL</span></div>', unsafe_allow_html=True)
    with col_v2:
        st.markdown('<div class="box" style="text-align: center;">☁️<br><span style="font-size:0.8em;color:{THEME["light_gray"]};">PATCH SUB INDO</span></div>', unsafe_allow_html=True)
    with col_v3:
        st.markdown('<div class="box" style="text-align: center;">💾<br><span style="font-size:0.8em;color:{THEME["light_gray"]};">HDD FULL GAME</span></div>', unsafe_allow_html=True)
    with col_v4:
        st.markdown('<div class="box" style="text-align: center;">⚙️<br><span style="font-size:0.8em;color:{THEME["light_gray"]};">INSTAL LANGSUNG</span></div>', unsafe_allow_html=True)
    with col_v5:
        st.markdown('<div class="box" style="text-align: center;">✅<br><span style="font-size:0.8em;color:{THEME["light_gray"]};">AMAN & TERPERCAYA</span></div>', unsafe_allow_html=True)

    # -- SERVICES ROW 2 (Detailed Pricing) --
    col_p1, col_p2, col_p3, col_p4 = st.columns([2, 3, 3, 2]) # Adjusted widths for content
    
    with col_p1:
        st.markdown('<div class="box" style="border: 2px solid {THEME["accent_red"]};">', unsafe_allow_html=True)
        st.markdown('<div style="text-align:center;">📥</div>', unsafe_allow_html=True)
        st.markdown('<span class="service-title">VIA DRIVE</span>', unsafe_allow_html=True)
        st.markdown('<span class="price">15K</span> <span class="price-per-game">PER<br>GAME</span>', unsafe_allow_html=True)
        st.markdown('<p style="font-size: 0.8em; color:{THEME["light_gray"]};margin-top:10px;">PATCH SUB INDO<br>DAN LINK DOWNLOAD<br>SESUAI CUSA GAME</p>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with col_p2:
        st.markdown('<div class="box" style="border: 2px solid {THEME["accent_red"]};">', unsafe_allow_html=True)
        st.markdown('<div style="text-align:center;">💿</div>', unsafe_allow_html=True)
        st.markdown('<span class="service-title">PKG & INSTALL GAME LANGSUNG DI PS</span>', unsafe_allow_html=True)
        st.markdown('<span class="price">25K</span> <span class="price-per-game">PER<br>GAME</span>', unsafe_allow_html=True)
        st.markdown('<p style="font-size: 0.9em;color:{THEME["main_text"]};">LOKASI PALEMBANG<br><span style="background-color:{THEME["accent_red"]};padding:2px 5px;border-radius:3px;">3 GAME 65K</span></p>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with col_p3:
        st.markdown('<div class="box" style="border: 2px solid {THEME["accent_red"]};">', unsafe_allow_html=True)
        st.markdown('<div style="text-align:center;">📀</div>', unsafe_allow_html=True)
        st.markdown('<span class="service-title">HDD FULL GAME SUB INDO (PKG/PNP)</span>', unsafe_allow_html=True)
        
        col_hdd_1, col_hdd_2 = st.columns(2)
        with col_hdd_1:
            st.markdown('<div style="background-color: white; color:{THEME["card_bg"]};border-radius:3px;text-align:center;padding:2px;">500GB</div>', unsafe_allow_html=True)
            st.markdown('<div class="price" style="font-size:1.8em;">350RB</div>', unsafe_allow_html=True)
        with col_hdd_2:
            st.markdown('<div style="background-color: white; color:{THEME["card_bg"]};border-radius:3px;text-align:center;padding:2px;">1TB</div>', unsafe_allow_html=True)
            st.markdown('<div class="price" style="font-size:1.8em;">550RB</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
    with col_p4:
        st.markdown('<div class="box" style="border: 2px solid {THEME["accent_red"]};">', unsafe_allow_html=True)
        col_s1, col_s2 = st.columns(2)
        with col_s1:
            st.markdown('<div style="text-align:center;">🛠️<br><span class="service-title">JASA HEN PS4</span><br><span class="price" style="font-size:1.8em;">50K</span></div>', unsafe_allow_html=True)
            st.markdown('<ul class="service-list" style="font-size:0.7em;"><li>Install HEN</li><li>Setting & Tes Game</li><li>Panduan Pemakaian</li></ul>', unsafe_allow_html=True)
        with col_s2:
            st.markdown('<div style="text-align:center;">🌡️<br><span class="service-title">GANTI PASTA THERMAL</span><br><span class="price" style="font-size:1.8em;">250RB</span></div>', unsafe_allow_html=True)
            st.markdown('<ul class="service-list" style="font-size:0.7em;"><li>Bersihin</li><li>Pasta Premium</li></ul>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Servis Stik (Placed next to Thermal)
        st.markdown('<div class="box" style="border: 2px solid {THEME["accent_red"]};">', unsafe_allow_html=True)
        st.markdown('<div style="text-align:center;">🎮<br><span class="service-title">SERVIS STIK PS4</span></div>', unsafe_allow_html=True)
        st.markdown('<ul class="service-list" style="font-size:0.7em;"><li>Analog drift</li><li>Tombol tidak respons</li><li>Ganti part / cleaning</li><li>Custom & upgrade</li></ul>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # -- GAME LIST SECTION --
    st.markdown('<div class="game-list-header">LIST GAME PATCH SUB INDONESIA (PS4)</div>', unsafe_allow_html=True)
    
    # Render game list in multi-column format (imitating the 5-column layout)
    games_per_col = (len(PS4_GAMES) // 4) + 1
    col_g1, col_g2, col_g3, col_g4 = st.columns(4)
    
    def render_game_column(games_list, column_widget, base_index):
        with column_widget:
            for i, game in enumerate(games_list):
                idx_display = base_index + i + 1
                st.markdown(f'<p style="font-size: 0.7em;color:{THEME["main_text"]}; margin-bottom: -5px;"><b>{idx_display}.</b> {game}</p>', unsafe_allow_html=True)

    # Manually chunking because of specific image ordering
    render_game_column(PS4_GAMES[0:18], col_g1, 0)
    render_game_column(PS4_GAMES[18:37], col_g2, 18)
    render_game_column(PS4_GAMES[37:55], col_g3, 37)
    render_game_column(PS4_GAMES[55:], col_g4, 55)

    # -- UPDATES & OTHER CONSOLES ROW --
    col_upd1, col_upd2, col_upd3, col_upd4 = st.columns(4)
    
    with col_upd1:
        st.markdown('<div class="box">', unsafe_allow_html=True)
        st.markdown('<p class="service-title">⚽ UPDATE BOLA PS4 HEN</p>', unsafe_allow_html=True)
        for i, up in enumerate(PS4_HEN_UPDATES):
            st.markdown(f'<p style="font-size: 0.7em;margin-bottom:-10px;">{i+1}. {up}</p>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
    with col_upd2:
        st.markdown('<div class="box">', unsafe_allow_html=True)
        st.markdown('<p class="service-title">⚽ UPDATE BOLA PS3</p>', unsafe_allow_html=True)
        for i, up in enumerate(PS3_BOLA_UPDATES):
            st.markdown(f'<p style="font-size: 0.7em;margin-bottom:-10px;">{i+1}. {up}</p>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with col_upd3:
        st.markdown('<div class="box">', unsafe_allow_html=True)
        st.markdown('<p class="service-title">📱 ANDROID</p>', unsafe_allow_html=True)
        for i, up in enumerate(ANDROID_SERVICES):
            st.markdown(f'<p style="font-size: 0.7em;margin-bottom:-10px;">{i+1}. {up}</p>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
    with col_upd4:
        st.markdown('<div class="box">', unsafe_allow_html=True)
        st.markdown('<p class="service-title">🕹️ NINTENDO SWITCH SUB INDO</p>', unsafe_allow_html=True)
        for i, game in enumerate(SWITCH_GAMES):
            st.markdown(f'<p style="font-size: 0.7em;margin-bottom:-10px;">{i+1}. {game}</p>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # -- FOOTER (CONTACT INFO) --
    st.markdown('<hr style="border-top: 2px solid rgba(255,255,255,0.1);margin-top:30px; margin-bottom:10px;">', unsafe_allow_html=True)
    
    col_ft1, col_ft2, col_ft3 = st.columns([2, 2, 2])
    
    with col_ft1:
        st.markdown('<p style="font-size: 0.8em;color:{THEME["light_gray"]};margin-bottom:-5px;">WA / ORDER</p>', unsafe_allow_html=True)
        # Using a button that links (placeholder) for order action
        if st.button("📞 082289421650", key="wa_order", type="primary"):
            st.write("Redirecting to WhatsApp...")

    with col_ft2:
        st.markdown('<p style="font-size: 0.8em;color:{THEME["light_gray"]};margin-bottom:-5px;">LOKASI</p>', unsafe_allow_html=True)
        st.markdown('<p style="font-size: 1.1em; color: white; margin-bottom:-5px;">PALEMBANG</p>', unsafe_allow_html=True)
        st.markdown('<p style="font-size: 0.7em;color:{THEME["light_gray"]};margin-top:-5px;">TEGAL BINANGUN SASANA PATRA</p>', unsafe_allow_html=True)
        
    with col_ft3:
        st.markdown('<p style="font-size: 0.8em;color:{THEME["light_gray"]};margin-bottom:-5px;">BELI JUGA DI SHOPEE</p>', unsafe_allow_html=True)
        shopee_url = "https://id.shp.ee/rLfMMQgT"
        st.link_button("🛍️ Visit Shopee Store", shopee_url, type="primary")

    # Final footer bar
    st.markdown('<hr style="border-top: 1px solid rgba(255,255,255,0.1);">', unsafe_allow_html=True)
    col_bot1, col_bot2, col_bot3 = st.columns([1, 2, 1])
    with col_bot1:
        st.markdown('<p class="footer-logo">MEDY5TATION</p>', unsafe_allow_html=True)
    with col_bot2:
        st.markdown('<p style="text-align:center; color:{THEME["light_gray"]};font-size: 0.8em;">" GAME IS ALWAYS A GOOD IDEA "</p>', unsafe_allow_html=True)
    with col_bot3:
        # Use an image for the controller icons for best layout fidelity
        st.markdown('<p style="text-align:right; color:{THEME["light_gray"]}; font-size: 0.7em;">△○×□  PLAY • SHARE • TOGETHER</p>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()