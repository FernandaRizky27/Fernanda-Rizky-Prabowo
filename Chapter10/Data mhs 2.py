datafile = open("datamhs.txt","r")
datalist = []
data = datafile.readlines()
for i in range (len(data)):
    hasildata = data[i].split("|")
    datadisk = {"nim": hasildata[0], "nama": hasildata[1], "alamat": hasildata[2]}
    datalist.append(datadisk)
print(datalist)
datafile.close()