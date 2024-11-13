# for i in range (5,10):
#     print(f'perulangan ke-{i}')

# fruits = ['apel','duren', 'khuldi','sirsak','kecubung']
# for i, fruit in enumerate (fruits):
#     print(f'BUah ke-{i} : {fruit}')

#keluar saat UTS
# for i in range(0,11):
#     if i % 2 == 0:
#         print(f'{i} adalah bilangan genap')
#     else:
#         print(f'{i} adalah bilangan ganjil')

# buah = {
#     'apel' : 40,
#     'mangga' : 90,
#     'duren' : 10,
# }

# for label in buah:
#     print(label)

# for value in buah.values():
#     print(value)

# for name, jumlah in buah.items():
#     print(f'Buah : {name}, Jumlah : {jumlah}')

total_nilai = 0 
jumlah = int(input ('Masukan jumlah siswa : ') )
for i in range(jumlah):
    nilai = int(input (f'Siswa nilai ke-{i}: '))
    total_nilai += nilai

rata_rata_nilai = float(total_nilai / jumlah)

print(f'Rata_rata nilai = {rata_rata_nilai}')
   
    

# jumlah = 10
# for i in range(jumlah):
#     print(i)
#     if i == 5:
#         break


# for i in range(5):
#     if i == 3:
#         continue
#     print(i)