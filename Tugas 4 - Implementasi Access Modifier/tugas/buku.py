class Buku:
    def __init__(self, judul, pengarang, tahun_terbit, harga):
        self.judul = judul
        self.pengarang = pengarang
        self.tahun_terbit = tahun_terbit
        self.__harga = harga


buku1 = Buku('Kamu Terlalu Banyak Bercanda', 'Marchella FP', 2018, 72000)
buku2 = Buku('Guru Aini', 'Andrea Hirata', 2020, 74000)
buku3 = Buku('Dear Tomorrow: Notes to My Future Self', 'Maudy Ayunda', 2018, 129000)


dabuk = [buku1, buku2, buku3]

print('Daftar Buku')
for i in dabuk:
    print(
        f'Buku {i.judul} karangan {i.pengarang} pertama kali diterbitkan tahun {i.tahun_terbit} dan dibandrol dengan harga Rp. {i._Buku__harga}')