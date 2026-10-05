import streamlit as st
from core import Blockchain

# Setup Halaman Streamlit
st.set_page_config(
    page_title="BMW Supply Chain Blockchain",
    page_icon="🚗",
    layout="wide"
)

# Inisialisasi Blockchain ke dalam Session State Streamlit agar data tidak hilang saat reload
if "bmw_chain" not in st.session_state:
    st.session_state.bmw_chain = Blockchain()
    
    # Tambahkan data awal (Sample Data)
    st.session_state.bmw_chain.add_block({
        "VIN": "WBA123456789BMW01",
        "Model": "BMW M4 Competition",
        "Tahap": "Manufaktur Komponen",
        "Lokasi": "Pabrik Munich, Jerman",
        "Keterangan": "Perakitan mesin V6 Biturbo selesai & lolos QC"
    })
    st.session_state.bmw_chain.add_block({
        "VIN": "WBA123456789BMW01",
        "Model": "BMW M4 Competition",
        "Tahap": "Perakitan Akhir",
        "Lokasi": "Pabrik Dingolfing, Jerman",
        "Keterangan": "Pemasangan bodi, sasis, dan sistem elektronik"
    })

bmw_chain = st.session_state.bmw_chain

# --- HEADER & STATUS BLOCKCHAIN ---
st.title("🚗 BMW Supply Chain Blockchain Ledger")
st.caption("Sistem Pelacakan Rantai Pasok Mobil BMW Berbasis Teknologi Blockchain SHA-256")

# Validasi Status Blockchain Secara Keseluruhan
is_valid, msg = bmw_chain.is_chain_valid()
if is_valid:
    st.success(f"✅ **Status Ledger Keseluruhan:** {msg}")
else:
    st.error(f"⚠️ **Status Ledger TERKOMPROMI/TIDAK VALID:** {msg}")

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
        bmw_chain.add_block(new_data)
        st.sidebar.success("Blok baru berhasil ditambahkan ke ledger!")
        st.rerun()

# --- SIDEBAR: SIMULASI PENGUJIAN/PERETASAN ---
st.sidebar.divider()
st.sidebar.header("🧪 Simulasi Peretasan / Tampering")
if len(bmw_chain.chain) > 1:
    target_block = st.sidebar.number_input("Pilih Nomor Blok untuk Diubah", min_value=2, max_value=len(bmw_chain.chain), step=1)
    new_text = st.sidebar.text_input("Ubah Keterangan Secara Ilegal", "Data ini diubah secara ilegal oleh pihak ketiga")
    if st.sidebar.button("Manipulasi Data Blok"):
        # Ubah data blok secara paksa tanpa memperbarui hash
        bmw_chain.chain[target_block - 1].data["Keterangan"] = new_text
        st.sidebar.warning(f"Data Blok #{target_block} berhasil dimanipulasi!")
        st.rerun()

# --- TAMPILAN LEDGER BLOCKCHAIN DENGAN PENGECEKAN VALIDASI ---
st.subheader("📜 Riwayat Rantai Pasok (Ledger Chain)")

for index, block in enumerate(bmw_chain.chain):
    # 1. Pengecekan Validitas Ulang Per Blok
    # Hitung ulang hash berdasarkan data saat ini
    calculated_hash = block.calculate_hash() if hasattr(block, 'calculate_hash') else None
    
    # Periksa apakah hash saat ini cocok dengan isi data, serta apakah previous_hash sesuai dengan hash blok sebelumnya
    is_block_corrupted = False
    if calculated_hash and block.hash != calculated_hash:
        is_block_corrupted = True
        
    if index > 0:
        prev_block = bmw_chain.chain[index - 1]
        if block.previous_hash != prev_block.hash:
            is_block_corrupted = True

    # 2. Judul Expander dengan Indikator Status
    tahap_title = block.data if isinstance(block.data, str) else block.data.get('Tahap', 'Genesis Block')
    status_icon = "❌ [DATA TERMANIPULASI]" if is_block_corrupted else "✅ [VALID]"
    expander_title = f"📦 **Blok #{block.index}** — {tahap_title} {status_icon}"

    with st.expander(expander_title, expanded=True):
        if is_block_corrupted:
            st.error("🚨 **Peringatan Pengecekan:** Hash pada blok ini tidak cocok dengan isinya atau rantai sebelumnya telah terputus!")
        else:
            st.success("🔒 **Pengecekan Data:** Hash valid & terverifikasi kodenya secara kriptografis.")

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