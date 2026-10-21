# Materi 4 — GIS dan Pemetaan
## Studi kasus: Pemetaan fasilitas umum di Kota Bengkulu

### Latar belakang
GIS dapat membantu menyimpan, memetakan, dan memahami informasi berdasarkan lokasi. Contoh ini menampilkan titik fasilitas pada peta web dan mengelompokkan penanda berdasarkan jenisnya.

### Kaitan dengan materi
Proyek memperlihatkan hubungan antara data spasial, atribut, dan peta interaktif. Dalam praktik industri GIS, data perlu dibersihkan dan distandarkan sebelum dimasukkan ke basis data. Contoh ini belum memakai PostGIS atau data resmi pemerintah.

### Fitur
- Membaca koordinat dan atribut dari CSV.
- Menampilkan titik pada peta interaktif.
- Memberi warna berbeda untuk tiap kategori.
- Membuat file HTML yang bisa dibuka di browser.

### Struktur folder
```text
Materi_4_GIS_dan_Pemetaan/
├── README.md
├── requirements.txt
├── src/
│   └── buat_peta.py
└── data/
    └── fasilitas_bengkulu.csv
```

### Cara menjalankan
```bash
pip install -r requirements.txt
python src/buat_peta.py
```
Program menghasilkan `outputs/peta_fasilitas.html`. Buka file itu di browser.

### Catatan
Nama dan koordinat fasilitas merupakan data demonstrasi, bukan data resmi. Untuk pemetaan sungguhan, gunakan koordinat yang sudah diverifikasi.
