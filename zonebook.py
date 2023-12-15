import datetime as dt

print("="*50)
print("Welcome To".center(50))
print("-ZonaBook-".center(50))
print("="*50)
print("|Menu: \t\t\t\t\t\t|")
print("|\t1. Pembelian\t\t\t\t|")
print("|\t2. Peminjaman\t\t\t\t|")
print("-"*50)

total_semua = 0
harga_buku = []
struk_pembelian = []
i = 0


pilih_menu = int(input("Masukkan[1/2/0-Keluar]: "))
if pilih_menu == 1:
    print("Menu buku kami".center(50))
    print("-"*60)
    print("|Kode\t\tTitle\t\t\tHarga\t\t|")
    print("-" * 60)
    print("UUD\t\tUUD 1945\t\tRp.5000")
    print("DRM\t\tDoraemon\t\tRp.15.000")
    print("NRT\t\tNaruto Shiphuden\tRp.20.000")
    print("DKC\t\tDetektif Conan\t\tRp.25.000")
    print("MK\t\tMalin Kundang\t\tRp.25.000")
    print("SKG\t\tSangkuriang\t\tRp.40.000")
    print("TM\t\tTimun Mas\t\tRp.35.000")
    print("GM\t\tGajah Mada\t\tRp.45.000")
    print("SKNCL\t\tSiKancil\t\tRp.30.000")
    print("G30\t\tPemberontakan PKI\tRp.100.000")
    print("-" * 60)

    jenis_ke = int(input("Banyak jenis buku yang ingin di beli : "))

    # perulangan
    while i < (jenis_ke):
        print("Pembelian Ke - ", i+1)
        beli_buku = input("Masukkan kode: ")
        beli_berapa = int(input("Mau beli berapa: "))

        if beli_buku == "NRT" or beli_buku == "nrt":
            title_buku = "Naruto Shiphuden"
            harga_buku = 20000
        elif beli_buku == "DKC" or beli_buku == "dkc":
            title_buku = "Detektif Conan"
            harga_buku = 25000
        elif beli_buku == "DRM" or beli_buku == "drm":
            title_buku = "Doraemon"
            harga_buku = 15000
        elif beli_buku == "MK" or beli_buku == "mk":
            title_buku = "Malin Kundang"
            harga_buku = 25000
        elif beli_buku == "SKG" or beli_buku == "skg":
            title_buku = "Sangkuriang"
            harga_buku = 40000
        elif beli_buku == "TM" or beli_buku == "tm":
            title_buku = "Timun Mas"
            harga_buku = 35000
        elif beli_buku == "GM" or beli_buku == "gm":
            title_buku = "Gajah Mada"
            harga_buku = 45000
        elif beli_buku == "SKCL" or beli_buku == "skcl":
            title_buku = "SI Kancil"
            harga_buku = 30000
        elif beli_buku == "UUD" or beli_buku == "uud":
            title_buku = "UUD 1945"
            harga_buku = 5000
        elif beli_buku == "G30" or beli_buku == "g30":
            title_buku = "Pemberontakan PKI"
            harga_buku = 100000

        else:
            print("Kode buku tidak valid, Mohon perhatikan kembali!!")
            continue

        # total pembelian
        total_harga = harga_buku * beli_berapa
        total_semua += total_harga

        # memasukkan input ke struk pembelian
        struk_pembelian.append(
            (beli_buku, title_buku, harga_buku, beli_berapa, total_harga)
        )
        i = i + 1

    # struk pembelian
    print("="*65)
    print("STRUK PEMBELIAN".center(60))
    print("-"*65)
    print(f"|Kode\tTitle\t\t         Harga\t      Jumlah\tTotal\t|")
    print("-" * 65)

    # mencetak kemabali detail buku yang dibeli - memasukkan pesanan yang telah dibeli ke struk pembelian
    for pembelian in struk_pembelian:
        beli_buku, title_buku, harga_buku, beli_berapa, total_harga = pembelian
        print(
            f"|{beli_buku:<5}|{title_buku:<20}|Rp.{harga_buku:>8}| {beli_berapa:^15}|Rp.{total_harga:>5,}|")

    print("="*65)
    print("Total Pembayaran untuk", jenis_ke,
          " buku: Rp.{:,}".format(total_semua))

    # kembalian
    uang_bayar = int(input("Masukkan jumlah uang: "))
    kembalian = uang_bayar - total_semua

    # area total
    print("Uang Bayar: Rp.{:,}".format(uang_bayar))
    print("Kembalian: Rp.{:,}".format(kembalian))
    print("="*65)
    print("Terima Kasih Telah Berbelanja :)".center(60))
    print("\t\t\t\t\t\tsalam hormat")
    print("\t\t\t\t\t\t-ZonabookTeam-")

