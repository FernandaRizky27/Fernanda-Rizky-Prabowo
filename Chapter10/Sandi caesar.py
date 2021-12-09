from typing import Text


enkripsi = open("sandi.txt","r")
text = enkripsi.read()
key = int(input("Masukkan berapa banyak urutan huruf yang digeser:"))
def caesar(text, key): 
    sandi = ""
    for ch in text:
        if ch.isalpha():
            huruf = ord(ch) + key
            if huruf > ord('z'):
                huruf -= 26
            textakhir= chr(huruf)
        
        sandi += textakhir

    print ("Hasilnya adalah: ", sandi)
    final = open("sandicaesar","a+")
    final.write(sandi)
    final.close()

    return sandi
enkripsi.close()
caesar(text, key)