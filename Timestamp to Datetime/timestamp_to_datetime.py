# Python timestamp to datetime
from datetime import datetime

# Timestamp dari log sistem saat anggota baru mendaftar perpustakaan
timestamp_daftar = 1545730073
waktu_daftar = datetime.fromtimestamp(timestamp_daftar)

print("Waktu pendaftaran anggota:", waktu_daftar)
print("Tipe data waktu:", type(waktu_daftar))

print("-" * 30)

# Python datetime to timestamp
from datetime import datetime

# Mengubah waktu peminjaman buku saat ini menjadi timestamp untuk disimpan di database
waktu_pinjam = datetime.now()
timestamp_database = datetime.timestamp(waktu_pinjam)

print("Waktu transaksi saat ini:", waktu_pinjam)
print("Log timestamp untuk database:", timestamp_database)