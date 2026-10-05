import streamlit as st
from core import Blockchain

# Setup Halaman Streamlit
st.set_page_config(
    page_title="BMW Supply Chain Blockchain",
    page_icon="🚗",
    layout="wide"
)

# 1. Inisialisasi Blockchain ke dalam Session State Streamlit
# Menggunakan nama key 'kopi_chain' sesuai dengan spesifikasi penugasan
if "kopi_chain" not in st.session_state:
    st.session_state.kopi_chain = Blockchain()
    
    # Tambahkan data awal
    st.session_state.kopi_chain.add_block({
        "VIN": "WBA123456789BMW01",
        "Model": "BMW M4 Competition",
        "Tahap": "Manufaktur Komponen",
        "Lokasi": "Pabrik Munich, Jerman",
        "Keterangan": "Perakitan mesin V6 Biturbo selesai & lolos QC"
    })
    st.session_state.kopi_chain.add_block({
        "VIN": "WBA123456789BMW01",
        "Model": "BMW M4 Competition",
        "Tahap": "Perakitan Akhir",
        "Lokasi": "Pabrik Dingolfing, Jerman",
        "Keterangan": "Pemasangan bodi, sasis, dan sistem elektronik"
    })

kopi_chain = st.session_state.kopi_chain

# --- HEADER & STATUS BLOCKCHAIN ---
st.title("🚗 BMW Supply Chain Blockchain Ledger")
st.caption("Sistem Pelacakan Rantai Pasok Mobil BMW Berbasis Teknologi Blockchain SHA-256")

# 4. Pembuktian Sistem / Pengecekan Integritas Rantai
if st.button("🛡️ Cek Integritas Rantai"):
    is_valid, msg = kopi_chain.is_chain_valid()
    if is_valid:
        st.success(f"✅ **AMAN:** {msg}")
    else:
        st.error(f"🚨 **BAHAYA:** Kebocoran atau manipulasi data terdeteksi! ({msg})")

st.divider()

# --- SIDEBAR: TAMBAH BLOK BARU ---
st.sidebar.header("➕ Tambah Lacak Pasok Baru")

with st.sidebar.form("add_block_form", clear_on_submit=True):
    vin = st.text_input("VIN (Vehicle Identification Number)", value="WBA123456789BMW01")
    model = st.selectbox("Model BMW", ["BMW M4 Competition", "BMW M3 Sedan", "BMW i4 M50", "BMW X5 xDrive40i", "BMW i7 xDrive60"])
    tahap = st.selectbox("Tahap Distribusi", [
        "Manufaktur Komponen",
        "Perakitan Akhir (Assembly)",
        "Pengujian Kualitas (QC)",
        "Logistik & Pengiriman Laut/Darat",
        "Penerimaan Dealer",
        "Penyerahan ke Konsumen"
    ])
    lokasi = st.text_input("Lokasi", value="Pelabuhan Tanjung Priok, Jakarta")
    keterangan = st.text_area("Keterangan Tambahan", value="Kendaraan tiba di pelabuhan dan lolos inspeksi bea cukai.")
    
    submitted = st.form_submit_button("Simpan ke Blockchain")
    
    if submitted:
        new_data = {
            "VIN": vin,
            "Model": model,
            "Tahap": tahap,
            "Lokasi": lokasi,
            "Keterangan": keterangan
        }
        kopi_chain.add_block(new_data)
        st.sidebar.success("Blok baru berhasil ditambahkan ke ledger!")
        st.rerun()

# --- SIDEBAR: SIMULASI SERANGAN (HACKING) ---
st.sidebar.divider()
st.sidebar.header("🧪 Simulasi Peretasan / Tampering")

# 2 & 3. Tombol Khusus "HACK BLOK 1" & Manipulasi Memori
if st.sidebar.button("HACK BLOK 1"):
    if len(st.session_state.kopi_chain.chain) > 1:
        # Eksekusi manipulasi data secara paksa
        st.session_state.kopi_chain.chain[1].data = "DATA PALSU!"
        st.sidebar.warning("⚠️ Data pada Blok 1 berhasil diubah secara paksa menjadi 'DATA PALSU!'")
        st.rerun()
    else:
        st.sidebar.error("Blok index 1 belum tersedia. Tambahkan blok terlebih dahulu!")

# --- TAMPILAN LEDGER BLOCKCHAIN ---
st.subheader("📜 Riwayat Rantai Pasok (Ledger Chain)")

for block in kopi_chain.chain:
    with st.expander(f"📦 **Blok #{block.index}** — {block.data if isinstance(block.data, str) else block.data.get('Tahap', 'Genesis Block')}", expanded=True):
        col1, col2 = st.columns([1, 2])
        
        with col1:
            st.markdown("**Waktu Ditambahkan:**")
            st.info(block.timestamp_readable)
            st.markdown("**Previous Hash:**")
            st.code(block.previous_hash, language="text")
            st.markdown("**Current Hash:**")
            st.code(block.hash, language="text")
            
        with col2:
            st.markdown("**Detail Informasi Data:**")
            if isinstance(block.data, dict):
                st.json(block.data)
            else:
                st.write(block.data)