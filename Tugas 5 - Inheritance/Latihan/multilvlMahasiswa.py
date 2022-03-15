class mahasiswa:
    def __init__(self, nama, nim) -> None:
        self.nama = nama
        self.nim = nim

class siswa1(mahasiswa):
    def __init__(self, nama, nim) -> None:
        self.nama = nama
        self.nim = nim

class siswa2(mahasiswa):
    def __init__(self, nama, nim) -> None:
        self.nama = nama
        self.nim = nim


mhs1 = mahasiswa('Khazin', 135105)
mhs2 = siswa1('Andi', 135117)
mhs3 = siswa2('Tio',134079)

print(mhs1.nama , mhs1.nim)
print(mhs2.nim)
print(mhs3.nama)