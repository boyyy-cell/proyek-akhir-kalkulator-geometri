
def input_positif(pesan):
    while True:
        try:
            nilai = float(input(pesan))
            if nilai > 0:
                return nilai
            print("Input harus lebih dari 0.")
        except ValueError:
            print("Input harus berupa angka yang valid.")


def tampilkan_menu():
    print("\n=== KALKULATOR GEOMETRI ===")
    print("1. Persegi")
    print("2. Persegi Panjang")
    print("3. Segitiga")
    print("4. Lingkaran")
    print("5. Keluar")
    return input("Pilih menu (1-5): ")
