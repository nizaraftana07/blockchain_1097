import streamlit as st
from core import Blockchain #mengimport mesin Blockchain yang kita buat

#configurasi halaman
st.set_page_config(page_title="Blockchain Explorer", page_icon="🧷", layout="wide")
st.title("📒 Blockchain for Halal Coffee Supply Chain")

#Session State Management
if 'my_blockchain' not in st.session_state:
    st.session_state.my_blockchain = Blockchain()

#sidebar input data
st.sidebar.header("➕ Tambah Data Baru")

#contoh kasus: rantai pasok kopi
petani = st.sidebar.text_input("Nama Petani/Aktor: ")
jumlah_kopi = st.sidebar.number_input("Jumlah Panen (Kg): ", min_value=1)
lokasi = st.sidebar.text_input("Lokasi Kebun: ")

if st.sidebar.button ("Tambahkan Ke Blockchain"):
    if petani and lokasi:
        #mengemas data menjadi satu string JSON-like
        data_transaksi = f"Petani: {petani} | Panen: {jumlah_kopi} Kg | Lokasi: {lokasi}"
        #memanggil method add_blockdari object yang ada di memori
        st.session_state.my_blockchain.add_block(data_transaksi)
        st.sidebar.success("Block Berhasil Ditambahkan!")
    else:
        st.sidebar.error("Lengkapi Semua Data!")

# Main Area Visualisasi Rantai 
st.subheader("📜Blockchain Ledger (Buku Besar)")

#status Validitas Rantai
is_valid = st.session_state.my_blockchain.is_chain_valid()
if is_valid:
    st.success("✅Status Jaringan: Rantai Valid (Aman)")
else:
    st.error("❌ PERINGATAN: Integritas Rantai Rusak (Telah Dimanipulasi!)")

#menampilkan semua block dengan Looping
for block in st.session_state.my_blockchain.chain:
    with st.expander(f"Blok #{block.index} | Hash: {block.hash[:15]}..."):
        #membuat 2 kolom untuk rapi
        col1, col2 = st.columns(2)

        with col1:
            st.write("**Data Payload**")
            st.info(block.data)
            st.write(f"**Timestamp:** {block.timestamp_readable}")

        with col2:
            st.write("**Kriptografi**")
            st.write(f"Hash Saat Ini:**")
            st.code(block.hash, language='python')
            st.write(f"**Hash Sebelumnya (pointer):**")
            st.code(block.previous_hash, language='python')