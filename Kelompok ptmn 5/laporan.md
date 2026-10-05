# LAPORAN TUGAS PROJEK KELOMPOK
## BMW Supply Chain Blockchain Ledger: Sistem Pelacakan Rantai Pasok Berbasis Streamlit & SHA-256

---

**Mata Kuliah:** Blockchain  
**Dosen Pengampu:** [Nama Dosen, S.Kom., M.T.]  
**Kelas:** 3 INF D  

---

### Anggota Kelompok:
1. **Nizar Aftana** - 2530801097
2. **Wafah Khonia** - 2530801081
3. **Wahyu** - 2530801103

---

### A. TUJUAN PEMBELAJARAN

1. Mahasiswa memahami konsep Object-Oriented Programming (OOP) pada Python melalui penerapan class dalam sistem blockchain.
2. Mahasiswa mampu menerapkan arsitektur modular dengan memisahkan bagian backend (`core.py`) dan frontend (`app.py`) pada aplikasi.
3. Mahasiswa memahami konsep dasar Blockchain, khususnya penggunaan block, hash, dan hash pointer dalam membentuk sebuah rantai data.
4. Mahasiswa mampu menerapkan algoritma SHA-256 untuk menjaga integritas data pada setiap blok.
5. Mahasiswa mampu membangun sistem sederhana untuk melakukan pelacakan rantai pasok kendaraan BMW secara terstruktur.
6. Mahasiswa mampu melakukan simulasi perubahan data atau tampering untuk mengetahui cara kerja validasi keamanan pada blockchain.

---

### B. KONSEP ARSITEKTUR MODULAR

Pada project ini, aplikasi blockchain dikembangkan menggunakan konsep arsitektur modular. Sistem dibagi menjadi dua bagian utama, yaitu backend (`core.py`) dan frontend (`app.py`). Pemisahan tersebut dilakukan agar logika utama blockchain tidak tercampur dengan bagian antarmuka aplikasi.

1. Backend (core.py)
   Backend merupakan bagian yang bertugas mengatur proses utama blockchain. Pada project ini, backend menangani pembuatan blok, pembentukan rantai blockchain, proses hashing menggunakan SHA-256, penambahan data baru, serta pemeriksaan validitas rantai.  
   
   Backend terdiri dari dua class utama, yaitu `Block` dan `Blockchain`.  
   * Class `Block` digunakan untuk menyimpan informasi sebuah blok, seperti nomor blok (`index`), waktu pembuatan (`timestamp`), data (`data`), hash dari blok sebelumnya (`previous_hash`), dan hash dari blok tersebut (`hash`).  
   * Class `Blockchain` digunakan untuk mengatur keseluruhan rantai blok (`chain`). Class ini bertugas membuat Genesis Block (`create_genesis_block`), menambahkan blok baru (`add_block`), serta melakukan validasi terhadap seluruh rantai blockchain (`is_chain_valid`).

2. Frontend (app.py)
   Frontend digunakan sebagai antarmuka yang memungkinkan pengguna berinteraksi dengan sistem blockchain. Pada project ini, frontend dibuat menggunakan Streamlit sehingga aplikasi dapat dijalankan melalui web browser dan dikelola menggunakan `st.session_state`.  
   
   Melalui antarmuka tersebut, pengguna dapat melihat status blockchain, melihat riwayat rantai pasok, menambahkan data perjalanan kendaraan melalui sidebar form, serta melakukan simulasi manipulasi data untuk menguji sistem validasi blockchain.

---

### C. DESKRIPSI PROJECT

Project yang dibuat merupakan sistem **BMW Supply Chain Blockchain Ledger**, yaitu sistem sederhana untuk melakukan pelacakan perjalanan kendaraan BMW dalam rantai pasok.

Rantai pasok kendaraan terdiri dari beberapa tahapan, mulai dari proses manufaktur komponen, perakitan akhir, pengujian kualitas, proses logistik dan pengiriman, penerimaan oleh dealer, hingga kendaraan diserahkan kepada konsumen.

Setiap tahapan tersebut disimpan sebagai sebuah blok di dalam blockchain. Data yang disimpan meliputi VIN (Vehicle Identification Number), model kendaraan, tahap proses, lokasi, dan keterangan tambahan.

Penggunaan blockchain pada project ini bertujuan untuk memberikan mekanisme pencatatan yang dapat mendeteksi apabila data yang telah tersimpan mengalami perubahan secara ilegal.

---

### D. LANGKAH KERJA PROJECT

* Tahap 1: Membuat Struktur Blockchain  
  Tahap pertama adalah membangun struktur blockchain yang terdiri dari beberapa blok yang saling terhubung. Setiap blok memiliki informasi berupa nomor blok (`index`), timestamp, data, `previous_hash`, dan `hash`. Hash pada setiap blok digunakan sebagai identitas unik yang terbentuk berdasarkan isi data blok tersebut.

* Tahap 2: Membuat Genesis Block  
  Blockchain diawali dengan sebuah Genesis Block. Genesis Block merupakan blok pertama yang menjadi titik awal dari rantai blockchain. Pada project ini, Genesis Block digunakan sebagai blok inisialisasi untuk ledger BMW Supply Chain dengan `index = 0` dan `previous_hash = "0"`.

