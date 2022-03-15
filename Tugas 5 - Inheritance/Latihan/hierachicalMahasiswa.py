class mahasiswa:
    def __init__(self, nama, nim) -> None:
        self.nama = nama
        self.nim = nim

class siswa1(mahasiswa):
    def __init__(self, nama, nim) -> None:
        self.nama = nama
        self.nim = nim

    def detSiswa1(self):
        print(self.nama, 'alamat : Wall Rose')

class siswa2(mahasiswa):
    def __init__(self, nama, nim) -> None:
        self.nama = nama
        self.nim = nim

    def detSiswa2(self):
        print(self.nama, 'jurusan : Informatika')

mhs1 = siswa1('khazin', 135105)
mhs2 = siswa2('andi',135117)

print(mhs1.nim)
mhs1.detSiswa1()
print(mhs2.nama)
mhs2.detSiswa2()