elif pilih_menu == 2:
    print("Menu buku kami".center(50))
    print("-"*60)
    print("|No\tKode\t\tTitle\t\t\t\t|")
    print("-" * 60)
    print("1\tUUD\t\tUUD 1945\t\tRp.5000")
    print("2\tDRM\t\tDoraemon\t\tRp.15.000")
    print("3\tNRT\t\tNaruto Shiphuden\tRp.20.000")
    print("4\tDKC\t\tDetektif Conan\t\tRp.25.000")
    print("5\tMK\t\tMalin Kundang\t\tRp.25.000")
    print("6\tSKG\t\tSangkuriang\t\tRp.40.000")
    print("7\tTM\t\tTimun Mas\t\tRp.35.000")
    print("8\tGM\t\tGajah Mada\t\tRp.45.000")
    print("9\tSKNCL\t\tSiKancil\t\tRp.30.000")
    print("10\tG30\t\tPemberontakan PKI\tRp.100.000")
    print("-" * 60)

    # milih
    minjam_buku = int(input("Pilih buku,Masukkan(No): "))

    # jika minjamBuku sama dengan 1,2,3 maka jalankan. Selain itu Else
    if minjam_buku in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
        print("-"*70)
        print("Data Diri".center(30))
        print("-"*70)
        nama = input("Isi Nama kamu: ")
        nim = int(input("Isi NIM kamu: "))
        telpon = int(input("Masukkan No. Telephone(+62): "))
        tanggal = int(input("pinjam sampai tanggal : "))
        date = dt.date(2023, 12, tanggal)
        hari_ini = dt.date.today()
        hari = date - hari_ini

        # buat munculin di detail peminjaman
        # nama buku
        if minjam_buku == 1:
            judul_buku = "UUD 1945"
        elif minjam_buku == 2:
            judul_buku = "Doraemon"
        elif minjam_buku == 3:
            judul_buku = "Naruto Shippuhen"
        elif minjam_buku == 4:
            judul_buku = "Detektif Conan"
        elif minjam_buku == 5:
            judul_buku = "Malin Kundang"
        elif minjam_buku == 6:
            judul_buku = "Sangkuriang"
        elif minjam_buku == 7:
            judul_buku = "Timun Mas"
        elif minjam_buku == 8:
            judul_buku = "Gajah Mada"
        elif minjam_buku == 9:
            judul_buku = "Si Kancil"
        elif minjam_buku == 10:
            judul_buku = "Pemberontakan PKI"

        # menghitung tanggal pengembalian
        '''deadline = tanggal + 7
        bulan = 12
        tahun = 23'''

        print("="*70)
        print("Detail Peminjaman".center(50))
        print("="*70)
        print(f"Nama: {nama}")
        print(f"NIM: {nim}")
        print(f"No. Telephone(+62): {telpon}")
        print(f"Buku yang dipinjam: {judul_buku}")
        print(f"Tanggal Peminjaman: {hari_ini} -{hari_ini : %A}")
        print(f"Batas Tanggal Pengembalian: {date} -{date : %A}")
        print(f"dipinjam selama  : {hari.days} hari")
        print("="*70)
        print("Note: Jika HILANG/RUSAK/SOBEK, Akan dikenakan denda sebesar Rp.100.000. ")
        print("\t\t\t\t\t\tTerima Kasih")
        print("\t\t\t\t\t\t-ZonabookTeam-")

    else:
        print("Mohon Maaf buku tidak ada")


else:
    print("syntax error! Perhatikan kembali")
