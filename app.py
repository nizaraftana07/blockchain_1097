import streamlit as st
from core import Blockchain  # Mengimpor logika blockchain dari core.py

# 1. Konfigurasi Halaman & Branding
st.set_page_config(
    page_title="RoastChain - Roastery & Coffee Ledger",
    page_icon="🔥",
    layout="wide"
)

st.title("🔥 RoastChain")
st.caption("Immutable Roastery & Supply Chain Ledger — Transparansi Sangrai hingga Cangkir")

# 2. Session State Management
if 'roastchain_ledger' not in st.session_state:
    st.session_state.roastchain_ledger = Blockchain()

# 3. Sidebar Input Data Sederhana
st.sidebar.header("➕ Catat Pasokan Biji Kopi")

supplier_pt = st.sidebar.text_input("Nama PT Supplier:", placeholder="Contoh: PT Kopi Harapan Tani")
jumlah_kg = st.sidebar.number_input("Jumlah Biji Kopi (Kg):", min_value=1, value=50)
penerima = st.sidebar.text_input("Penerima / Tujuan:", placeholder="Contoh: Roastery Utama / Klien A")

if st.sidebar.button("Simpan ke RoastChain"):
    if supplier_pt and penerima:
        # Mengemas data transaksi ringkas
        payload = f"Supplier: {supplier_pt} | Jumlah: {jumlah_kg} Kg | Penerima: {penerima}"
        
        # Menambahkan ke blockchain
        st.session_state.roastchain_ledger.add_block(payload)
        st.sidebar.success("✅ Transaksi Berhasil Ditambahkan!")
    else:
        st.sidebar.error("⚠️ Lengkapi Nama PT Supplier dan Penerima!")

# 4. Main Area - Visualisasi Buku Besar RoastChain
st.subheader("📜 RoastChain Block Explorer")

# Status Validitas Rantai
is_valid = st.session_state.roastchain_ledger.is_chain_valid()
if is_valid:
    st.success("✅ Status Jaringan: Valid (Integritas Data Terjamin)")
else:
    st.error("🚨 PERINGATAN: Integritas Data Rusak! Terdeteksi Perubahan Ilegal.")

# Menampilkan Daftar Blok
for block in st.session_state.roastchain_ledger.chain:
    with st.expander(f"🔥 Blok #{block.index} | Hash: {block.hash[:18]}... | Waktu: {block.timestamp_readable}"):
        col1, col2 = st.columns(2)
        
        with col1:
            st.write("**📦 Transaksi Pasokan**")
            st.info(block.data)
            
        with col2:
            st.write("**🔒 Bukti Kriptografi (SHA-256)**")
            st.write("**Hash Blok Ini:**")
            st.code(block.hash, language='python')
            st.write("**Hash Blok Sebelumnya (Pointer):**")
            st.code(block.previous_hash, language='python')