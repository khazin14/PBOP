#KHAZIN MUBAROK
#5210411187

while True:
    print('======== PROGRAM MENGHITUNG LUAS ========')
    print('1. PERSEGI PANJANG')
    print('2. SEGITIGA')
    print('3. LINGKARAN')
    print('4. KELUAR')
    print('=========================================')
    pilih=int(input('Masukan Pilihan : '))
    if pilih ==1:
        p = int(input('Masukan Panjang : '))
        l = int(input('Masukan Lebar : '))
        pp = p*l
        print('Luas Persegi Panjang adalah :', pp)
        wait = input("Press enter to continue...")
    elif pilih ==2:
        a = int(input('Masukan Alas : '))
        t = int(input('Masukan Tinggi : '))
        segitiga = a*t/2
        print('Luas Segitiganya adalah :', segitiga)
        wait = input("Press enter to continue...")
    elif pilih ==3:
        jj = int(input("Masukkan Jari Lingkaran: "))
        lingkaran = (jj*jj)*3.14
        print("Luas lingkaran adalah : ", lingkaran)
        wait = input("Press enter to continue...")
    elif pilih ==4:
        print('Terimakasih')
        break
    else:
        print('Salah pilih menu')