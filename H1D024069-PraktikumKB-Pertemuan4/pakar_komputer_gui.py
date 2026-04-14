import tkinter as tk
from tkinter import messagebox

# DATA KERUSAKAN & GEJALA
# Struktur: "Nama Kerusakan": ["gejala1", "gejala2", ...]
database_kerusakan = {
    "RAM Rusak": ["blue_screen", "sering_restart", "gagal_booting"],
    "Power Supply (PSU) Lemah": ["komputer_mati_sendiri", "tidak_menyala", "restart_tiba_tiba"],
    "Overheat (Prosesor)": ["komputer_mati_sendiri", "kipas_berisik", "lemot_parah"],
    "VGA Bermasalah": ["layar_blank", "artefak_layar", "resolusi_berubah"],
    "Hardisk Corrupt": ["gagal_booting", "file_hilang", "loading_lama"],
}

# SOLUSI SINGKAT UNTUK SETIAP KERUSAKAN
solusi_kerusakan = {
    "RAM Rusak": "Coba bersihkan pin RAM dengan penghapus, lalu pasang kembali. Jika masih bermasalah, ganti RAM baru.",
    "Power Supply (PSU) Lemah": "Periksa kabel daya dan konektor PSU. Jika voltase tidak stabil, segera ganti PSU.",
    "Overheat (Prosesor)": "Bersihkan debu pada heatsink dan kipas. Ganti thermal paste prosesor jika sudah kering.",
    "VGA Bermasalah": "Pasang ulang kartu VGA dan bersihkan slotnya. Coba update atau reinstall driver VGA.",
    "Hardisk Corrupt": "Jalankan perintah CHKDSK untuk memperbaiki sektor bad. Segera backup data dan pertimbangkan ganti HDD/SSD.",
}

# DAFTAR SEMUA GEJALA UNTUK PERTANYAAN
semua_gejala = [
    ("blue_screen",        "Apakah komputer/laptop sering mengalami Blue Screen (BSOD)?"),
    ("sering_restart",     "Apakah komputer/laptop sering restart dengan sendirinya?"),
    ("gagal_booting",      "Apakah komputer/laptop gagal atau lama saat proses booting?"),
    ("komputer_mati_sendiri", "Apakah komputer/laptop tiba-tiba mati sendiri saat digunakan?"),
    ("tidak_menyala",      "Apakah komputer/laptop tidak menyala sama sekali saat ditekan tombol power?"),
    ("restart_tiba_tiba",  "Apakah komputer/laptop restart tanpa peringatan saat beban kerja tinggi?"),
    ("kipas_berisik",      "Apakah kipas pendingin terdengar sangat berisik atau berputar cepat terus-menerus?"),
    ("lemot_parah",        "Apakah performa komputer/laptop sangat lemot meskipun program ringan?"),
    ("layar_blank",        "Apakah layar menjadi blank/hitam saat komputer menyala?"),
    ("artefak_layar",      "Apakah muncul garis, kotak, atau warna aneh di layar?"),
    ("resolusi_berubah",   "Apakah resolusi layar berubah sendiri atau tampilan buram?"),
    ("file_hilang",        "Apakah ada file/folder yang tiba-tiba hilang atau tidak bisa dibuka?"),
    ("loading_lama",       "Apakah membuka file atau program membutuhkan waktu sangat lama?"),
]


class AplikasiPakar:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistem Pakar Diagnosa Kerusakan Komputer")
        self.gejala_terpilih = []
        self.index_pertanyaan = 0

        # Label Judul
        self.label_judul = tk.Label(
            root,
            text="Sistem Pakar Diagnosa Komputer",
            font=("Arial", 14, "bold"),
            fg="#2c3e50"
        )
        self.label_judul.pack(pady=(15, 5))

        # Label Pertanyaan
        self.label_tanya = tk.Label(
            root,
            text="Selamat Datang di Sistem Pakar",
            font=("Arial", 11),
            wraplength=440,
            justify="center"
        )
        self.label_tanya.pack(pady=20)

        # Tombol Mulai
        self.btn_mulai = tk.Button(
            root,
            text="Mulai Diagnosa",
            command=self.mulai_tanya,
            bg="#2980b9",
            fg="white",
            font=("Arial", 11, "bold"),
            relief="flat",
            padx=15,
            cursor="hand2"
        )
        self.btn_mulai.pack(pady=10)

        # Frame Tombol Jawaban (Disembunyikan di awal)
        self.frame_jawaban = tk.Frame(root)
        self.btn_ya = tk.Button(
            self.frame_jawaban,
            text="YA",
            width=10,
            command=lambda: self.jawab('y'),
            bg="#27ae60",
            fg="white",
            font=("Arial", 10, "bold"),
            relief="flat",
            cursor="hand2"
        )
        self.btn_tidak = tk.Button(
            self.frame_jawaban,
            text="TIDAK",
            width=10,
            command=lambda: self.jawab('t'),
            bg="#e74c3c",
            fg="white",
            font=("Arial", 10, "bold"),
            relief="flat",
            cursor="hand2"
        )
        self.btn_ya.pack(side=tk.LEFT, padx=10)
        self.btn_tidak.pack(side=tk.LEFT, padx=10)

    def mulai_tanya(self):
        self.gejala_terpilih = []
        self.index_pertanyaan = 0
        self.btn_mulai.pack_forget()
        self.frame_jawaban.pack(pady=20)
        self.tampilkan_pertanyaan()

    def tampilkan_pertanyaan(self):
        if self.index_pertanyaan < len(semua_gejala):
            kode, teks = semua_gejala[self.index_pertanyaan]
            self.label_tanya.config(
                text=f"Pertanyaan {self.index_pertanyaan + 1} dari {len(semua_gejala)}\n\n{teks}"
            )
        else:
            self.proses_hasil()

    def jawab(self, respon):
        if respon == 'y':
            kode = semua_gejala[self.index_pertanyaan][0]
            self.gejala_terpilih.append(kode)

        self.index_pertanyaan += 1
        self.tampilkan_pertanyaan()

    def proses_hasil(self):
        hasil = []
        for kerusakan, syarat in database_kerusakan.items():
            # Cek apakah gejala_terpilih mengandung semua syarat kerusakan
            if all(s in self.gejala_terpilih for s in syarat):
                hasil.append(kerusakan)

        if hasil:
            pesan = ""
            for kerusakan in hasil:
                solusi = solusi_kerusakan.get(kerusakan, "Konsultasikan ke teknisi.")
                pesan += f"🔧 {kerusakan}\n   Solusi: {solusi}\n\n"
            messagebox.showinfo(
                "Hasil Diagnosa",
                f"Berdasarkan gejala Anda, terdeteksi:\n\n{pesan.strip()}"
            )
        else:
            messagebox.showinfo(
                "Hasil Diagnosa",
                "Tidak terdeteksi kerusakan spesifik.\n\nSaran: Coba bawa ke teknisi untuk pemeriksaan lebih lanjut."
            )

        # Reset ke awal
        self.frame_jawaban.pack_forget()
        self.btn_mulai.pack(pady=10)
        self.label_tanya.config(text="Diagnosa Selesai. Ingin mengulang?")


# Menjalankan Aplikasi
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("480x280")
    root.resizable(False, False)
    app = AplikasiPakar(root)
    root.mainloop()