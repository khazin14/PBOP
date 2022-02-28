class menuMinuman:
    def __init__(self, nama, deskripsi, harga):
        self.nama = nama
        self.deskripsi = deskripsi
        self.harga = harga


menu1 = menuMinuman('Barley Coffee', 'Coffee with barley and palm sugar', 15000)
menu2 = menuMinuman('Choco Hazelnut',
                   'Hazelnut and nut flavored drink', 12000)
menu3 = menuMinuman('Milk Coffee',
                   'Premium coffee with premium milk and palm sugar', 15000)
menu4 = menuMinuman('Americano', 'Ice bold black coffee with palm sugar', 14000)
menu5 = menuMinuman('Cinnamon Coffee', 'Coffee with the aroma of cinnamon is very relaxing for the body and mind', 15000)


pilihanMenu = [menu1, menu2, menu3, menu4, menu5,]
print('Daftar Menu Pesona Coffee')

for i in pilihanMenu:
    print('{} harga Rp. {} , {}'.format(i.nama, i.harga, i.deskripsi))