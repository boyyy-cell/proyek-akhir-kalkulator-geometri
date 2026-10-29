
import math


def hitung_persegi(sisi):
    return sisi ** 2, 4 * sisi


def hitung_persegi_panjang(panjang, lebar):
    return panjang * lebar, 2 * (panjang + lebar)


def hitung_segitiga(alas, tinggi, a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("Sisi tidak membentuk segitiga yang valid.")

    luas = 0.5 * alas * tinggi
    keliling = a + b + c
    return luas, keliling


def hitung_lingkaran(jari_jari):
    luas = math.pi * jari_jari ** 2
    keliling = 2 * math.pi * jari_jari
    return luas, keliling
