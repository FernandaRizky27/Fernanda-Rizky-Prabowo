def diffDate(yyyy,mm,dd):
    from datetime import date
    now =date.today()
    masuk = date(yyyy,mm,dd)
    selisih = masuk - now
    print("Selisih harinya adalah",selisih)
yyyy = int(input("Masukkan Tahun: "))
mm = int(input("Masukkan bulan:"))
dd = int(input("Masukkan tanggal:"))
diffDate(yyyy,mm,dd)