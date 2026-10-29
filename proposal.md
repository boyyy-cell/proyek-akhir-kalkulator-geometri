
# PROPOSAL PROYEK KALKULATOR GEOMETRI

## 1. Judul Proyek
Kalkulator Geometri Berbasis Python

## 2. Latar Belakang
Geometri merupakan salah satu materi matematika yang mempelajari bentuk, luas, dan keliling bangun datar. Perhitungan secara manual terkadang membutuhkan waktu dan berisiko menimbulkan kesalahan. Oleh karena itu, dibuat program Kalkulator Geometri menggunakan Python untuk membantu pengguna melakukan perhitungan dengan lebih cepat dan mudah.

## 3. Pengguna dan Tujuan
Pengguna utama program ini adalah mahasiswa dan pelajar yang mempelajari matematika.

Tujuan proyek:
- Mempermudah perhitungan luas dan keliling bangun datar.
- Menerapkan konsep algoritma dan pemrograman Python.
- Melatih penggunaan fungsi, percabangan, perulangan, dan validasi input.

## 4. Ruang Lingkup
Fitur wajib:
1. Menghitung luas dan keliling persegi.
2. Menghitung luas dan keliling persegi panjang.
3. Menghitung luas dan keliling segitiga.
4. Menghitung luas dan keliling lingkaran.
5. Memvalidasi input dan menampilkan pesan kesalahan.

Batasan proyek:
- Program berjalan melalui terminal.
- Program dibuat menggunakan Python.
- Program hanya menghitung bangun datar yang tersedia pada menu.

## 5. Kebutuhan

### Kebutuhan Fungsional
- Program menampilkan menu pilihan bangun datar.
- Program menerima ukuran dari pengguna.
- Program menghitung luas dan keliling.
- Program menolak input yang tidak sesuai.
- Program menampilkan hasil perhitungan.

### Kebutuhan Nonfungsional
- Program mudah digunakan.
- Pesan kesalahan mudah dipahami.
- Kode disusun menggunakan fungsi.
- Program dapat dijalankan melalui terminal VS Code.

## 6. Input, Proses, dan Output

| Input | Proses | Output |
|---|---|---|
| Sisi persegi | Menghitung sisi × sisi dan 4 × sisi | Luas dan keliling persegi |
| Panjang dan lebar | Menghitung panjang × lebar dan 2 × (panjang + lebar) | Luas dan keliling persegi panjang |
| Alas, tinggi, dan tiga sisi | Menghitung luas dan menjumlahkan sisi | Luas dan keliling segitiga |
| Jari-jari lingkaran | Menghitung π × r² dan 2 × π × r | Luas dan keliling lingkaran |
| Pilihan menu | Memeriksa pilihan pengguna | Menu atau pesan kesalahan |

## 7. Algoritma
1. Mulai program.
2. Tampilkan menu kalkulator geometri.
3. Pengguna memilih bangun datar.
4. Program menerima input ukuran.
5. Program memvalidasi input.
6. Program menghitung luas dan keliling sesuai pilihan.
7. Program menampilkan hasil.
8. Ulangi menu sampai pengguna memilih keluar.
9. Selesai.

## 8. Struktur Program

## 8. Struktur Program
- `src/main.py`: mengatur alur utama program dan pemanggilan fungsi.
- `src/analisis.py`: menyediakan fungsi perhitungan luas dan keliling bangun datar.
- `src/utilitas.py`: menangani input pengguna, validasi ukuran, dan tampilan menu.
- `src/data_io.py`: menyimpan hasil perhitungan ke file riwayat.
- `README.md`: dokumentasi dan petunjuk menjalankan program.
- `proposal.md`: dokumen rancangan proyek.
- `tests/test_case.md`: dokumentasi pengujian program.
- `data/nilai_contoh.txt`: menyimpan contoh data pengujian.
- `output/riwayat.txt`: menyimpan riwayat hasil perhitungan.

Fungsi yang digunakan:
- `luas_persegi()`
- `keliling_persegi()`
- `luas_persegi_panjang()`
- `keliling_persegi_panjang()`
- `luas_segitiga()`
- `keliling_segitiga()`
- `luas_lingkaran()`
- `keliling_lingkaran()`
- `input_positif()`
- `main()`

## 9. Struktur Data
Program menggunakan tipe data float untuk menyimpan ukuran bangun datar dan hasil perhitungan. String digunakan untuk menerima pilihan menu dan menampilkan pesan. Fungsi digunakan untuk memisahkan proses perhitungan.

## 10. Test Case
Pengujian awal direncanakan mencakup input normal, input batas, input tidak valid, dan pilihan menu yang salah. Rincian pengujian ditulis pada `tests/test_case.md`.

## 11. Pembagian Tugas
Pembagian tugas disesuaikan dengan jumlah anggota kelompok:
- Koordinator: mengatur pekerjaan dan integrasi proyek.
- Programmer: membuat dan mengembangkan program.
- Tester: menguji hasil program.
- Dokumentasi: menyusun proposal dan README.

Nama anggota dan penanggung jawab akan disesuaikan dengan anggota kelompok sebenarnya.

## 12. Jadwal
- Pertemuan 14: menyusun proposal, struktur program, dan test case.
- Sebelum Pertemuan 15: menyelesaikan implementasi awal.
- Pertemuan 15: melakukan integrasi, pengujian, dan debugging.
- Pertemuan 16: presentasi dan demonstrasi program.

## 13. Repository
URL GitHub: diisi setelah repository proyek dibuat.
