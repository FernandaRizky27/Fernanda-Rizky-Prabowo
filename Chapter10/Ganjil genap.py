myfile = open("angka.txt", "r")
line = myfile.readlines()
p=[]
for i in line:
    p.append(i.rstrip("\n"))
ganjil=0
genap=0
for x in range (len(p)):
    y=int(p[x])
    print(y)
    if y%2==0:
        genap+=1
    else:
        ganjil+=1

print("Bilangan genap:",genap)
print("Bilangan ganjil:",ganjil)
myfile.close()