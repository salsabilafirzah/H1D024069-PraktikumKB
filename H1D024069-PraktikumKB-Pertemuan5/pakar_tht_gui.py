import tkinter as tk
from tkinter import messagebox

# ============================================================
# DATA PENYAKIT THT & GEJALA
# ============================================================
database_penyakit = {
    "Tonsilitis":                   ["G37", "G12", "G5",  "G27", "G6",  "G21"],
    "Sinusitis Maksilaris":         ["G37", "G12", "G27", "G17", "G33", "G36", "G29"],
    "Sinusitis Frontalis":          ["G37", "G12", "G27", "G17", "G33", "G36", "G21", "G26"],
    "Sinusitis Edmoidalis":         ["G37", "G12", "G27", "G17", "G33", "G36", "G21", "G30", "G13", "G26"],
    "Sinusitis Sfenoidalis":        ["G37", "G12", "G27", "G17", "G33", "G36", "G29", "G7"],
    "Abses Peritonsiler":           ["G37", "G12", "G6",  "G15", "G2",  "G29", "G10"],
    "Faringitis":                   ["G37", "G5",  "G6",  "G7",  "G15"],
    "Kanker Laring":                ["G5",  "G27", "G6",  "G15", "G2",  "G19", "G1"],
    "Deviasi Septum":               ["G37", "G17", "G20", "G8",  "G18", "G25"],
    "Laringitis":                   ["G37", "G5",  "G15", "G16", "G32"],
    "Kanker Leher & Kepala":        ["G5",  "G22", "G8",  "G28", "G3",  "G11"],
    "Otitis Media Akut":            ["G37", "G20", "G35", "G31"],
    "Contact Ulcers":               ["G5",  "G2"],
    "Abses Parafaringeal":          ["G5",  "G16"],
    "Barotitis Media":              ["G12", "G20"],
    "Kanker Nasofaring":            ["G17", "G8"],
    "Kanker Tonsil":                ["G6",  "G29"],
    "Neuronitis Vestibularis":      ["G35", "G24"],
    "Meniere":                      ["G20", "G35", "G14", "G4"],
    "Tumor Syaraf Pendengaran":     ["G12", "G34", "G23"],
    "Kanker Leher Metastatik":      ["G29"],
    "Osteosklerosis":               ["G34", "G9"],
    "Vertigo Postular":             ["G24"],
}

# ============================================================
# DAFTAR SEMUA GEJALA 
# ============================================================
semua_gejala = [
    ("G1",  "Apakah Anda mengalami nafas yang abnormal (sesak/tidak normal)?"),
    ("G2",  "Apakah Anda mengalami suara serak?"),
    ("G3",  "Apakah ada perubahan kulit yang tidak biasa pada tubuh Anda?"),
    ("G4",  "Apakah telinga Anda terasa penuh atau tersumbat?"),
    ("G5",  "Apakah Anda merasakan nyeri saat bicara atau menelan?"),
    ("G6",  "Apakah Anda merasakan nyeri tenggorokan?"),
    ("G7",  "Apakah Anda merasakan nyeri di area leher?"),
    ("G8",  "Apakah hidung Anda mengalami pendarahan (mimisan)?"),
    ("G9",  "Apakah telinga Anda terdengar berdenging?"),
    ("G10", "Apakah air liur Anda menetes secara tidak terkontrol?"),
    ("G11", "Apakah ada perubahan suara yang tidak wajar pada Anda?"),
    ("G12", "Apakah Anda mengalami sakit kepala?"),
    ("G13", "Apakah ada nyeri di pinggir hidung?"),
    ("G14", "Apakah Anda mengalami serangan vertigo (pusing berputar)?"),
    ("G15", "Apakah kelenjar getah bening Anda terasa membesar?"),
    ("G16", "Apakah leher Anda terasa bengkak?"),
    ("G17", "Apakah hidung Anda tersumbat?"),
    ("G18", "Apakah Anda mengalami infeksi sinus sebelumnya?"),
    ("G19", "Apakah berat badan Anda turun secara tidak wajar?"),
    ("G20", "Apakah Anda merasakan nyeri pada telinga?"),
    ("G21", "Apakah selaput lendir di tenggorokan/mulut tampak kemerahan?"),
    ("G22", "Apakah ada benjolan di leher Anda?"),
    ("G23", "Apakah tubuh Anda sering terasa tidak seimbang?"),
    ("G24", "Apakah bola mata Anda bergerak tidak terkontrol?"),
    ("G25", "Apakah Anda merasakan nyeri di area wajah?"),
    ("G26", "Apakah dahi Anda terasa sakit atau berdenyut?"),
    ("G27", "Apakah Anda mengalami batuk?"),
    ("G28", "Apakah ada sesuatu yang tumbuh / benjolan di dalam mulut?"),
    ("G29", "Apakah ada benjolan yang terasa di leher Anda?"),
    ("G30", "Apakah ada nyeri di area antara kedua mata?"),
    ("G31", "Apakah gendang telinga Anda meradang atau terasa sakit?"),
    ("G32", "Apakah tenggorokan Anda terasa gatal?"),
    ("G33", "Apakah hidung Anda meler (keluar cairan)?"),
    ("G34", "Apakah Anda mengalami penurunan pendengaran / tuli?"),
    ("G35", "Apakah Anda mengalami mual atau muntah?"),
    ("G36", "Apakah Anda merasa mudah lelah atau lesu belakangan ini?"),
    ("G37", "Apakah Anda sedang atau baru saja mengalami demam?"),
]


