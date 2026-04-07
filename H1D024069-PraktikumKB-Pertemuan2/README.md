# Pertemuan 2 — Logika Fuzzy: Sistem Kendali Kipas Angin

Implementasi sistem inferensi fuzzy sederhana menggunakan metode **Mamdani** untuk menentukan kecepatan kipas angin berdasarkan suhu dan kelembapan.

---

## Source Code

### kipas_angin.py
Sistem fuzzy berbasis CLI yang menerima input suhu dan kelembapan, lalu menghitung rekomendasi kecepatan kipas secara otomatis.

---

## Variabel Fuzzy

| Variabel | Tipe | Range |
|----------|------|-------|
| Suhu | Input | 0 – 40 °C |
| Kelembapan | Input | 0 – 100 % |
| Kecepatan Kipas | Output | 0 – 100 |

**Fungsi keanggotaan:** Segitiga (trimf)

| Variabel | Himpunan |
|----------|----------|
| Suhu | Dingin · Sejuk · Panas |
| Kelembapan | Kering · Normal · Lembap |
| Kecepatan | Lambat · Sedang · Cepat |

---

## Aturan Fuzzy

| Aturan | Kondisi | Output |
|--------|---------|--------|
| 1 | Suhu Dingin **AND** Kelembapan Kering | Kecepatan Lambat |
| 2 | Suhu Sejuk **OR** Kelembapan Normal | Kecepatan Sedang |
| 3 | Suhu Panas **OR** Kelembapan Lembap | Kecepatan Cepat |

---

## Requirements

```
numpy
scikit-fuzzy
matplotlib
```

Install dengan:

```bash
pip install numpy scikit-fuzzy matplotlib
```

---

## Cara Menjalankan

```bash
python kipas_angin.py
```

Program akan menampilkan grafik himpunan fuzzy terlebih dahulu, kemudian meminta input suhu dan kelembapan, lalu menampilkan hasil kecepatan kipas beserta grafiknya.

---

## Struktur Folder

```
H1D024069-PraktikumKB-Pertemuan2/
│
├── kipas_angin.py
└── README.md
```

---

<p align="center"><sub>Praktikum Kecerdasan Buatan — Pertemuan 2</sub></p>
