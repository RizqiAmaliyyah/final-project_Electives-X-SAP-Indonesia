# Final Project Kelompok 9
## Electives X SAP Indonesia:
### **Kelas Kilat: Membuat Aplikasi Console Pertamamu**

#################################################################################

#film yang sedang tayang
film_tayang = {
    1: "Petualangan Sherina 2",
    2: "A Haunting in Venice",
    3: "The Exorcist",
    4: "EXPEND4BLES"
}

#film yang akan datang
film_akan_datang = {
    1: "Trolls Band Together",
    2: "Freelance",
    3: "Aquaman and the Lost Kingdom",
    4: "Five Nights at Freddy's"
}

#pesan selamat datang
print("=================================================================")
print("=                WowieMovie - Lihat dan rasakan                 =")
print("=                   contactus@wowiemovie.com                    =")
print("=================================================================")
print("Halo! Ada yang bisa dibantu?")

#fitur yang tersedia
while True:
    print("1. Liat Film yang Sedang Tayang")
    print("2. Liat Film yang Akan Datang")
    print("3. Liat Pemesanan yang Sudah Ada")
    print("4. Batal Pemesanan")
    print("5. Keluar")

    pilihan = input("Masukkan Pilihan (1..5): ")

    if pilihan == '1':
      print("Film yang sedang tayang:", film_tayang)
    elif pilihan == '2':
      print("Film yang akan datang", film_akan_datang)
    elif pilihan == '3':
      print("Anda belum memesan tiket apapun, silahkan lakukan pemesanan")
    elif pilihan == '4':
      print("Anda tidak memiliki pemesanan aktif saat ini")
    elif pilihan == '5':
      print("Terima kasih telah melakukan pemesanan tiket di WowieMovie, jika memiliki pertanyaan atau keluhan lainnya hubungi kami melalui email berikut: contactus@wowiemovie.com")
      break
    else:
        print("Pilihan tidak valid. Silakan pilih antara 1 hingga 5.")