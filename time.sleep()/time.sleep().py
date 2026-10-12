import time

# Example: sleep() Method
# Simulasi sistem perpustakaan sedang memproses peminjaman buku ke database
print("Memproses data peminjaman buku ke database pusat...")
time.sleep(2.4)
print("Data peminjaman berhasil disimpan! (Muncul setelah delay 2.4 detik)")

print("-" * 30)

# Create a Digital Clock in Python
# Simulasi jam digital di layar monitor lobi perpustakaan
print("Menjalankan jam digital lobi (Tekan Ctrl+C untuk berhenti)...")

try:
    while True:
        # Mengambil waktu lokal dari sistem komputer
        waktu_sekarang = time.localtime()

        # Memformat tampilan waktu dengan sistem 12 jam (AM/PM)
        jam_terformat = time.strftime("%I:%M:%S %p", waktu_sekarang)

        print("Waktu saat ini:", jam_terformat)

        # Menahan eksekusi program selama 1 detik sebelum mengulang loop
        time.sleep(1)
except KeyboardInterrupt:
    print("\nJam digital perpustakaan dimatikan.")