# import library
import time
import datetime

# input nama user
nama = input("Hallo... nama saya Mr. Kompie, nama Anda siapa? ")

# tampilkan nama user
print("Oh.. nama Anda", nama, ", nama yang bagus sekali.")

# kasih jeda 3 detik
time.sleep(3)

# input tahun lahir
thnLahir = int(input("BTW... " + nama + "kamu lahir tahun berapa? "))

# kasih jeda 3 detik
time.sleep(3)

# hitung usia user 
skrg = datetime.datetime.now()
usia = skrg.year - thnLahir

# tampilkan usia
print("Hmmm...", nama,"kamu sudah", usia,"tahun ya..")

# tampilkan pesan sesuai range usia
if (usia > 50):
    print("Anda sudah cukup tua ya?")
    print("Jaga kesehatan ya!!")
elif (usia > 20):
    print("Ternyata Anda masih cukup muda belia")
    print("Jangan sia-siakan masa mudamu ya!!")
elif (usia > 17):
    print("Hihihi... Anda ternyata masih ABG")
    print("Mulai berpikirlah secara dewasa ya!!")
else:
    print("Oalah.. Anda masih anak-anak toh?")
    print("Jangan suka merengek-rengek minta jajan ya!!")

#Nilai
nilai = int(input("Kamu bisa kasih aku nilai 1 sampai 10. Kamu kasih berapa?"))

#Pemberian nilai
if (nilai > 9):
    print("Aaaa... terima kasih atas nilai nya <3.")
elif(nilai > 6):
    print ("Wah terima kasih atas nilainya.")
else:
    print ("Terima kasih atas nilainya.")

# kasih jeda 3 detik
time.sleep(3)

# say goodbye
print("OK.. see you later", nama, ".. senang berkenalan denganmu")