# ============================================================
# KELAS APLIKASI
# ============================================================
class AplikasiPakar:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistem Pakar Diagnosa Penyakit THT")
        self.gejala_terpilih = []
        self.index_pertanyaan = 0

        # ---- Header ----
        self.label_judul = tk.Label(
            root,
            text="Sistem Pakar Diagnosa Penyakit THT",
            font=("Arial", 13, "bold"),
            fg="#1a5276"
        )
        self.label_judul.pack(pady=(15, 2))

        self.label_sub = tk.Label(
            root,
            text="(Telinga, Hidung, Tenggorokan)",
            font=("Arial", 10, "italic"),
            fg="#555555"
        )
        self.label_sub.pack(pady=(0, 10))

        # ---- Label Pertanyaan ----
        self.label_tanya = tk.Label(
            root,
            text="Selamat Datang di Sistem Pakar THT\nTekan tombol di bawah untuk memulai diagnosa.",
            font=("Arial", 11),
            wraplength=460,
            justify="center"
        )
        self.label_tanya.pack(pady=20)

        # ---- Progress Label ----
        self.label_progress = tk.Label(
            root,
            text="",
            font=("Arial", 9),
            fg="#888888"
        )
        self.label_progress.pack()

        # ---- Tombol Mulai ----
        self.btn_mulai = tk.Button(
            root,
            text="Mulai Diagnosa",
            command=self.mulai_tanya,
            bg="#1a5276",
            fg="white",
            font=("Arial", 11, "bold"),
            relief="flat",
            padx=18,
            pady=6,
            cursor="hand2"
        )
        self.btn_mulai.pack(pady=15)

        # ---- Frame Tombol Jawaban (Disembunyikan di awal) ----
        self.frame_jawaban = tk.Frame(root)
        self.btn_ya = tk.Button(
            self.frame_jawaban,
            text="YA",
            width=12,
            command=lambda: self.jawab('y'),
            bg="#1e8449",
            fg="white",
            font=("Arial", 11, "bold"),
            relief="flat",
            cursor="hand2"
        )
        self.btn_tidak = tk.Button(
            self.frame_jawaban,
            text="TIDAK",
            width=12,
            command=lambda: self.jawab('t'),
            bg="#c0392b",
            fg="white",
            font=("Arial", 11, "bold"),
            relief="flat",
            cursor="hand2"
        )
        self.btn_ya.pack(side=tk.LEFT, padx=12)
        self.btn_tidak.pack(side=tk.LEFT, padx=12)

    # ----------------------------------------------------------
    def mulai_tanya(self):
        self.gejala_terpilih = []
        self.index_pertanyaan = 0
        self.btn_mulai.pack_forget()
        self.frame_jawaban.pack(pady=20)
        self.tampilkan_pertanyaan()

    # ----------------------------------------------------------
    def tampilkan_pertanyaan(self):
        if self.index_pertanyaan < len(semua_gejala):
            kode, teks = semua_gejala[self.index_pertanyaan]
            self.label_tanya.config(text=teks)
            self.label_progress.config(
                text=f"Pertanyaan {self.index_pertanyaan + 1} dari {len(semua_gejala)}"
            )
        else:
            self.proses_hasil()

    # ----------------------------------------------------------
    def jawab(self, respon):
        if respon == 'y':
            kode = semua_gejala[self.index_pertanyaan][0]
            self.gejala_terpilih.append(kode)

        self.index_pertanyaan += 1
        self.tampilkan_pertanyaan()

    # ----------------------------------------------------------
    def proses_hasil(self):
        hasil = []
        for penyakit, syarat in database_penyakit.items():
            # Cek apakah semua gejala syarat ada dalam gejala yang dipilih
            if all(s in self.gejala_terpilih for s in syarat):
                hasil.append(penyakit)

        kesimpulan = ", ".join(hasil) if hasil else None

        if kesimpulan:
            messagebox.showinfo(
                "Hasil Diagnosa",
                f"Berdasarkan gejala Anda:\n\n"
                f"✅ Kemungkinan Penyakit:\n{kesimpulan}\n\n"
                f"⚠️ Harap segera konsultasikan ke dokter THT."
            )
        else:
            messagebox.showinfo(
                "Hasil Diagnosa",
                "Tidak terdeteksi penyakit THT yang cocok.\n\n"
                "Kemungkinan gejala belum cukup spesifik.\n"
                "Disarankan untuk berkonsultasi ke dokter."
            )

        # Reset ke awal
        self.frame_jawaban.pack_forget()
        self.label_progress.config(text="")
        self.btn_mulai.pack(pady=15)
        self.label_tanya.config(
            text="Diagnosa Selesai.\nIngin melakukan diagnosa ulang?"
        )


# ============================================================
# Menjalankan Aplikasi
# ============================================================
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("500x300")
    root.resizable(False, False)
    app = AplikasiPakar(root)
    root.mainloop()