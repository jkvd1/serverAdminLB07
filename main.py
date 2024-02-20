#tolong buat fungsi lainnya untuk pengurangan, perkalian, pembagian
#dengan format yang sama

def operasi_matematika(a, b, operasi):
    return operasi(a, b)

penambahan = lambda a, b: a + b
pengurangan = lambda a, b: a - b
perkalian = lambda a, b: a * b
pembagian = lambda a, b: a / b

def main():
    a = 10
    b = 5

    operasi = {
        'Penambahan': penambahan,
        'Pengurangan': pengurangan,
        'Perkalian': perkalian,
        'Pembagian': pembagian
    }

    for nama_operasi, fungsi_operasi in operasi.items():
        hasil = operasi_matematika(a, b, fungsi_operasi)
        print(f"{nama_operasi}: {hasil}")

main()
