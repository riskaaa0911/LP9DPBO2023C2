from hunian import Hunian

class Indekos(Hunian):
    def __init__(self, nama_pemilik, nama_penghuni, jml_penghuni, jml_kamar, lokasi, harga, path_photo):
        super().__init__("Indekos", jml_penghuni, jml_kamar, lokasi, path_photo)
        self.nama_pemilik = nama_pemilik
        self.nama_penghuni = nama_penghuni
        self.harga = harga
        
    def get_dokumen(self):
        return "Bukti kontrak indekos oleh " + self.nama_penghuni + " dari " + self.nama_pemilik + "."

    def get_nama_pemilik(self):
        return self.nama_pemilik

    def get_nama_penghuni(self):
        return self.nama_penghuni
    
    def get_detail(self):
        return "Pemilik : " + self.nama_pemilik + "\nJumlah Kamar : " + str(self.jml_kamar) + "\nHarga Sewa : " + str(self.harga) + "\n"
    
    def get_harga(self):
        return self.harga
