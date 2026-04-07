# Import library
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Menyiapkan himpunan Fuzzy
suhu = ctrl.Antecedent(np.arange(0, 41), 'suhu')
kelembapan = ctrl.Antecedent(np.arange(0, 101), 'kelembapan')
kecepatan = ctrl.Consequent(np.arange(0, 101), 'kecepatan')

# Suhu (0-40 derajat Celcius)
suhu['Dingin'] = fuzz.trimf(suhu.universe, [0, 0, 20])
suhu['Sejuk']  = fuzz.trimf(suhu.universe, [10, 20, 30])
suhu['Panas']  = fuzz.trimf(suhu.universe, [20, 40, 40])

# Kelembapan (0-100 persen)
kelembapan['Kering'] = fuzz.trimf(kelembapan.universe, [0, 0, 50])
kelembapan['Normal'] = fuzz.trimf(kelembapan.universe, [25, 50, 75])
kelembapan['Lembap'] = fuzz.trimf(kelembapan.universe, [50, 100, 100])

# Kecepatan kipas (0-100)
kecepatan['Lambat'] = fuzz.trimf(kecepatan.universe, [0, 0, 50])
kecepatan['Sedang'] = fuzz.trimf(kecepatan.universe, [25, 50, 75])
kecepatan['Cepat']  = fuzz.trimf(kecepatan.universe, [50, 100, 100])

# Tampilkan grafik himpunan fuzzy dulu
suhu.view()
kelembapan.view()
kecepatan.view()
input("Tekan ENTER untuk melanjutkan...")

# Aturan Fuzzy
aturan1 = ctrl.Rule(suhu['Dingin'] & kelembapan['Kering'], kecepatan['Lambat'])
aturan2 = ctrl.Rule(suhu['Sejuk']  | kelembapan['Normal'], kecepatan['Sedang'])
aturan3 = ctrl.Rule(suhu['Panas']  | kelembapan['Lembap'], kecepatan['Cepat'])

# Membuat Inference Engine dan Sistem Fuzzy
engine = ctrl.ControlSystem([aturan1, aturan2, aturan3])
system = ctrl.ControlSystemSimulation(engine)

# Input dari user
print("=== Sistem Kecepatan Kipas Angin ===")
input_suhu       = float(input("Masukkan nilai suhu (0-40 C)       : "))
input_kelembapan = float(input("Masukkan nilai kelembapan (0-100 %): "))

# Hitung output
system.input['suhu']       = input_suhu
system.input['kelembapan'] = input_kelembapan
system.compute()

print(f"\nKecepatan Kipas  : {system.output['kecepatan']:.2f}")

# Tampilkan grafik hasil output
kecepatan.view(sim=system)
input("Tekan ENTER untuk keluar...")
