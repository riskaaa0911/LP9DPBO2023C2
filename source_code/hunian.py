class Hunian():
    def __init__(self, jenis, jml_penghuni = 1, jml_kamar = 1, lokasi="Unknown", path_photo="images/welcome-back.png"):
        self.jenis = jenis
        self.jml_penghuni = jml_penghuni
        self.jml_kamar = jml_kamar
        self.lokasi = lokasi
        self.path_photo = path_photo

    def get_jenis(self):
        return self.jenis

    def get_jml_penghuni(self):
        return self.jml_penghuni

    def get_jml_kamar(self):
        return self.jml_kamar

    def get_dokumen(self):
        pass

    def get_summary(self):
        return "Hunian "+ self.jenis +", berlokasi di " + self.lokasi + " dan dihuni oleh " + str(self.jml_penghuni) + " orang."
    
    def get_photo(self):
        return self.path_photo
    
    def get_lokasi(self):
        return self.lokasi
   