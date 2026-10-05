import streamlit as st
from core import Block, Blockchain

st.set_page_config(page_title="Supply Chain Kopi", page_icon="☕")
st.title("☕ Sistem Pelayakan Rantai Pasok Kopi")

if "kopi_chain" not in st.session_state:
    st.session_state.kopi_chain = Blockchain()

data_kopi = st.text_input("Masukkan Data Pengiriman (Misal: '100kg - Petani A'):")
if st.button("⚒️ Mine Block (Tambah Data)"):
    if data_kopi:
        new_index = len(st.session_state.kopi_chain.chain)
        new_block = Block(new_index, data_kopi, "")

        # Streamlit Spinner untuk efek loading saat proses PoW berlangsung
        with st.spinner("Sedang mencari Hash yang tepat (Mining)..."):
            st.session_state.kopi_chain.add_block(new_block)

        st.success("Blok berhasil ditambang dan diamankan ke dalam rantai!")

# --- FITUR BARU: Validasi Rantai ---
st.markdown("---")
if st.button("🛡️ Cek Integritas Rantai"):
    if st.session_state.kopi_chain.is_chain_valid():
        st.success("Status Jaringan: AMAN (Rantai Valid)")
    else:
        st.error("Status Jaringan: BAHAYA (Data telah dimanipulasi!)")
st.markdown("---")

st.subheader("📜 Buku Besar (Ledger)")
for block in st.session_state.kopi_chain.chain:
    with st.expander(f"Block #{block.index} - Hash: {block.hash[:15]}..."):
        st.write(f"**Waktu:** {block.timestamp}")
        st.write(f"**Data:** {block.data}")
        # FITUR BARU: Menampilkan Nonce
        st.write(f"**Nonce (Tebakan):** {block.nonce}")
        st.write(f"**Prev Hash:** {block.previous_hash}")
        # FITUR BARU: Menyoroti Hash yang sudah sesuai Difficulty
        st.info(f"**Hash:** {block.hash}")