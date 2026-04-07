# PROGRAM SIMULASI KOPI-KOPIAN

# Library 1: random - untuk menentukan takaran kopi
import random

# Library 2: time - untuk efek brewing (seduh)
import time

# Library 3: math - untuk hitung harga
import math

# STRUKTUR DATA: List dan Dictionary
menu_kopi = [
    "Espresso", "Americano", "Cappuccino", 
    "Latte", "Mocha", "Kopi Tubruk"
]

# Dictionary dengan data unik (level kekuatan kopi dan harga)
resep_kopi = {
    "Espresso": {"level": "Sangat Kuat", "harga": 15000, "waktu_seduh": 2},
    "Americano": {"level": "Kuat", "harga": 18000, "waktu_seduh": 3},
    "Cappuccino": {"level": "Sedang", "harga": 20000, "waktu_seduh": 4},
    "Latte": {"level": "Ringan", "harga": 22000, "waktu_seduh": 5},
    "Mocha": {"level": "Manis", "harga": 25000, "waktu_seduh": 6},
    "Kopi Tubruk": {"level": "Extra Strong", "harga": 12000, "waktu_seduh": 2}
}

# Set untuk menyimpan pesanan unik
pesanan_unik = set()

# List untuk menyimpan histori pesanan
histori_pesanan = []

def tampilkan_menu():
    """Menampilkan menu kopi dengan gaya"""
    print("\n" + "="*50)
    print("           KOPI-KOPIAN")
    print("="*50)
    print(f"{'No':<3} {'Menu':<12} {'Level':<15} {'Harga':<10}")
    print("-"*50)
    
    # STRUKTUR KONTROL: Perulangan for dengan enumerate
    for i, kopi in enumerate(menu_kopi, 1):
        data = resep_kopi[kopi]
        print(f"{i:<3} {kopi:<12} {data['level']:<15} Rp{data['harga']:,}")
    print("="*50)

def pesan_kopi():
    """Fungsi untuk memesan kopi"""
    print("\nPESAN KOPI")
    
    tampilkan_menu()
    
    # STRUKTUR KONTROL: Try-except untuk validasi input
    try:
        pilihan = int(input("Pilih nomor menu (1-6): "))
        
        # STRUKTUR KONTROL: Percabangan if-elif
        if 1 <= pilihan <= 6:
            kopi_dipesan = menu_kopi[pilihan-1]
            data_kopi = resep_kopi[kopi_dipesan]
            
            print(f"Anda memesan: {kopi_dipesan}")
            print(f"Level: {data_kopi['level']}")
            
            # Library time: efek brewing (seduh)
            print("\nBrewing", end="")
            for i in range(data_kopi['waktu_seduh']):
                time.sleep(1)
                print(".", end="", flush=True)
            
            # Library random: variasi suhu kopi
            suhu = random.choice(["Panas", "Hangat", "Dingin"])
            
            # STRUKTUR DATA: Menambah ke histori (list)
            pesanan = {
                "kopi": kopi_dipesan,
                "suhu": suhu,
                "harga": data_kopi['harga'],
                "waktu": time.strftime("%H:%M:%S")
            }
            histori_pesanan.append(pesanan)
            
            # STRUKTUR DATA: Menambah ke set (untuk pesanan unik)
            pesanan_unik.add(kopi_dipesan)
            
            print(f"\n{kopi_dipesan} {suhu} siap dinikmati!")
            print(f"Total: Rp{data_kopi['harga']:,}")
            
        else:
            print("Pilihan tidak ada di menu!")
            
    except ValueError:
        print("Masukkan angka yang benar!")

def random_kopi():
    """Library random untuk rekomendasi kopi acak"""
    print("\nFITUR: KOPI ACAK (untuk yang bingung memilih)")
    
    # STRUKTUR KONTROL: Validasi menu kosong
    if menu_kopi:
        # Library random
        kopi_acak = random.choice(menu_kopi)
        data_acak = resep_kopi[kopi_acak]
        
        # Library math: pembulatan harga diskon
        diskon = data_acak['harga'] * 0.1
        harga_diskon = math.floor(data_acak['harga'] - diskon)
        
        print(f"\nRekomendasi hari ini: {kopi_acak}")
        print(f"Level: {data_acak['level']}")
        print(f"Harga normal: Rp{data_acak['harga']:,}")
        print(f"Harga spesial: Rp{harga_diskon:,}")
    else:
        print("Menu kosong...")

def lihat_histori():
    """Melihat histori pesanan"""
    print("\nHISTORI PESANAN")
    
    # STRUKTUR KONTROL: Percabangan untuk cek histori kosong
    if not histori_pesanan:
        print("Belum ada pesanan...")
        return
    
    # STRUKTUR KONTROL: Perulangan for dengan counter
    for idx, pesan in enumerate(histori_pesanan, 1):
        print(f"\n{idx}. {pesan['kopi']} - {pesan['suhu']}")
        print(f"   Rp{pesan['harga']:,} - {pesan['waktu']}")

def statistik_unik():
    """Menampilkan statistik pesanan unik (SET)"""
    print("\nSTATISTIK PESANAN UNIK")
    
    # Menggunakan SET untuk melihat variasi pesanan
    print(f"Jenis kopi yang pernah dipesan: {len(pesanan_unik)} dari {len(menu_kopi)} menu")
    
    # STRUKTUR KONTROL: Percabangan
    if pesanan_unik:
        print("Menu yang sudah pernah dipesan:")
        # Perulangan untuk menampilkan set
        for kopi in sorted(pesanan_unik):
            print(f"   - {kopi}")
        
        # Set operation: difference (menu yang belum pernah dipesan)
        belum_dipesan = set(menu_kopi) - pesanan_unik
        if belum_dipesan:
            print("\nMenu yang belum pernah dipesan:")
            for kopi in sorted(belum_dipesan):
                print(f"   - {kopi}")
    else:
        print("Belum ada yang pesan...")

def main():
    """Program utama"""
    print("="*50)
    print("          SELAMAT DATANG DI KOPI-KOPIAN")
    print("="*50)
    print("Menu yang tersedia:", ", ".join(menu_kopi))
    
    # STRUKTUR KONTROL: Perulangan while untuk menu
    while True:
        print("\n" + "="*30)
        print("        MENU UTAMA")
        print("="*30)
        print("1. Pesan Kopi")
        print("2. Random Kopi")
        print("3. Lihat Histori Pesanan")
        print("4. Statistik Pesanan Unik")
        print("5. Keluar")
        print("="*30)
        
        pilihan = input("Pilih menu (1-5): ")
        
        if pilihan == "1":
            pesan_kopi()
        elif pilihan == "2":
            random_kopi()
        elif pilihan == "3":
            lihat_histori()
        elif pilihan == "4":
            statistik_unik()
        elif pilihan == "5":
            print("\nTerima kasih sudah mampir di Kopi-Kopian!")
            
            # Library time untuk efek keluar
            print("Menutup program", end="")
            for i in range(3):
                time.sleep(0.5)
                print(".", end="", flush=True)
            break
        else:
            print("Pilihan tidak valid!")

# Jalankan program
if __name__ == "__main__":
    main()