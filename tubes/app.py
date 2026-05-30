"""
================================================
FRONTEND — Tampilan Streamlit
File    : app.py
Dikerjakan oleh: Ummi & Fathiya
================================================

Cara Menjalankan:
    pip install streamlit gtts
    streamlit run app.py
"""

import streamlit as st
from logic import Queue, buat_audio, estimasi_tunggu

# ─────────────────────────────────────────────
# INISIALISASI SESSION STATE
# ─────────────────────────────────────────────
if "antrian" not in st.session_state:
    st.session_state.antrian = Queue()

q: Queue = st.session_state.antrian


def putar_audio(teks: str):
    b64 = buat_audio(teks)
    st.markdown(
        f'<audio autoplay><source src="data:audio/mp3;base64,{b64}" type="audio/mp3"></audio>',
        unsafe_allow_html=True
    )


# ─────────────────────────────────────────────
# DATA MENU
# ─────────────────────────────────────────────
MENU = {
    "🍜 Mie": [
        "Mie Gacoan Lv 0", "Mie Gacoan Lv 1", "Mie Gacoan Lv 2",
        "Mie Gacoan Lv 3", "Mie Gacoan Lv 4", "Mie Gacoan Lv 5",
        "Mie Gacoan Lv 6", "Mie Gacoan Lv 7", "Mie Gacoan Lv 8",
        "Mie Hompimpa", "Mie Suit",
    ],
    "🥟 Dimsum": [
        "Udang Rambutan", "Udang Keju", "Lumpia Udang",
        "Siomay", "Pangsit Goreng", "Ceker", "Lobster Ball", "Fish Roll",
    ],
    "🧊 Es & Minuman": [
        "Es Gobak Sodor", "Es Teklek", "Es Petak Umpet", "Es Sluku Bathok",
        "Es Teh", "Lemon Tea", "Vanilla Latte", "Thai Tea", "Milo",
    ],
}

# ─────────────────────────────────────────────
# TAMPILAN UTAMA
# ─────────────────────────────────────────────
st.set_page_config(page_title="Antrian Mie Gacoan", page_icon="🍜", layout="centered")
st.title("🍜 Sistem Antrian Restoran")
st.subheader("Mie Gacoan — Konsep Queue (FIFO)")
st.divider()

# ── BAGIAN 1: ENQUEUE ─────────────────────────
st.subheader("➕ Tambah Pelanggan (Enqueue)")

with st.form("form_enqueue", clear_on_submit=True):
    nama_input   = st.text_input("Nama Pelanggan", placeholder="cth: Farhan")
    pesanan_list = []
    for kategori, items in MENU.items():
        with st.expander(kategori):
            pilihan = st.multiselect(f"Pilih {kategori}", items, key=kategori)
            pesanan_list.extend(pilihan)

    submitted = st.form_submit_button("🪑 Masukkan ke Antrian", use_container_width=True)

if submitted:
    if not nama_input.strip():
        st.warning("⚠️ Nama pelanggan tidak boleh kosong.")
    elif not pesanan_list:
        st.warning("⚠️ Pilih minimal satu pesanan.")
    else:
        q.enqueue(nama_input.strip(), ", ".join(pesanan_list))
        st.success(f"✅ **{nama_input}** masuk antrian. Posisi: #{q.size()} | Estimasi tunggu: {estimasi_tunggu(q.size() - 1)}")

st.divider()

# ── BAGIAN 2: DEQUEUE ─────────────────────────
st.subheader("📢 Panggil Pelanggan (Dequeue)")

if st.button("🔔 Panggil Pelanggan Berikutnya", use_container_width=True, type="primary"):
    if q.is_empty():
        st.error("❌ Antrian kosong!")
    else:
        pelanggan = q.dequeue()
        nama, pesanan = pelanggan["nama"], pelanggan["pesanan"]
        teks = f"Atas nama {nama}, pesanan {pesanan} siap diambil. Silakan menuju kasir."

        st.success(f"📣 Memanggil: **{nama}** — {pesanan}")
        st.info(f"🔊 *\"{teks}\"*")
        try:
            putar_audio(teks)
        except Exception as e:
            st.warning(f"Audio tidak dapat diputar: {e}")

st.divider()

# ── BAGIAN 3: STATUS ANTRIAN ──────────────────
st.subheader("📋 Status Antrian")

col_f, col_r, col_s = st.columns(3)
with col_f:
    f = q.front()
    st.metric("🟢 Depan (Front)", f["nama"] if f else "—")
with col_r:
    r = q.rear()
    st.metric("🔴 Belakang (Rear)", r["nama"] if r else "—")
with col_s:
    st.metric("👥 Total Antrian", q.size())

# ── BAGIAN 4: ISI ANTRIAN ─────────────────────
st.subheader("🗂️ Isi Antrian Saat Ini")

isi = q.to_list()
if not isi:
    st.info("Antrian kosong. Silakan tambahkan pelanggan.")
else:
    for i, p in enumerate(isi):
        label  = "🟢 DEPAN" if i == 0 else ("🔴 BELAKANG" if i == q.size() - 1 else f"#{i+1}")
        tunggu = estimasi_tunggu(i)
        waktu  = p["waktu_masuk"].strftime("%H:%M:%S")
        st.write(f"**{label}** → {p['nama']} | {p['pesanan']} | ⏱ {tunggu} | masuk: {waktu}")

st.divider()

if st.button("🗑️ Reset Antrian", use_container_width=True):
    q.reset()
    st.success("Antrian telah direset.")
    st.rerun()
