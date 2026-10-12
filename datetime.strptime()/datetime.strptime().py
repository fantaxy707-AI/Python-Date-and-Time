from datetime import datetime

# Example 1: string to datetime object
teks_tanggal = "21 June, 2026"
objek_tanggal = datetime.strptime(teks_tanggal, "%d %B, %Y")
print("Teks input pendaftaran:", teks_tanggal)
print("Hasil konversi objek:", objek_tanggal)

# Example 2: string to datetime object (Beda format)
teks_waktu = "12/11/2026 09:15:32"
waktu_format_indo = datetime.strptime(teks_waktu, "%d/%m/%Y %H:%M:%S")
print("Format baca Indonesia:", waktu_format_indo)

waktu_format_us = datetime.strptime(teks_waktu, "%m/%d/%Y %H:%M:%S")
print("Format baca Amerika:", waktu_format_us)

# ValueError in strptime()
teks_salah = "12/11/2026"
try:
    objek_salah = datetime.strptime(teks_salah, "%d %m %Y")
except ValueError as e:
    print("Pesan error akibat format salah:", e)