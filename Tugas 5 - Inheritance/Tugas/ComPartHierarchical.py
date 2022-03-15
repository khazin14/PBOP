class computerPart:
    def __init__(self,pabrikan, nama, jenis, harga):
        self.pabrikan = pabrikan
        self.nama = nama
        self.jenis = jenis
        self.harga = harga

class processor(computerPart):
    def __init__(self,pabrikan,nama,harga,jumlahCore, speed):
        super().__init__(pabrikan, nama, "Processor", harga)
        self.jumlahCore = jumlahCore
        self.speed = speed

    def detailProcessor(self):
        print('\nDetail Processor')
        print(f'''
        Pabrikan    : {self.pabrikan}
        Nama        : {self.nama}
        Jumlah Core : {self.jumlahCore}
        Speed       : {self.speed}
        Harga       : {self.harga}''')

class ram(computerPart):
    def __init__(self,pabrikan, nama, harga, kapasitas):
        super().__init__(pabrikan,nama,"RAM",harga)
        self.kapasitas = kapasitas

    def detailRam(self):
        print('\nDetail Ram')
        print(f'''
        Pabrikan    : {self.pabrikan}
        Nama        : {self.nama}
        Kapasitas   : {self.kapasitas}
        Harga       : {self.harga}''')

class hardDisk(computerPart):
    def __init__(self, pabrikan, nama, harga,  kapasitas, rpm):
        super().__init__(pabrikan, nama, "Sata", harga)
        self.kapasitas = kapasitas
        self.rpm = rpm

    def detailHardisk(self):
        print('\nDetail Harddisk')
        print(f'''
        Pabrikan    : {self.pabrikan}
        Nama        : {self.nama}
        Kapasitas   : {self.kapasitas}
        Speed       : {self.kapasitas} RPM
        Harga       : {self.harga}''')
        

data1 = input('Input data processor (Pabrikan, Nama, harga, Jumlah Core, kecepatan) : ')
data1 = data1.split(',')
p = processor(data1[0],data1[1],int(data1[2]),data1[3],data1[4])

data2 = input('Input data ram (Pabrikan, Nama, harga, kapasistas) : ')
data2 = data2.split(',')
r = ram(data2[0],data2[1],int(data2[2]),data2[3])

data3 = input('Input data hardisk (Pabrikan, Nama, harga, kapasistas, rpm) : ')
data3 = data3.split(',')
hdd = hardDisk(data3[0],data3[1],int(data3[2]),data3[3],data3[4])

parts = [p,r,hdd]
for part in parts:
    print(f'{part.jenis} {part.nama} Produksi {part.pabrikan}')

p.detailProcessor()
r.detailRam()
hdd.detailHardisk()