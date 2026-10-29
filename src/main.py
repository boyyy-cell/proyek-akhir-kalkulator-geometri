
from analisis import (
    hitung_persegi,
    hitung_persegi_panjang,
    hitung_segitiga,
    hitung_lingkaran,
)
from utilitas import input_positif, tampilkan_menu
from data_io import simpan_laporan


def proses_perhitungan(pilihan):
    if pilihan == "1":
        sisi = input_positif("Masukkan sisi: ")
        luas, keliling = hitung_persegi(sisi)
        nama = "Persegi"

    elif pilihan == "2":
        panjang = input_positif("Masukkan panjang: ")
        lebar = input_positif("Masukkan lebar: ")
        luas, keliling = hitung_persegi_panjang(panjang, lebar)
        nama = "Persegi Panjang"

    elif pilihan == "3":
        alas = input_positif("Masukkan alas: ")
        tinggi = input_positif("Masukkan tinggi: ")
        a = input_positif("Masukkan sisi pertama: ")
        b = input_positif("Masukkan sisi kedua: ")
        c = input_positif("Masukkan sisi ketiga: ")

        luas, keliling = hitung_segitiga(alas, tinggi, a, b, c)
        nama = "Segitiga"

    elif pilihan == "4":
        r = input_positif("Masukkan jari-jari: ")
        luas, keliling = hitung_lingkaran(r)
        nama = "Lingkaran"

    else:
        print("Pilihan tidak valid.")
        return

    hasil = (
        f"Bangun datar: {nama}\n"
        f"Luas: {luas:.2f}\n"
        f"Keliling: {keliling:.2f}"
    )

    print("\n" + hasil)
    simpan_laporan(hasil)
    print("Hasil berhasil disimpan ke output/riwayat.txt")


def main():
    while True:
        pilihan = tampilkan_menu()

        if pilihan == "5":
            print("Terima kasih telah menggunakan program!")
            break

        try:
            proses_perhitungan(pilihan)
        except ValueError as error:
            print(f"Perhitungan gagal: {error}")


if __name__ == "__main__":
    main()
