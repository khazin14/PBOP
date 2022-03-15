class mahasiswa:
    def __init__(self, nama, nim) -> None:
        self.nama = nama
        self.nim = nim

    def detailMhs(self):
        return self.nama, self.nim

    def cekMhs(self):
        if self.nim < 150000:
            return 'Mahasiswa Aktif'
        else:
            return 'Mahasiswa tidak terdaftar'

class siswa(mahasiswa):
    def end(self):
        print('Mahasiswa belum melakukan daftar ulang')


mahasiswa1 = mahasiswa('Khazin', 140702)
print(mahasiswa1.detailMhs(), mahasiswa1.cekMhs())

mahasiswa2 = siswa('Andi', 153000)
print(mahasiswa2.detailMhs(), mahasiswa2.cekMhs())
mahasiswa2.end()