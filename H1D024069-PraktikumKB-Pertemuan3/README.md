# Pertemuan 3 — Logika Fuzzy

Implementasi sistem inferensi fuzzy dengan library `scikit-fuzzy` pada Python.

---

## Daftar Source Code

### 1. pelayanan_masyarakat.py
Sistem fuzzy untuk menentukan **tingkat kepuasan pelayanan publik** berdasarkan 4 variabel input.

| Variabel | Tipe | Range |
|----------|------|-------|
| Kejelasan Informasi | Input | 0 – 100 |
| Kejelasan Persyaratan | Input | 0 – 100 |
| Kemampuan Petugas | Input | 0 – 100 |
| Ketersediaan Sarana & Prasarana | Input | 0 – 100 |
| Kepuasan Pelayanan | Output | 0 – 400 |

**Contoh input yang digunakan:**
```
Kejelasan Informasi    : 80
Kejelasan Persyaratan  : 60
Kemampuan Petugas      : 50
Ketersediaan Sarpras   : 90
```

---

### 2. `toko_hewan.py`
Sistem fuzzy untuk menentukan **rekomendasi jumlah stok makanan** berdasarkan 4 variabel input.

| Variabel | Tipe | Range |
|----------|------|-------|
| Barang Terjual | Input | 0 – 100 |
| Permintaan | Input | 0 – 300 |
| Harga per Item | Input | 0 – 100.000 |
| Profit | Input | 0 – 4.000.000 |
| Stok Makanan | Output | 0 – 1.000 |

**Contoh input yang digunakan:**
```
Barang Terjual : 80
Permintaan     : 255
Harga per Item : Rp 25.000
Profit         : Rp 3.500.000
```

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
python kepuasan_pelayanan.py
python stok_makanan.py
```

---

## Struktur Folder

```
H1D024069-PraktikumKB-Pertemuan3/
│
├── kepuasan_pelayanan.py
├── stok_makanan.py
└── README.md
```

---

<p align="center"><sub>Praktikum Kecerdasan Buatan — Pertemuan 3</sub></p>
