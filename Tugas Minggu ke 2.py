#untuk class buku
class buku :
    def __init__ (self,judul,penulis,isbn):
        self.judul   = judul
        self.penulis = penulis
        self.isbn    = isbn
        self.sedang_dipinjam = False

    def daftar_buku(self):
        status = "dipinjam" if self.sedang_dipinjam else "tersedia"
        print(f"judul   = {self.judul}")
        print(f"penulis = {self.penulis}")
        print(f"ISBN    = {self.isbn}")
        print(f"status {self.judul} ={status}")

    def dipinjam(self):
        self.sedang_dipinjam = True
    
    def dikembalikan(self):
        self.sedang_dipinjam = False



#untuk class anggota perpus
class member :
    def __init__(self,nama,member_id,):
        self.nama       = nama
        self.member_id  = member_id
        self.daftar_pinjam =[]
    
    def tambah_peminjaman(self,peminjaman):
        self.daftar_pinjam.append(peminjaman)



#untuk class penjaga perpus
class staff:
    def __init__(self, nama, staff_id):
        self.nama    = nama
        self.staffid = staff_id




class TransaksiPeminjaman :
    def __init__(self, buku, member, staff , tanggal_pinjam):
        self.buku           = buku
        self.member         = member
        self.staff          = staff
        self.tanggal_pinjam = tanggal_pinjam
        self.sudah_dikembalikan = False
    
    def pinjam_buku(self):
        if not self.buku.sedang_dipinjam:
            self.buku.dipinjam()
            self.member.tambah_peminjaman(self)
            print(f"buku {self.buku.judul} berhasil dipinjam oleh {self.member.nama}")
        else:
            print(f"maaf {self.member.nama}, buku sedang dipinjam")

    def kembalikan_buku(self):
        if not self.sudah_dikembalikan:
            self.buku.dikembalikan()
            print(f"buku {self.buku.judul} berhasil dikembalikan")
        else:
            print("buku sudah dikembalikan sebelumnya") 

#proses meminjam
buku1 = buku("laskar pelangi", "adrea hirata", "2110100")
buku2 = buku("bumi manusia", "pramoedya", "2110233")
buku3 = buku("deep work", "cal newport", "2110452")

member1 = member("chelsia viontika", "0000012")
member2 = member("cahaya indah", "0000007")
member3 = member("bunga lestari", "0000232")
member4 = member("choi seungcheol", "0000011")

staff1 = staff("zeska candra", "11221")
staff2 = staff("putri maya", "12111")

transaksi1 = TransaksiPeminjaman(buku1, member1, staff1, "01-02-2026")
transaksi2 = TransaksiPeminjaman(buku1, member2, staff1, "02-02-2026")
transaksi3 = TransaksiPeminjaman(buku2, member3, staff1, "02-02-2026")
transaksi4 = TransaksiPeminjaman(buku3, member4, staff2, "03-02-2026")

print("\n")
transaksi1.pinjam_buku()
transaksi2.pinjam_buku()
transaksi3.pinjam_buku()
transaksi4.pinjam_buku()

print("\nStatus Buku Setelah Peminjaman")
buku1.daftar_buku()
buku2.daftar_buku()
buku3.daftar_buku()

print("\n")
transaksi1.kembalikan_buku()
transaksi2.kembalikan_buku()
transaksi3.kembalikan_buku()
transaksi4.kembalikan_buku()

print("\nStatus Buku Setelah Pengembalian")
buku1.daftar_buku()
buku2.daftar_buku()
buku3.daftar_buku()


        
    
