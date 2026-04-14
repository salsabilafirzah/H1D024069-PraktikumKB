# Sistem Pakar Diagnosa Kerusakan Komputer

Aplikasi desktop berbasis **Python Tkinter** yang menggunakan metode **sistem pakar** untuk mendiagnosa kerusakan komputer berdasarkan gejala yang dialami pengguna.

---

## Deskripsi

Aplikasi ini mengajukan serangkaian pertanyaan terkait gejala yang dialami, kemudian mencocokkan jawaban dengan basis pengetahuan untuk menentukan jenis kerusakan beserta solusinya.

---

## Basis Pengetahuan

### Kerusakan yang Dapat Didiagnosa

| Kerusakan | Gejala yang Dikenali |
|-----------|----------------------|
| RAM Rusak | Blue screen, sering restart, gagal booting |
| Power Supply (PSU) Lemah | Mati sendiri, tidak menyala, restart tiba-tiba |
| Overheat (Prosesor) | Mati sendiri, kipas berisik, lemot parah |
| VGA Bermasalah | Layar blank, artefak layar, resolusi berubah |
| Hardisk Corrupt | Gagal booting, file hilang, loading lama |

### Total Gejala yang Dikenali

13 gejala berbeda yang ditanyakan secara bertahap melalui antarmuka GUI.

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
python pakar_komputer_gui.py
```

---

## Alur Penggunaan

1. Klik **Mulai Diagnosa**
2. Jawab setiap pertanyaan dengan tombol **YA** atau **TIDAK**
3. Setelah 13 pertanyaan selesai, hasil diagnosa dan solusi akan ditampilkan

---

<p align="center"><sub>Praktikum Kecerdasan Buatan — Pertemuan 4</sub></p>
