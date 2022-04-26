import datetime
waktu=datetime.datetime.now() 

class Perpusitem: 
    def __init__(self,judul,subjek,lokasi,info):
        self.judul = judul 
        self.subjek =  subjek
        self.lokasi = lokasi
        self.info = info

    '''def lokasiSimpan(self):
    self.lokasi = lokasi
    self.info = info
    '''

class Buku(Perpusitem): 
    def __init__(self,judul,subjek,lokasi,info,isbn,pengarang,jmlhal,ukuran):
        super().__init__(judul,"Buku",lokasi, info) 
        self.isbn = isbn
        self.pengarang = pengarang 
        self.jmlhal = jmlhal
        self.ukuran = ukuran

class Majalah(Perpusitem): 
    def __init__(self,judul,subjek,lokasi,info,volume,issue):
        super().__init__(judul,"Majalah",lokasi,info) 
        self.volume = volume 
        self.issue = issue

class DVD(Perpusitem): #
    def __init__(self,judul,subjek, lokasi, info, aktor, genre):
        super().__init__(judul,"DVD",lokasi,info) 
        self.aktor = aktor 
        self.fenre = genre

class borrow(Perpusitem): 
    def __init__(self,nama_buku,pengarang,nama_peminjam, tanggal_pinjam):
        self.nama_peminjam = nama_peminjam
        self.nama_buku = nama_buku 
        self.pengarang = pengarang
        self.tanggal_pinjam = tanggal_pinjam

class returnn(Perpusitem):
    def __init__(self,nama_buku, pengarang, nama_peminjam, tanggal_pengembalian):
        self.nama_peminjam = nama_peminjam
        self.nama_buku = nama_buku 
        self.pengarang = pengarang
        self.tanggal_pengembalian = tanggal_pengembalian

class katalog():
    def Search(item,my_list):
        found = False
        position = 0
        while position < len(my_list) and not found:
            if my_list[position] == item:
                found = True
            position = position + 1
        return found


b =Buku("Ziarah","Buku cetak","Rak Nomor 14","ada","945-900-20-02","Iwan Simatupang",2,"25x150")
m = Majalah("Bobo","Majalah cetak","Rak nomor 7","ada","X","Dari Hobi Menjadi Prestasi")
d = DVD("Warkop DKI Reborn","Film","Rak nomor 2","dipinjam","Anggi Umbara","Film")

book = ['Sistem operasi','sistem cedas','Front end developer','malin kundang','si kancil']

def buku(): 
    daftar =[b,m,d] 
    for dft in daftar: 
        print("Judul  : {}".format(dft.judul))
        print("subjek : {}".format(dft.subjek)) 
        print("Lokasi : {}".format(dft.lokasi)) 
        print("Info   : {}".format(dft.info),"\n") 


while True: 
        print("==== PERPUSTAKAAN UTY ====") 
        print("1. Daftar Buku")
        print("2. Pinjam Buku")
        print("3. Pencarian buku")
        print("4. Pengembalian Buku")
        print("5. Keluar Program")
        pilihan = 0
        pilihan =int(input("Masukan pilihan Anda : ")) 

        if pilihan == 1:
            print("==== DAFTAR BUKU ====")
            buku()
        
        elif pilihan == 2:
            print("==== PEMINJAMAN BUKU ====")
            nama = str(input("Nama Peminjam  : ")) 
            judul_buku = str(input("Nama Buku      : "))
            pengarang = str(input("Pengarang Buku : "))
            tanggal_pinjam = waktu 

            print("Pinjam buku berhasil.....","\n")
    
            p = borrow(judul_buku,pengarang,nama,tanggal_pinjam) 
            data = [p] 
            for x in data:
                print("Judul buku     : {}".format(x.nama_buku)) 
                print("Karangan       : {}".format(x.pengarang))
                print("Nama           : {}".format(x.nama_peminjam)) 
                print("Tanggal pinjam : {}".format(x.tanggal_pinjam),"\n",) 

        elif pilihan == 3:
            print("==== MENCARI BUKU ====")
            data =katalog.Search 
            cari = input('Masukan judul Buku : ')
            item =data(cari,book)
            if item:
                print("Buku",cari," berhasil ditemukan....","\n") 
                print('Buku', cari, "Tidak ditemukan....","\n") 

        elif pilihan == 4: 
            print("==== PENGEMBALIAN BUKU ====") 
            nama = str(input("Nama Peminjam  : ")) 
            judul_buku = str(input("Nama Buku      : ")) 
            pengarang = str(input("Pengarang Buku : "))
            tanggal_pengembalian = waktu 
            print("pengembalian buku berhasil....","\n")
            p = returnn(judul_buku,pengarang,nama,tanggal_pengembalian) 
            for y in data:  
                print("Judul buku     : {}".format(y.nama_buku)) 
                print("Karangan       : {}".format(y.pengarang)) 
                print("Nama           : {}".format(y.nama_peminjam)) 
                print("Dibuat pada    : {}".format(y.tanggal_pengembalian),"\n") 
        
        elif pilihan == 5: #
            print("==== KELUAR PROGRAM ====")
            print("Terima Kasih sudah berkunjung di Perpustakaan UTY")
            break 
            
        else: 
            print ("maaf menu tidak tersedia...","\n") 