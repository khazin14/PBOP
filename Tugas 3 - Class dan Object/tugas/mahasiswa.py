class Mahasiswa:
    def __init__(self, nama, nim, prodi, thn_masuk):
        self.nama = nama
        self.nim = nim
        self.prodi = prodi
        self.thn_masuk = thn_masuk


maha1 = Mahasiswa('Khazin Mubarok', '5210411187', 'Informatika', 2021)
maha2 = Mahasiswa('Ainun', '5210411000', 'Informatika', 2021)
maha3 = Mahasiswa('Andra', '5210411101', 'Informatika', 2021)


damas = [maha1, maha2, maha3]

print('Daftar Mahasiswa')
for i in damas:
        print(f'{i.nama} adalah mahasiswa {i.prodi} angkatan {i.thn_masuk} dengan nim {i.nim}')