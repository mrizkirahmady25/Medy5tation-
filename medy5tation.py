import streamlit as st

# =========================
# PENGATURAN HALAMAN
# =========================

st.set_page_config(
    page_title="Medy5tation",
    page_icon="🎮",
    layout="wide"
)

# =========================
# JUDUL
# =========================

st.title("🎮 MEDY5TATION")
st.subheader("PS4 • GAME • SERVICE")

st.write(
    "Selamat datang di Medy5tation."
)

st.write(
    "Menyediakan game PS4, jasa isi game, "
    "update game, dan service controller."
)

st.divider()

# =========================
# MENU
# =========================

menu = st.sidebar.selectbox(
    "MENU MEDY5TATION",
    [
        "Beranda",
        "Game PS4",
        "Jasa Isi Game",
        "Jasa Service",
        "Kontak"
    ]
)

# =========================
# BERANDA
# =========================

if menu == "Beranda":

    st.header("Selamat Datang 👋")

    st.write(
        "Medy5tation adalah tempat untuk kebutuhan "
        "gaming dan service PlayStation."
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("🎮 GAME PS4")
        st.write(
            "Berbagai pilihan game PlayStation 4."
        )

    with col2:
        st.subheader("💿 ISI GAME")
        st.write(
            "Jasa isi dan update game PS4."
        )

    with col3:
        st.subheader("🔧 SERVICE")
        st.write(
            "Jasa service PS4 dan controller."
        )

    st.divider()

    st.info(
        "Silakan gunakan menu di sebelah kiri "
        "untuk melihat layanan Medy5tation."
    )


# =========================
# GAME PS4
# =========================

elif menu == "Game PS4":

    st.header("🎮 GAME PS4")

    st.write(
        "Pilih game yang ingin kamu lihat:"
    )

    game = st.selectbox(
        "Daftar Game",
        [
            "FC 26",
            "GTA V",
            "God of War",
            "Uncharted 4",
            "The Last of Us Part II",
            "Red Dead Redemption 2"
        ]
    )

    st.success(
        "Game yang dipilih: " + game
    )

    st.write(
        "Untuk harga dan ketersediaan game, "
        "silakan hubungi Medy5tation."
    )


# =========================
# JASA ISI GAME
# =========================

elif menu == "Jasa Isi Game":

    st.header("💿 JASA ISI GAME PS4")

    st.write(
        "Layanan yang tersedia:"
    )

    st.write("✅ Isi game PS4")
    st.write("✅ Update game")
    st.write("✅ Update roster")
    st.write("✅ Game subtitle Indonesia")
    st.write("✅ Isi game melalui HDD")

    st.divider()

    st.warning(
        "Harga dan ketersediaan dapat berubah. "
        "Silakan hubungi Medy5tation."
    )


# =========================
# SERVICE
# =========================

elif menu == "Jasa Service":

    st.header("🔧 JASA SERVICE")

    service = st.selectbox(
        "Pilih layanan",
        [
            "Service Controller PS4",
            "Service PS4",
            "Pengecekan HDD",
            "Install Game",
            "Update Game"
        ]
    )

    st.success(
        "Layanan yang dipilih: " + service
    )

    st.write(
        "Hubungi Medy5tation untuk konsultasi "
        "dan pengecekan lebih lanjut."
    )


# =========================
# KONTAK
# =========================

elif menu == "Kontak":

    st.header("📱 KONTAK MEDY5TATION")

    st.write(
        "Untuk informasi harga, pemesanan, "
        "dan konsultasi service:"
    )

    st.write("📱 WhatsApp")
    st.write("🛒 Shopee")

    st.divider()

    st.info(
        "Silakan hubungi Medy5tation "
        "untuk mengetahui harga dan ketersediaan."
    )


# =========================
# FOOTER
# =========================

st.divider()

st.caption(
    "© 2026 Medy5tation | PS4 • GAME • SERVICE"
)