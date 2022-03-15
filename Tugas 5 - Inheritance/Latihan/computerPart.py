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


class ram(computerPart):
    def __init__(self,pabrikan, nama, harga, kapasitas):
        super().__init__(pabrikan,nama,"RAM",harga)
        self.kapasitas = kapasitas

class hardDisk(computerPart):
    def __init__(self, pabrikan, nama, harga,  kapasitas, rpm):
        super().__init__(pabrikan, nama, "SATA", harga)
        self.kapasitas = kapasitas
        self.rpm = rpm


p = processor('Intel', 'Core i7 11700K', 6500000, 12, '4.5GHz')
m = ram('Team', 'DDR4 SODimm 3200Mhz', 500000, '8GB')
hdd = hardDisk('WD Blue', 'HDD 2,5 Inch', 500000, '1000GB',7200)

parts = [p,m,hdd]
for part in parts:
    print(f'{part.jenis} {part.nama} Produksi {part.pabrikan}')