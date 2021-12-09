#Mencari kode peminjam
print("Selamat datang di Perpustakaan PTIK")
from datetime import timedelta

datafile = open("datapeminjaman.txt","r")
cari = input("Masukkan kode peminjaman: ")
buku = datafile.readlines()

for i in range(len(buku)):
    if cari in buku[i]:
        d=buku[i].split("|")
        print("Kode Peminjam:",d[0])
        print("Nama:",d[1])
        print("Judul buku:",d[2])
        print("Tanggal meminjam:",d[3])
        print("Tanggal mengembalikan:",d[4])
        #hitung hari
        from datetime import date
        now =date.today()
        btspnjm = now+timedelta(days=-2)
        selisih = now-btspnjm
        y=int(selisih.days)
        if y<=0:
            print("Terlambat: 0 Hari")
            print("Denda: 0 Rupiah")
        else:
            print("Terlambat:",y,"hari")
            print("Denda:",y * 2000,"Rupiah")
    
        break
datafile.close()

