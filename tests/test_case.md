
# Test Case Kalkulator Geometri

## Tujuan Pengujian
Memastikan program dapat menghitung luas dan keliling bangun datar serta menangani input yang tidak valid.

| ID | Pengujian | Input | Hasil yang Diharapkan |
|---|---|---|---|
| TC01 | Persegi | Sisi 5 | Luas 25, keliling 20 |
| TC02 | Persegi Panjang | Panjang 8, lebar 4 | Luas 32, keliling 24 |
| TC03 | Segitiga | Alas 6, tinggi 4, sisi 5, 5, 6 | Luas 12, keliling 16 |
| TC04 | Lingkaran | Jari-jari 7 | Luas 153.94, keliling 43.98 |
| TC05 | Input nol | Sisi 0 | Program meminta input positif |
| TC06 | Input huruf | Memasukkan huruf pada ukuran | Program meminta input angka |
| TC07 | Pilihan menu salah | Memilih menu 9 | Pesan pilihan tidak valid |
| TC08 | Segitiga tidak valid | Sisi 1, 2, 10 | Program menolak segitiga |

## Kesimpulan
Pengujian dilakukan dengan membandingkan hasil aktual dengan hasil yang diharapkan. Program dinyatakan sesuai apabila hasil perhitungan benar dan kesalahan input ditangani dengan baik.