* Tahap 3: Menambahkan Data Rantai Pasok
  Setelah Genesis Block dibuat, sistem menambahkan data awal mengenai perjalanan kendaraan BMW ke dalam `st.session_state.kopi_chain`:
  * VIN : WBA123456789BMW01 | Model : BMW M4 Competition |  Tahap : Manufaktur Komponen |  Lokasi : Pabrik Munich, Jerman.
  * VIN : WBA123456789BMW01 | Model : BMW M4 Competition |  Tahap : Perakitan Akhir |  Lokasi : Pabrik Dingolfing, Jerman.  
  
  Setiap data baru akan dibuat menjadi blok baru dan dihubungkan dengan hash dari blok sebelumnya.

* Tahap 4: Proses Hashing SHA-256 
  Setiap blok menghasilkan hash menggunakan algoritma SHA-256 melalui method `calculate_hash()`. Hash tersebut diperoleh berdasarkan gabungan dari `index`, `timestamp`, `data`, dan `previous_hash`. Jika terdapat perubahan pada data blok setelah hash dibuat, hasil perhitungan hash baru akan berbeda dengan hash yang tersimpan sebelumnya.

* Tahap 5: Validasi Blockchain
  Sistem melakukan validasi melalui method `is_chain_valid()` untuk memastikan bahwa setiap blok masih dalam kondisi valid. Validasi dilakukan dengan dua pemeriksaan utama:
  1. Memastikan `current_block.hash` masih sama dengan hasil perhitungan ulang `current_block.calculate_hash()`.
  2. Memastikan nilai `current_block.previous_hash` sesuai dengan `previous_block.hash` dari blok sebelumnya.  
  
  Jika kedua pemeriksaan tersebut terpenuhi, blockchain dinyatakan valid (`AMAN`).

* Tahap 6: Menambahkan Data Melalui Antarmuka
  Pengguna dapat menambahkan informasi rantai pasok baru melalui form yang tersedia pada bagian sidebar aplikasi. Data yang dapat dimasukkan meliputi: VIN kendaraan, Model BMW, Tahap distribusi, Lokasi, dan Keterangan tambahan. Setelah data disimpan, sistem akan membuat blok baru dan memasukkannya ke dalam blockchain.

* Tahap 7: Simulasi Tampering
  Project juga menyediakan fitur simulasi tampering melalui tombol  "HACK BLOK 1" pada sidebar. Fitur tersebut digunakan untuk mengubah atribut `.data` pada Blok 1 secara langsung di memori menjadi `"DATA PALSU!"` tanpa memperbarui hash yang telah tersimpan. Setelah data dimanipulasi, saat tombol "🛡️ Cek Integritas Rantai" ditekan, sistem mendeteksi perbedaan hash dan menampilkan status bahaya/kebocoran data.

---

### E. HASIL IMPLEMENTASI

Hasil implementasi project berupa sebuah aplikasi web interaktif Streamlit yang menampilkan **BMW Supply Chain Blockchain Ledger**.

Pada halaman utama, pengguna dapat melihat status validitas blockchain dan seluruh riwayat rantai pasok kendaraan. Setiap blok ditampilkan dalam komponen `st.expander` dengan informasi:
* Nomor blok (`Blok #index`)
* Waktu penambahan data (`timestamp_readable`)
* Previous Hash
* Current Hash
* Detail informasi rantai pasok dalam format JSON atau teks.

Selain melihat data, pengguna juga dapat menambahkan data rantai pasok baru melalui form sidebar dan menjalankan simulasi peretasan.

---

### F. ANALISIS HASIL

Berdasarkan implementasi yang dilakukan, blockchain dapat digunakan sebagai salah satu pendekatan untuk menjaga integritas data pada sistem pelacakan rantai pasok.

Setiap blok memiliki hubungan dengan blok sebelumnya melalui `previous_hash`. Hubungan tersebut membuat perubahan pada suatu blok dapat memengaruhi validitas rantai karena data yang telah diubah akan menghasilkan hash yang berbeda.

Penggunaan SHA-256 juga memberikan mekanisme untuk mendeteksi perubahan isi blok. Apabila data dalam sebuah blok dimodifikasi secara langsung (seperti simulasi pada Blok 1), hasil perhitungan `calculate_hash()` tidak lagi sesuai dengan hash yang tersimpan di dalam atribut `hash`.

Fitur simulasi tampering membantu membuktikan konsep immutability blockchain secara visual di antarmuka Streamlit. Saat peretasan dilakukan, sistem dengan sigap memberikan peringatan bahwa data telah mengalami manipulasi.

---

### G. KESIMPULAN

Project **BMW Supply Chain Blockchain** berhasil mengimplementasikan konsep dasar blockchain untuk mencatat dan melacak tahapan rantai pasok kendaraan BMW.

Sistem menggunakan struktur `Block` dan `Blockchain` yang saling terhubung melalui *hash pointer* serta menggunakan algoritma SHA-256 untuk menghasilkan hash setiap blok. Selain itu, sistem memiliki mekanisme validasi `is_chain_valid()` yang dapat mendeteksi perubahan data pada blok.

Penggunaan Streamlit membuat proses interaksi dengan blockchain menjadi lebih interaktif karena pengguna dapat melihat ledger, menambahkan data rantai pasok, serta melakukan simulasi tampering secara *real-time*.

---

### H. HASIL IMPLEMENTASI (TAMPILAN APLIKASI)

![ssan hasil bawah.png](ssan hasil bawah.png)

![ssan hasil.png](ssan hasil.png)