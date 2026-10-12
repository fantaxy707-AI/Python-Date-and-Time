import time

# Python time.time() Function
# Mencatat waktu timestamp saat barcode buku di-scan
detik_scan = time.time()
print("Timestamp scan barcode buku:", detik_scan)

print("-" * 30)

# Python time.ctime() Function
# Mengubah timestamp dari database menjadi waktu yang bisa dibaca admin perpustakaan
timestamp_log = 1672215379.5045543
waktu_lokal_admin = time.ctime(timestamp_log)
print("Waktu log akses anggota:", waktu_lokal_admin)

print("-" * 30)

# Python time.sleep() Function
# Simulasi jeda waktu saat sistem sedang memproses pencarian buku di database
print("Sistem sedang mencari buku di database...")
time.sleep(2.4)
print("Pencarian selesai setelah loading 2.4 detik.")

print("-" * 30)

# Python time.localtime() Function
# Mendapatkan detail waktu lokal untuk data peminjaman buku
waktu_lokal_pinjam = time.localtime(1672214933)
print("Struktur data peminjaman (Lokal):", waktu_lokal_pinjam)
print("Tahun peminjaman:", waktu_lokal_pinjam.tm_year)
print("Jam peminjaman:", waktu_lokal_pinjam.tm_hour)

print("-" * 30)

# Python time.gmtime() Function
# Mendapatkan detail waktu UTC untuk sinkronisasi server perpustakaan pusat
waktu_utc_sinkron = time.gmtime(1672214933)
print("Struktur data sinkronisasi (UTC):", waktu_utc_sinkron)
print("Jam sinkronisasi (UTC):", waktu_utc_sinkron.tm_hour)

print("-" * 30)

# Python time.mktime() Function
# Mengubah input jadwal batas pengembalian (bentuk tuple) menjadi timestamp
# Format tuple: (year, month, day, hour, minute, second, weekday, day of year, daylight saving)
tuple_batas_kembali = (2026, 12, 28, 8, 44, 4, 4, 362, 0)
timestamp_batas = time.mktime(tuple_batas_kembali)
print("Timestamp batas pengembalian buku:", timestamp_batas)

print("-" * 30)

# Python time.asctime() Function
# Mengubah tuple jadwal batas pengembalian tadi menjadi string biasa
tuple_waktu = (2026, 12, 28, 8, 44, 4, 4, 362, 0)
waktu_baca = time.asctime(tuple_waktu)
print("Batas waktu dalam teks struk:", waktu_baca)

print("-" * 30)

# Python time.strftime() Function
# Memformat waktu lokal sistem untuk dicetak di bukti peminjaman
struktur_waktu_sekarang = time.localtime()
struk_format = time.strftime("%d/%m/%Y, %H:%M:%S", struktur_waktu_sekarang)
print("Waktu cetak bukti peminjaman:", struk_format)

print("-" * 30)

# Python time.strptime() Function
# Mengubah input teks dari form pengembalian di website menjadi struktur waktu sistem
input_form = "14 July, 2026"
struktur_hasil_input = time.strptime(input_form, "%d %B, %Y")
print("Data form pengembalian setelah diproses backend:", struktur_hasil_input)