#current date and time
import datetime

waktu_pinjam = datetime.datetime.now()
print("Buku dipinjam pada:", waktu_pinjam)

#current date
import datetime

tanggal_absen = datetime.date.today()
print("Daftar hadir pengunjung tanggal:", tanggal_absen)

#Date object to represent a date
import datetime

tenggat_kembali = datetime.date(2026, 11, 20)
print("Buku harus dikembalikan pada:", tenggat_kembali)

#Get the current date using today
from datetime import date

laporan_hari_ini = date.today()
print("Laporan sirkulasi buku tanggal:", laporan_hari_ini)

#Get the date from a timestamp
from datetime import date

timestamp_sistem = 1326244364
tanggal_daftar = date.fromtimestamp(timestamp_sistem)
print("Anggota terdaftar sejak:", tanggal_daftar)

#Print today's year month and day
from datetime import date

hari_ini = date.today()
print("Tahun pembukuan:", hari_ini.year)
print("Bulan rekapitulasi:", hari_ini.month)
print("Tanggal cetak:", hari_ini.day)

#Time object to represent time
from datetime import time

jam_buka = time(8, 0, 0)
jam_tutup = time(16, 30, 0)
print("Perpustakaan buka jam:", jam_buka)
print("Perpustakaan tutup jam:", jam_tutup)

#Print hour minute second and microsecond
from datetime import time

waktu_kunjungan = time(14, 45, 30)
print("Jam masuk:", waktu_kunjungan.hour)
print("Menit masuk:", waktu_kunjungan.minute)
print("Detik masuk:", waktu_kunjungan.second)

#Python datetime object
from datetime import datetime

jadwal_ruang_diskusi = datetime(2026, 10, 15, 10, 30, 0)
print("Booking ruang diskusi dijadwalkan pada:", jadwal_ruang_diskusi)

#Print year month hour minute and timestamp
from datetime import datetime

waktu_kembali = datetime(2026, 10, 12, 13, 15, 0)
print("Tahun kembali:", waktu_kembali.year)
print("Jam kembali:", waktu_kembali.hour)
print("Log sistem timestamp:", waktu_kembali.timestamp())

#Difference between two timedelta objects
from datetime import timedelta

waktu_terlambat_asli = timedelta(days=5, hours=12)
toleransi_terlambat = timedelta(days=3, hours=0)

sisa_waktu_denda = waktu_terlambat_asli - toleransi_terlambat
print("Total durasi yang kena denda:", sisa_waktu_denda)

#Time duration in seconds
from datetime import timedelta

durasi_baca = timedelta(hours=2, minutes=30)
print("Total detik membaca di tempat:", durasi_baca.total_seconds())
