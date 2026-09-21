# 📜 Laporan Proyek: RoastChain — Immutable Roastery & Coffee Supply Chain Ledger

---

## 📌 1. Ringkasan Eksekutif

**RoastChain** adalah aplikasi berbasis Python dan Streamlit yang mengimplementasikan teknologi *Blockchain* sederhana untuk mencatat dan memantau rantai pasok (supply chain) kopi, mulai dari pemasok (*supplier*) hingga roastery atau penerima akhir.

Dengan memanfaatkan algoritma kriptografi **SHA-256**, RoastChain memastikan bahwa setiap catatan transaksi bersifat tak terubah (*immutable*), transparan, dan dapat diverifikasi keabsahannya secara langsung (*real-time verification*).

---

## 🛠️ 2. Arsitektur & Teknologi

Proyek ini terbagi menjadi dua komponen utama:
1. **`core.py` (Logika Blockchain)**: Mengatur struktur data blok, penghitungan hash, dan validasi keterkaitan antar-blok.
2. **`app.py` (Antarmuka Pengguna / User Interface)**: Dibangun menggunakan **Streamlit** untuk memfasilitasi entri data transaksi dan visualisasi *Block Explorer*.

### Tech Stack:
- **Bahasa Pemrograman**: Python 3.x
- **Framework UI**: Streamlit
- **Modul Standar Python**: `hashlib`, `time`, `datetime`
- **Algoritma Hashing**: SHA-256

---

## 🧱 3. Pembahasan Kode Utama

### A. Struktur Data Kriptografi (`core.py`)

#### 1. Kelas `Block`
Setiap blok menyimpan informasi esensial:
- `index`: Urutan posisi blok dalam rantai.
- `timestamp`: Waktu pembuatan blok dalam format Unix timestamp.
- `data`: Muatan/informasi transaksi yang dicatat.
- `previous_hash`: Hash unik dari blok sebelum dirinya (penghubung rantai).
- `hash`: Hasil kalkulasi SHA-256 dari seluruh isi atribut blok.

```python
def calculate_hash(self):
    block_string = (
        str(self.index)
        + str(self.timestamp)
        + str(self.data)
        + str(self.previous_hash)
    )
    return hashlib.sha256(block_string.encode()).hexdigest()
```

#### 2. Kelas `Blockchain`
Mengelola seluruh rantai (*ledger*) dan fungsi pengujian integritas data:
- **Genesis Block**: Blok pertama yang diinisialisasi secara otomatis saat sistem pertama kali dijalankan.
- **Validasi Rantai (`is_chain_valid`)**: Melakukan dua tahap pemeriksaan keamanan:
  1. Memverifikasi apakah isi data suatu blok telah dimodifikasi (membandingkan `hash` simpanan dengan rekalkulasi `calculate_hash()`).
  2. Memverifikasi apakah keterkaitan `previous_hash` sesuai dengan `hash` blok sebelumnya.

---

### B. Antarmuka Web Interaktif (`app.py`)

#### 1. Manajemen Sesi State (`st.session_state`)
Agar instance blockchain tidak ter-reset setiap kali pengguna berinteraksi dengan UI Streamlit, ledger disimpan ke dalam session state:
```python
if 'roastchain_ledger' not in st.session_state:
    st.session_state.roastchain_ledger = Blockchain()
```

#### 2. Form Input Pasokan Biji Kopi (Sidebar)
Memungkinkan pengguna memasukkan:
- Nama PT Supplier (pemasok)
- Jumlah Biji Kopi (dalam Kg)
- Nama Penerima / Tujuan

Data tersebut dikemas menjadi string payload terformat dan ditambahkan ke blockchain melalui metode `add_block()`.

#### 3. Block Explorer & Monitoring Integritas
- Display status validitas jaringan secara *live* (`st.success` jika valid, `st.error` jika ada perusakan data).
- Menampilkan rincian blok dalam bentuk *collapsible card* (`st.expander`), menampilkan payload transaksi serta potongan kode SHA-256 (`hash` dan `previous_hash`).

---

## 💡 4. Alur Kerja Aplikasi (Workflow)

```
[ Pengguna Mengisi Form ] 
         │
         ▼
[ Format Payload: "Supplier: X | Jumlah: Y Kg | Penerima: Z" ]
         │
         ▼
[ Buat Blok Baru: Hitung Timestamp & SHA-256 ]
         │
         ▼
[ Hubungkan `previous_hash` dengan Hash Blok Terakhir ]
         │
         ▼
[ Tambahkan ke session_state.roastchain_ledger ]
         │
         ▼
[ Validasi Ulang Seluruh Rantai (is_chain_valid) ]
         │
         ▼
[ Tampilkan pada Block Explorer UI ]
```

---

## 🚀 5. Rencana Pengembangan Lengkap (Future Roadmap)

1. **Persistensi Data**: Mengintegrasikan database (misal: PostgreSQL atau MongoDB) agar data blockchain tersimpan secara permanen saat aplikasi di-restart.
2. **Proof-of-Work (PoW) / Consensus**: Menambahkan mekanisme konsensus/mining sederhana untuk mensimulasikan blockchain terdistribusi secara nyata.
3. **Multi-Role User**: Fitur otentikasi login untuk Petani, Roaster, dan Distributor agar riwayat pasokan memiliki tanda tangan digital (*digital signature*).
4. **QR Code Generator**: Menghasilkan QR Code untuk setiap batch kopi agar konsumen akhir dapat memindai dan melihat riwayat asal-usul kopi (*Farm-to-Cup Transparency*).

---

## 📄 6. Kesimpulan
Proyek **RoastChain** berhasil mensimulasikan penggunaan teknologi blockchain pada industri kopi roastery. Aplikasi ini membuktikan bahwa transparansi data dan perlindungan dari manipulasi transaksi dapat dicapai dengan memanfaatkan kombinasi algoritma enkripsi SHA-256 dan antarmuka web modern berbasi Streamlit.

![alt text](image.png)