from hunian import Hunian

class Rumah(Hunian):
    def __init__(self, nama_pemilik, jml_penghuni, jml_kamar, lokasi, jml_lantai, path_photo):
        super().__init__("Rumah", jml_penghuni, jml_kamar, lokasi, path_photo)
        self.nama_pemilik = nama_pemilik
        self.jml_lantai = jml_lantai

    def get_dokumen(self):
        return "Izin Mendirikan Bangunan (IMB) a/n " + self.nama_pemilik

    def get_nama_pemilik(self):
        return self.nama_pemilik
    
    def get_detail(self):
        return "Pemilik : " + self.nama_pemilik + "\nJumlah Kamar : " + str(self.jml_kamar) + "\nJumlah Lantai : " + str(self.jml_lantai) + "\n"
    
    def get_jmlLantai(self):
        return self.jml_lantai