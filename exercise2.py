import random
angka_rahasia = random.randint(0,10)

while True:
    print('---SELAMAT DATANG---')
    pilihan = int(input('Masukan Angka : '))
    percobaan += 1

    if pilihan > angka_rahasia:
        print('Angka lebih tinggi dari angka rahasia')
    elif pilihan < angka_rahasia:
        print('Angka ')