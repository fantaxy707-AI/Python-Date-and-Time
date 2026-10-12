from datetime import date
from datetime import datetime

# Example 1: Python get today's date
hari_ini = date.today()
print("Tanggal operasional perpustakaan:", hari_ini)
print("-" * 30)

# Example 2: Current date in different formats
# Format untuk keperluan cetak laporan peminjaman buku harian
format_1 = hari_ini.strftime("%d/%m/%Y")
print("Format laporan 1 (dd/mm/YYYY):", format_1)

format_2 = hari_ini.strftime("%B %d, %Y")
print("Format laporan 2 (Bulan penuh):", format_2)

format_3 = hari_ini.strftime("%m/%d/%y")
print("Format laporan 3 (Bulan/Hari/Tahun pendek):", format_3)

format_4 = hari_ini.strftime("%b-%d-%Y")
print("Format laporan 4 (Singkatan bulan):", format_4)
print("-" * 30)

# Example 3: Get the current date and time in Python
# Mencatat waktu pasti saat anggota mengembalikan buku di meja kasir
waktu_kembali = datetime.now()
print("Objek waktu pengembalian buku:", waktu_kembali)

waktu_struk = waktu_kembali.strftime("%d/%m/%Y %H:%M:%S")
print("Waktu tercatat di struk peminjaman:", waktu_struk)