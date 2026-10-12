# Current time using the datetime object
from datetime import datetime

# Mencatat jam persis saat anggota meminjam buku
waktu_sekarang = datetime.now()
jam_peminjaman = waktu_sekarang.strftime("%H:%M:%S")
print("Jam peminjaman buku tercatat:", jam_peminjaman)

print("-" * 30)

# Current time using time module
import time

# Mencatat log sistem kapan komputer perpustakaan diakses
waktu_lokal_sistem = time.localtime()
jam_log_akses = time.strftime("%H:%M:%S", waktu_lokal_sistem)
print("Log akses komputer perpustakaan pada jam:", jam_log_akses)

print("-" * 30)

# Current time of a Certain timezone
from datetime import datetime
import pytz

# Mengecek jam untuk keperluan pinjam-meminjam buku antar perpustakaan internasional
zona_ny = pytz.timezone('America/New_York')
waktu_ny = datetime.now(zona_ny)
print("Jam server perpustakaan mitra di New York:", waktu_ny.strftime("%H:%M:%S"))

zona_london = pytz.timezone('Europe/London')
waktu_london = datetime.now(zona_london)
print("Jam server perpustakaan mitra di London:", waktu_london.strftime("%H:%M:%S"))