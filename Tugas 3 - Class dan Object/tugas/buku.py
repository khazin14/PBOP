class Buku:
    def __init__(self, judul, pengarang, tahun_terbit):
        self.judul = judul
        self.pengarang = pengarang
        self.tahun_terbit = tahun_terbit


buku1 = Buku('Kamu Terlalu Banyak Bercanda', 'Marchella FP', 2018)
buku2 = Buku('Guru Aini', 'Andrea Hirata', 2020)
buku3 = Buku('Dear Tomorrow: Notes to My Future Self', 'Maudy Ayunda', 2018)


dabuk = [buku1, buku2, buku3]

print('Daftar Buku')
for i in dabuk:
    print(
        f'Buku {i.judul} karangan {i.pengarang} pertama kali diterbitkan tahun {i.tahun_terbit}')
