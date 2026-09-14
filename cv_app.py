import streamlit as st

# Pembuatan Title Halaman
st.set_page_config(page_title="CV App", page_icon="📄", layout="wide")

# Pembuatan sidebar
st.sidebar.title("Pengaturan Profile")
st.sidebar.write("Masukkan data diri Anda di bawah ini:")

# Komponen Inputan
nama = st.sidebar.text_input("Nama:", "Nama Lengkap")
nim = st.sidebar.text_input("NIM", "123456789")
jurusan = st.sidebar.text_input("Jurusan", "Teknik Informatika")

deskripsi = st.sidebar.text_area("Deskripsi", "Saya adalah seorang mahasiswa yang tertarik dengan dunia teknologi dan pemrograman.")
pengalaman_organisasi = st.sidebar.text_area("Pengalaman Organisasi", "- Anggota Himpunan Mahasiswa (2023 - Sekarang)\n- Panitia Event Kampus")

# Sidebar slider untuk mengatur level skill
st.sidebar.markdown("---")
st.sidebar.subheader("Atur Kemahiran Skill")
skill_python = st.sidebar.slider("Python", 0, 100, 80)
skill_web = st.sidebar.slider("Web Development", 0, 100, 60)
skill_db = st.sidebar.slider("Database", 0, 100, 70)

# Area utama
st.title("Curriculum Vitae")
st.markdown("---")

kolom_kiri, kolom_kanan = st.columns([1, 2])
with kolom_kiri:
    st.header(nama)
    # Gunakan try-except agar tidak error jika file Foto.jpg tidak ada
    try:
        st.image("Foto.jpg", use_container_width=True)
    except:
        st.warning("Foto.jpg tidak ditemukan")
    st.markdown(f"**{jurusan}** | NIM: {nim}")

with kolom_kanan:
    st.markdown("### 👤 Tentang Saya")
    st.write(deskripsi)
    
    st.markdown("### 🏛️ Pengalaman Organisasi")
    st.write(pengalaman_organisasi)

# - BAGIAN KEAHLIAN (SKILLS) -
st.markdown("---")
st.markdown("### 🛠️ Keahlian Teknis")

# Menampilkan indikator visual (Progress Bar) di halaman utama
st.write(f"**Python ({skill_python}%)**")
st.progress(skill_python)

st.write(f"**Web Development ({skill_web}%)**")
st.progress(skill_web)

st.write(f"**Database ({skill_db}%)**")
st.progress(skill_db)

# - BAGIAN KONTAK -
st.markdown("---")
st.markdown("### 📬 Hubungi Saya")
nama_clean = nama.lower().replace(' ', '')
with st.expander("Klik untuk melihat detail kontak"):
    st.write(f"📧 Email: {nama_clean}@gmail.com")
    st.write(f"🔗 LinkedIn: linkedin.com/in/{nama_clean}")
    st.write(f"🐙 GitHub: github.com/{nama_clean}")

# - BAGIAN UNDUH CV -
st.markdown("---")
st.markdown("### 📥 Unduh CV")

# Menggabungkan seluruh data menjadi format teks yang rapi
data_cv = f"""
========================================
           CURRICULUM VITAE
========================================

NAMA    : {nama}
NIM     : {nim}
JURUSAN : {jurusan}

----------------------------------------
TENTANG SAYA:
{deskripsi}

----------------------------------------
PENGALAMAN ORGANISASI:
{pengalaman_organisasi}

----------------------------------------
KEAHLIAN TEKNIS:
- Python          : {skill_python}%
- Web Development : {skill_web}%
- Database        : {skill_db}%

----------------------------------------
KONTAK:
- Email    : {nama_clean}@gmail.com
- LinkedIn : linkedin.com/in/{nama_clean}
- GitHub   : github.com/{nama_clean}
========================================
"""

# Tombol Download File TXT
st.download_button(
    label="📄 Unduh CV (Format TXT)",
    data=data_cv,
    file_name=f"CV_{nama.replace(' ', '_')}.txt",
    mime="text/plain"
)