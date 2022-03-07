class menuMinuman:
    def __init__(self, nama, deskripsi, harga, ukuran):
        self.nama = nama
        self.deskripsi = deskripsi
        self.harga = harga
        self.__ukuran = ukuran


menu1 = menuMinuman('Barley Coffee', 'Coffee with barley and palm sugar', 15000, 'Tall')
menu2 = menuMinuman('Choco Hazelnut',
                   'Hazelnut and nut flavored drink', 12000, 'Grande')
menu3 = menuMinuman('Milk Coffee',
                   'Premium coffee with premium milk and palm sugar', 15000, 'Venti')
menu4 = menuMinuman('Americano', 'Ice bold black coffee with palm sugar', 14000, 'Venti')
menu5 = menuMinuman('Cinnamon Coffee', 'Coffee with the aroma of cinnamon is very relaxing for the body and mind', 15000, 'Grande')


pilihanMenu = [menu1, menu2, menu3, menu4, menu5,]
print('Daftar Menu Pesona Coffee')

for i in pilihanMenu:
    print('{} harga Rp. {} , {} , {}' .format(
        i.nama, i.harga, i.deskripsi, i._menuMinuman__ukuran))