#memasukkan jarak dan kecepatan  dari Kota A ke kota B
print('Jarak Kota A ke Kota B adalah 125 KM')
print('Rata rata kecepatan 62km/jam')
print('Jarak kota B ke kota C adalah 256 km')
print(' Rata rata kecepatan 70km/jam')
print('Berangkat dari kota A jam 06.00 dan istirahat di kota  B 45 menit')
print('Estimasi waktu untuk sampai ke kota C')

#penyelesaian
wa=6
mnt=45
jrk1=int(input('Masukkan jarak kota A ke kota B:'))
kcpt1=int(input('Masukkan kecepatan rata rata :'))
wkt1=jrk1//kcpt1
jrk2=int(input('Masukkan jarak kota B ke kota C:'))
kcpt2=int(input('Masukkan kecepatan rata rata :'))
wkt2=jrk2//kcpt2
wkt3=wkt1+wkt2
print(wkt3,'jam perjalanan')
total=wa+wkt3
print('Pak Amir sampai di kota C Jam',total,'menit',mnt)
