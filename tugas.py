class karyawan:
    print('>>>>>Dasar kelas untuk semua karyawan<<<<<')
    jumlah_karyawan = 2

    def __init__ (self,nama,gaji):
        self.nama = nama
        self.gaji = gaji
        karyawan.jumlah_karyawan += 1
        
    def tampilkan_jumlah(self):
         print("Total karyawan;",karyawan.jumlah_karyawan)

    def tampilkan_profil(self):
         print("nama :", self.nama)
         print("gaji :", self.gaji)

# membuat objek pertama dari kelas karyawan
karyawan1 = print("aini")
# membuat objek kedua dari kelas karyawan
karyawan2 = print("sarip")

karyawan1 = ('tampilkan_profil()')
karyawan2 = ('tampilkan_profil()')
print("Total karyawan :",karyawan.jumlah_karyawan)