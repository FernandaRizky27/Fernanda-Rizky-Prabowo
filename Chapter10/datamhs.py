dataFile = open("datamhs.txt","a")

while True:
    nim = input("Masukkan NIM Mahasiswa:")
    nama = input("Masukkan Nama Mahasiswa:")
    alamat = input("Masukkan Alamat Mahasiswa:")

    hasil = nim+"|"+nama+"|"+alamat+"\n"
    dataFile.write(hasil)
    jwb = input("Mau mengisi data lagi(y/n)?")
    if jwb == "n":
        break
dataFile.close()