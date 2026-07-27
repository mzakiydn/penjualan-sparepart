Judul Proyek : Analisis Tren Penjualan dan Stok Sparepart Mobil
Nama         : Muhammad Zakiyuddin Ramadhan
NIM          : 25.11.6348

Deskripsi :
Proyek ini dibuat untuk menganalisis data penjualan komponen sparepart mobil (seperti bumper, kaca depan, kap mesin, dll). Program ini menggunakan Python untuk membaca data secara otomatis, lalu menghitung beberapa poin penting seperti:
- Total seluruh barang yang laku terjual.
- Rata-rata stok awal yang tersedia di gudang.
- Mencari produk apa yang paling laris dan produk mana yang penjualannya paling sedikit.
- Mengelompokkan total penjualan berdasarkan tipe mobil konsumen.

Dataset proyek ini diambil langsung dari Kaggle melalui link berikut:
https://www.kaggle.com/datasets/zahrasyakiranabilla/penjualan-sparepart

Cara Menjalankan Program:
1. Install Library Dahulu:
   Pastikan laptop sudah terinstal library pandas dan matplotlib. Jika belum, buka terminal di VS Code lalu ketik:
   pip install pandas matplotlib

2. Mengatur File dan Folder:
   - Buat folder baru bernama 'dataset' di dalam folder proyek ini.
   - Download file CSV dari link Kaggle di atas, lalu masukkan ke dalam folder 'dataset' tadi dan ubah namanya menjadi 'data_mentah.csv'.
   - Struktur foldernya harus seperti ini:
     ├── dataset/
     │   └── data_mentah.csv
     ├── utils.py
     ├── main.py
     └── README.txt

3. Running Program:
   Buka terminal di VS Code, pastikan posisi path terminal sudah berada di folder proyek ini, lalu jalankan perintah:
   python main.py

4. Output:
   Setelah program selesai berjalan, otomatis akan muncul dua file baru di folder proyek Anda:
   - 'hasil_analisis.txt' : Berisi teks rangkuman statistik dan laporan produk terlaris.
   - 'grafik_output.png'  : Berisi visualisasi grafik batang dari hasil penjualan produk.
