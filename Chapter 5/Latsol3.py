#menghitung berapa banyak konsumsi bbm
print("Pak Budi akan melakukan perjalanan ke kota A ke Kota C dengan jarak 765.")
print("Konsumsi BBM mobil Pak Budi adalah 1:12.")
print("Berapakah liter kah bahan bakar yang diperlukan unuk sampai ke kota C?")
#menghitung
bensin = 1/12
bbm = float(input("Masukkan jarak Kota A ke kota C :"))
total = bbm*bensin
print("Bensin yang dibutuhkan Pak Budi adalah", total, "liter")
print("Apabila kapasitas bahan bakar mobil Pak Budi 50 liter")
print("Berapa banyak pengisian bahan bakar saat menuju ke kota C?")
kapasitas = 50
pengisian = total//kapasitas
print("Jadi Pak Budi minimal harus mengisi BBM sebanyak", pengisian,"kali agar sampai ke Kota C.")