#menghitung biaya sewa
print('Tarif rental sewa mobil RP 200.000 untuk 12 jam pertama')
print('Untuk berikutnya Rp 10.000/jam')

#menyewa
tarif=200000
jam1=int(input('Masukkan waktu anda meminjam dalam satuam jam, contoh 8 :'))
mnt1=int(input('Masukkan waktu anda meminjam dalam satuam menit, contoh 30 :'))
jam2=int(input('Masukkan waktu anda memgembalikam dalam satuam jam, contoh 8 :'))
mnt2=int(input('Masukkan waktu anda memgembalikan dalam satuam menit, contoh 30 :'))
jam3=jam2-jam1
print(jam3)
mnt3=mnt2-mnt1
print('Anda menyewa dalam kurun waktu', jam3,'jam',mnt3,'menit')
tarif1=(jam3-12)*10000
tarif2=(mnt3/60)*10000
print(tarif1)
print(tarif2)
tarif3=int(tarif+tarif1+tarif2)
print('Total biaya rental mobil Rp ',tarif3)
