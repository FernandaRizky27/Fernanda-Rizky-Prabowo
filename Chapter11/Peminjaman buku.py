dataFile = open("datapeminjaman.txt","a+")
import datetime
x = datetime.datetime.date(datetime.datetime.now())
y = x + datetime.timedelta(days = 7)
while True:
    nim = input("Masukkan Kode Member:")
    nama = input("Masukkan Nama Mahasiswa:")
    alamat = input("Judul Buku:")
    
    hasil = nim + "|" + nama + "|" + alamat + "|" + str(x) +"|"+ str(y) + "\n"
    dataFile.write(hasil)
    jwb = input("Mau mengisi data lagi(y/n)?")
    if jwb == "n":
        break
dataFile.close()