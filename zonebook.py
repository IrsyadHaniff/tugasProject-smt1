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
    print("NRT\t\tNaruto Shiphuden\tRp.25.000")
    print("DKC\t\tDetektif Conan\t\tRp.30.000")
    print("DRM\t\tDoraemon\t\tRp.35.000")
    print("-" * 60)

    jenis_ke = int(input("Banyak jenis buku yang ingin di beli : "))

    # perulangan
    while i < (jenis_ke):
        print("Jenis Ke - ", i+1)
        beli_buku = input("Masukkan kode[NRT/DKC/DRM]: ")
        beli_berapa = int(input("Mau beli berapa: "))

        if beli_buku == "NRT" or beli_buku == "nrt":
            title_buku = "Naruto Shiphuden"
            harga_buku = 25000
        elif beli_buku == "DKC" or beli_buku == "dkc":
            title_buku = "Detektif Conan"
            harga_buku = 30000
        elif beli_buku == "DRM" or beli_buku == "drm":
            title_buku = "Doraemon            "
            harga_buku = 35000
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

    # mencetak kemabali detail buku yang dibeli
    for pembelian in struk_pembelian:
        beli_buku, title_buku, harga_buku, beli_berapa, total_harga = pembelian
        print(beli_buku,"\t",title_buku,"\t Rp{:,}".format(harga_buku),"\t",beli_berapa,"\tRp{:,}".format(total_harga))

    print("="*65)
    print("Total Pembayaran untuk",jenis_ke," buku: Rp.{:,}".format(total_semua))

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
    print("1\tNRT\t\tNaruto Shiphuden")
    print("2\tDKC\t\tDetektif Conan")
    print("3\tDRM\t\tDoraemon")
    print("-" * 60)

    # milih
    minjam_buku = int(input("Pilih buku,Masukkan [1/2/3/0-keluar]: "))

    # jika minjamBuku sama dengan 1,2,3 maka jalankan. Selain itu Else
    if minjam_buku in [1, 2, 3]:
        print("-"*70)
        print("Data Diri".center(30))
        print("-"*70)
        nama = input("Isi Nama kamu: ")
        nim = int(input("Isi NIM kamu: "))
        tanggal = int(input("pinjam sampai tanggal : "))
        date = dt.date(2023,12,tanggal)
        hari_ini = dt.date.today()
        hari = date - hari_ini
        
        # buat munculin di detail peminjaman
        # nama buku
        if minjam_buku == 1:
            judul_buku = "Naruto Shippuden"
        elif minjam_buku == 2:
            judul_buku = "Detektif Conan"
        elif minjam_buku == 3:
            judul_buku = "Doraemon"

        # menghitung tanggal pengembalian
        '''deadline = tanggal + 7
        bulan = 12
        tahun = 23'''

        print("="*70)
        print("Detail Peminjaman".center(50))
        print("="*70)
        print(f"Nama: {nama}")
        print(f"NIM: {nim}")
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
