from apartemen import Apartemen
from rumah import Rumah
from indekos import Indekos
from tkinter import *
from PIL import ImageTk, Image

# Menginstansi properti yang berbeda dan menyimpannya dalam sebuah list
hunians = []
hunians.append(Apartemen("Nelly Joy", 2, 3, "Bandung", "3.000.000/Bulan","images/apt.jpg"))
hunians.append(Rumah("Sekar MK", 5, 5, "Jakarta", 2 , "images/rumah2.jpg"))
hunians.append(Indekos("Bp. Romi", "Cahya", 8, 10,"Gegerkalong, Bandung", "800.000/Bulan", "images/indekos1.jpg"))
hunians.append(Rumah("Satria", 2, 4, "Surabaya", 1, "images/rumah1.jpg"))
hunians.append(Indekos("Bp. Udin", "Riska", 4, 6, "Gegerkalong, Bandung", "850.000/Bulan", "images/indekos2.jpg"))

root = Tk()
root.title("Praktikum DPBO Python")

# Mendefinisikan fungsi untuk membuka tampilan tabel
def open_table():
    landing_frame.pack_forget()  # Sembunyikan frame landing page
    table_frame.pack(padx=10, pady=10)  # Tampilkan frame tabel properti

# Mendefinisikan fungsi untuk menampilkan detail properti
def details(index):
    top = Toplevel()
    top.title("Detail " + hunians[index].get_jenis())

    d_frame = LabelFrame(top, text="Data Residen", padx=10, pady=10)
    d_frame.pack(padx=10, pady=10)

    d_summary = Label(d_frame, text="Summary\n" + hunians[index].get_detail() + hunians[index].get_summary() + "\n" + hunians[index].get_dokumen(), anchor="w", justify=LEFT)
    d_summary.grid(row=0, column=0, sticky="w")
    img = Image.open(hunians[index].get_photo())
    img = img.resize((250, 200)) 
    photo = ImageTk.PhotoImage(img)
    photo_label = Label(d_frame, image=photo)
    photo_label.grid(row=1, column=0, sticky="w")
    photo_label.image = photo  # Simpan referensi ke objek photo untuk mencegah garbage collection

# Frame Landing Page
landing_frame = Frame(root, padx=50, pady=30)
landing_frame.pack(padx=10, pady=10)

landing_label = Label(landing_frame, text="Selamat Datang di ResidenInfo",  font=("Tahoma", 12))
landing_label.pack(padx=10, pady=10)

image_path = "images/welcome-back.png" 

img = Image.open(image_path)
img = img.resize((120, 120)) 
photo = ImageTk.PhotoImage(img)
image_label = Label(landing_frame, image=photo)
image_label.pack(padx=10, pady=10)

start_button = Button(landing_frame, text="Lihat Daftar Residen", command=open_table)
start_button.pack(padx=10, pady=10)

# Frame Tabel Properti Hunian
table_frame = Frame(root, padx=10, pady=10)

frame = LabelFrame(table_frame, text="Data Seluruh Residen", padx=10, pady=10)
frame.pack(padx=10, pady=10)

opts = LabelFrame(table_frame, padx=10, pady=10)
opts.pack(padx=10, pady=10)

b_add = Button(opts, text="Add Data", state="disabled")
b_add.grid(row=0, column=0)

b_exit = Button(opts, text="Exit", command=root.quit)
b_exit.grid(row=0, column=1)

# Menampilkan informasi properti dalam tabel
for index, h in enumerate(hunians):
    idx = Label(frame, text=str(index+1), width=5, borderwidth=1, relief="solid")
    idx.grid(row=index, column=0)

    type = Label(frame, text=h.get_jenis(), width=15, borderwidth=1, relief="solid")
    type.grid(row=index, column=1)

    if h.get_jenis() != "Indekos":
        name = Label(frame, text=" " + h.get_nama_pemilik(), width=40, borderwidth=1, relief="solid", anchor="w")
        name.grid(row=index, column=2)
    else:
        name = Label(frame, text=" " + h.get_nama_penghuni(), width=40, borderwidth=1, relief="solid", anchor="w")
        name.grid(row=index, column=2)

    b_detail = Button(frame, text="Details ", command=lambda index=index: details(index))
    b_detail.grid(row=index, column=3)

root.mainloop()
