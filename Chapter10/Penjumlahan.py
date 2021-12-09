datalist = open("penjumlahan.txt","r")
baca = datalist.readlines()
p=[]
for i in baca:
    p.append(i.rstrip("\n"))
for i in range(len(p)):
    a=p[i].split("|")
    b=int(a[0])
    c=int(a[1])
    d=b+c
    print(d)
