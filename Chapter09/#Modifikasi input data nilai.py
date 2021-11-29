#MODIFIKASI input data nilai
nilai = [{'nim' : 'A01', 'nama' : 'Agustina', 'mid' : 50, 'uas' : 80}, 
 	   {'nim' : 'A02', 'nama' : 'Budi', 'mid' : 40, 'uas' : 90}, 
         {'nim' : 'A03', 'nama' : 'Chicha', 'mid' : 100, 'uas' : 50}, 
         {'nim' : 'A04', 'nama' : 'Donna', 'mid' : 20, 'uas' : 100}, 
	   {'nim' : 'A05', 'nama' : 'Fatimah', 'mid' : 70, 'uas' : 100}]

print("="*100)
print("NIM      NAMA MHS         MID       UAS      NA      STATUS")
print("="*100)
for x in range(len(nilai)):
    print(nilai[x]['nim'].ljust(9),end='')
    print(nilai[x]['nama'].ljust(15),end='')
    print(str(nilai[x]['mid']).rjust(5),end='')
    print(str(nilai[x]['uas']).rjust(10),end='')
    total=((nilai[x]['mid'])+(2*(nilai[x]['uas'])))//3
    print(str(total).rjust(8),end='')
    if(total>=60):
           print(str('LULUS').rjust(10))
    else:
        print(str('TIDAK LULUS').rjust(10))