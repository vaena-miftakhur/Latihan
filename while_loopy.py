i = 0
while i < 10:
    if i == 5:
        print(f'{i} - python itu mudah')
        i += 1
        continue

while True:
    print('Sam')

jumlah = 10
for i in range(jumlah):
    print(i)
    if i == 5:
        break

while True:
    name = input('Masukan Nama : ')
    option = input('Apakah anda ingin keluar? (y/t)').lower()
    if option == 'y':
        print('Program selesai')
        break



    