# LP9DPBO2023C2
## Janji
Saya Riska Nurohmah [2109103] mengerjakan Latihan Praktikum 9 dalam mata kuliah Desain dan Pemrograman Berorientasi Objek untuk keberkahanNya maka saya tidak melakukan kecurangan seperti yang telah dispesifikasikan. Aamiin.

## Deskripsi Soal
Latihan Praktikum tidak menggunakan Database, tapi harus mengirim bukti
screenshot menjalankan contoh kode yang dikirim.

**Spesifikasi:**
* Lengkapi fitur summary
* Buat landing Page (button yg ngarah ke halaman daftar residen)
* Tampilin gambar
* Tambahin 1 metode yang masih relevan untuk setiap kelas
 
## Desain dan Alur Program
Program ini merupakan program Python GUI yang menampilkan data residen. Pada program terdapat 4 kelas yaitu:
1. hunian, memiliki atribut jenis, jml_penghuni, jml_kamar, lokasi, path_photo. Pada Class ini terdapat method get_summary dan method get untuk setiap atribut.
2. apartemen, memiliki atribut nama_pemilik, harga_sewa.
3. indekos, memiliki atribut nama_pemilik, nama_penghuni, dan harga.
4. rumah, memiliki atribut nama_pemilik, jml_lantai.

Class apartemen, indekos, dan rumah mempunyai method get_detail dan get_dokumen serta method get untuk setiap atributnya. Class hunian merupakan parent dari Class apartemen, indekos, dan rumah. Sehingga, ketiga kelas tersebut dapat mengakses atribut dan method pada Class hunian.

Program ditampilkan menggunakan virtualenv dan running dilakukan di file main. Ketika program dijalankan maka akan tampil landing page, ketika ditekan button pada landing page maka akan tampil tabel daftar residen dan user dapat melihat details dari residen dengan mengklik button details pada data residen yang ingin dilihat detailnya. Data-data tersebut dimasukan secara hardcode. Untuk keluar dari program dapat dilakukan dengan mengklik button exit atau close window.

## Dokumentasi
### Screenshot Mencoba Database
![coba_database](https://github.com/riskaaa0911/LP9DPBO2023C2/assets/119839421/6cdbfb6b-c283-45a1-91f5-39eb0100d5cc)
### Video Menjalankan Program
https://github.com/riskaaa0911/LP9DPBO2023C2/assets/119839421/d9f6b016-6981-4a7d-a406-7bcebd0f0a22

 


