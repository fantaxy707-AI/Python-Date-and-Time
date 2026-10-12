# Example 1: datetime to string using strftime()
from datetime import datetime

waktu_transaksi = datetime.now() # Waktu saat buku diproses di kasir

tahun_transaksi = waktu_transaksi.strftime("%Y")
print("Tahun transaksi:", tahun_transaksi)

bulan_transaksi = waktu_transaksi.strftime("%m")
print("Bulan transaksi:", bulan_transaksi)

hari_transaksi = waktu_transaksi.strftime("%d")
print("Hari transaksi:", hari_transaksi)

jam_transaksi = waktu_transaksi.strftime("%H:%M:%S")
print("Jam transaksi:", jam_transaksi)

waktu_lengkap = waktu_transaksi.strftime("%m/%d/%Y, %H:%M:%S")
print("Waktu transaksi dicetak di struk:", waktu_lengkap)

print("-" * 30)

# Example 2: Creating string from a timestamp
from datetime import datetime

# Anggap ini data timestamp log sistem saat sebuah buku donasi didaftarkan
timestamp_donasi = 1528797322
waktu_donasi = datetime.fromtimestamp(timestamp_donasi)
print("Objek waktu donasi buku:", waktu_donasi)

format_1 = waktu_donasi.strftime("%m/%d/%Y, %H:%M:%S")
print("Format log 1:", format_1)

format_2 = waktu_donasi.strftime("%d %b, %Y")
print("Format log 2:", format_2)

format_3 = waktu_donasi.strftime("%d %B, %Y")
print("Format log 3:", format_3)

format_4 = waktu_donasi.strftime("%I%p")
print("Format log 4 (Jam masuk):", format_4)

print("-" * 30)

# Example 3: Locale's appropriate date and time
from datetime import datetime

# Timestamp saat akun anggota perpustakaan dibuat
timestamp_daftar = 1528797322
waktu_daftar = datetime.fromtimestamp(timestamp_daftar)

# %c, %x, dan %X akan menyesuaikan dengan pengaturan bahasa/region di komputer lo
format_lokal_lengkap = waktu_daftar.strftime("%c")
print("Waktu daftar (lokal lengkap):", format_lokal_lengkap)

format_lokal_tanggal = waktu_daftar.strftime("%x")
print("Tanggal daftar (lokal):", format_lokal_tanggal)

format_lokal_jam = waktu_daftar.strftime("%X")
print("Jam daftar (lokal):", format_lokal_jam)