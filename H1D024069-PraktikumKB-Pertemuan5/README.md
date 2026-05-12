# Sistem Pakar Diagnosa Penyakit THT

Aplikasi desktop berbasis **Python Tkinter** yang menggunakan metode **sistem pakar** untuk mendiagnosa kemungkinan penyakit Telinga, Hidung, dan Tenggorokan (THT) berdasarkan gejala yang dialami pengguna.

---

## Deskripsi

Aplikasi ini mengajukan serangkaian pertanyaan terkait gejala yang dialami, kemudian mencocokkan jawaban dengan basis pengetahuan untuk menentukan kemungkinan penyakit THT yang diderita.

---

## Basis Pengetahuan

### Penyakit yang Dapat Didiagnosa

| Kategori | Penyakit |
|----------|----------|
| Infeksi Tenggorokan | Tonsilitis, Faringitis, Abses Peritonsiler, Abses Parafaringeal |
| Sinusitis | Sinusitis Maksilaris, Frontalis, Edmoidalis, Sfenoidalis |
| Gangguan Laring | Laringitis, Kanker Laring, Contact Ulcers |
| Gangguan Telinga | Otitis Media Akut, Barotitis Media, Osteosklerosis, Neuronitis Vestibularis, Meniere, Tumor Syaraf Pendengaran |
| Kanker | Kanker Nasofaring, Kanker Tonsil, Kanker Leher & Kepala, Kanker Leher Metastatik |
| Lainnya | Deviasi Septum, Vertigo Postular |

**Total penyakit:** 23 penyakit

**Total gejala yang dikenali:** 37 gejala

---

## Teknologi

| Teknologi | Keterangan |
|-----------|------------|
| Python | Bahasa pemrograman utama |
| Tkinter | Library GUI bawaan Python |

Tidak memerlukan instalasi library eksternal — hanya membutuhkan Python.

---

## Cara Menjalankan

```bash
python pakar_tht_gui.py
```

---

## Alur Penggunaan

1. Klik **Mulai Diagnosa**
2. Jawab setiap pertanyaan dengan tombol **YA** atau **TIDAK**
3. Setelah 37 pertanyaan selesai, hasil diagnosa akan ditampilkan
4. Segera konsultasikan hasil diagnosa ke dokter THT
5. Klik **Mulai Diagnosa** kembali untuk mengulang

> Aplikasi ini hanya sebagai alat bantu awal. Hasil diagnosa tidak menggantikan pemeriksaan medis profesional.

---

## Struktur Folder

```
H1D024069-PraktikumKB-Pertemuan5/
│
├── pakar_tht_gui.py
└── README.md
```

---

<p align="center"><sub>Praktikum Kecerdasan Buatan — Pertemuan 5</sub></p>
