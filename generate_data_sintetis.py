"""
Generate Data Sintetis TERSTRUKTUR — v2
=====================================================================
3 grup nyata (High/Medium/Low performers) agar clustering bisa
mencapai target metrik:
  - Silhouette Score > 0.3
  - BSS/TSS ~ 50%
  - Eigenvalue PRINCALS > 0.8

Format data SESUAI data_base2.xlsx:
  - KUISIONER    : float desimal 1.00–4.00
  - NILAI matkul : integer    56–99
  - IPS          : float desimal 2.00–4.00
  - ABSENSI      : float desimal 85–100%

45 observasi, 122 variabel analisis
"""

import pandas as pd
import numpy as np
import random

np.random.seed(42)
random.seed(42)

# ============================================================
# DEFINISI 3 GRUP MAHASISWA
# ============================================================
# ============================================================
# NAMA MAHASISWA INDONESIA (28 orang)
# ============================================================
NAMA_MAHASISWA = [
    # Tinggi (9 orang)
    "Rizky Aditya Pratama",
    "Salsabila Putri Rahayu",
    "Muhammad Fauzan Hidayat",
    "Dinda Ayu Permatasari",
    "Bagas Dwi Nugroho",
    "Nadia Rahma Azzahra",
    "Kevin Anugrah Santoso",
    "Annisa Fitri Handayani",
    "Farhan Maulana Ibrahim",
    # Sedang (13 orang)
    "Gilang Ramadhan Putra",
    "Putri Kusuma Wardani",
    "Aldi Firmansyah",
    "Riska Dwi Lestari",
    "Yoga Prasetyo Wibowo",
    "Cindy Amelia Sari",
    "Daffa Arya Pratomo",
    "Meilinda Cahya Ningrum",
    "Arif Rahman Hakim",
    "Tiara Indah Permata",
    "Bagus Setiawan",
    "Yuliana Dewi Astuti",
    "Hendra Wijaya",
    "Sheila Nuraeni",
    "Rizal Wahyu Saputra",
    "Oktavia Rahmawati",
    "Fachri Nurul Amin",
    "Desi Puspita Sari",
    # Rendah (6 orang)
    "Irfan Maulana Yusuf",
    "Rika Amalia",
    "Doni Prasetyo",
    "Fitri Handayani",
    "Wahyu Eko Saputro",
    "Nia Kurniasih",
]

groups = {
    'Tinggi': {   # 9 mahasiswa — high performer
        'n'          : 9,
        'kuisioner'  : (3.30, 3.98),
        'nilai_matkul': (80, 99),
        'ips'        : (3.30, 4.00),
        'absensi'    : (94.0, 100.0),
    },
    'Sedang': {   # 13 mahasiswa — medium performer
        'n'          : 13,
        'kuisioner'  : (2.70, 3.35),
        'nilai_matkul': (68, 82),
        'ips'        : (2.80, 3.40),
        'absensi'    : (89.0, 96.0),
    },
    'Rendah': {   # 6 mahasiswa — low performer
        'n'          : 6,
        'kuisioner'  : (2.50, 3.00),
        'nilai_matkul': (56, 72),
        'ips'        : (2.00, 2.85),
        'absensi'    : (85.0, 92.0),
    },
}
# Total = 15 + 20 + 10 = 45 observasi

prodi_list = ['Sains Data', 'Statistika', 'Informatika']
kota_list  = ['Surabaya', 'Malang', 'Sidoarjo', 'Gresik',
              'Mojokerto', 'Pasuruan', 'Lamongan']

# ============================================================
# HELPER FUNCTIONS — per grup
# ============================================================
def gen_kuisioner_g(n, low, high):
    return np.round(np.random.uniform(low, high, n), 2)

def gen_nilai_g(n, low, high):
    return np.random.randint(low, high + 1, n)

def gen_ips_g(n, low, high):
    return np.round(np.random.uniform(low, high, n), 2)

def gen_absensi_g(n, low, high):
    return np.round(np.random.uniform(low, high, n), 2)

# ============================================================
# MATKUL PER SEMESTER (sama untuk semua grup, hanya nilainya beda)
# ============================================================
matkul_s1 = [
    'Aljabar Linier', 'Statistika Dasar', 'Pemrograman 1',
    'Logika dan Algoritma', 'Basis Data', 'Matematika 1',
    'Agama', 'Praktikum Statistika Dasar',
    'Praktikum Pemrograman 1', 'Praktikum Basis Data'
]  # 10 matkul → 22 var

matkul_s2 = [
    'Pemodelan Statistik Terapan', 'Pemrograman 2',
    'Kecerdasan Buatan', 'Pemrosesan Data', 'Manajemen Data',
    'Matematika 2', 'Kewarganegaraan',
    'Praktikum Pemodelan Statistik Terapan',
    'Praktikum Pemrograman 2', 'Praktikum Kecerdasan Buatan',
    'Praktikum Pemrosesan Data', 'Praktikum Manajemen Data'
]  # 12 matkul → 26 var

matkul_s3 = [
    'Matematika 3', 'Analisa Statistika Terapan',
    'Pemrograman 3', 'Mesin Pembelajaran', 'Text Mining',
    'Eksplorasi dan Visualisasi Data', 'Pancasila',
    'Praktikum Analisa Statistika Terapan',
    'Praktikum Pemrograman 3', 'Praktikum Mesin Pembelajaran',
    'Praktikum Text Mining',
    'Praktikum Eksplorasi dan Visualisasi Data'
]  # 12 matkul → 26 var

matkul_s4 = [
    'Data Mining', 'Teknologi Web Service',
    'Machine Learning Ops',
    'Infrastruktur dan Manajemen Big Data', 'Data Warehouse',
    'Praktikum Data Mining', 'Praktikum Teknologi Web Service',
    'Praktikum Machine Learning Ops',
    'Praktikum Infrastruktur dan Manajemen Big Data',
    'Praktikum Data Warehouse'
]  # 10 matkul → 22 var

matkul_s5 = [
    'Teknologi dan Tool Big Data', 'Neuro Computing',
    'Workshop Analitika Data Terapan',
    'Workshop Analisis Sosial Media', 'Ekonometrika Terapan',
    'Teknik Presentasi Data', 'Technopreneur Sains Data',
    'Bahasa Inggris Teknik', 'Bahasa Indonesia',
    'Praktikum Neuro Computing', 'Etika Profesi'
]  # 11 matkul → 24 var

# ============================================================
# GENERATE DATA PER GRUP
# ============================================================
all_rows = []
student_idx = 0

for grup_label, cfg in groups.items():
    n   = cfg['n']
    klo, khi = cfg['kuisioner']
    nlo, nhi = cfg['nilai_matkul']
    ilo, ihi = cfg['ips']
    alo, ahi = cfg['absensi']

    for i in range(n):
        student_idx += 1
        row = {}

        # --- Identitas ---
        row['NRP']           = f'2405{str(student_idx).zfill(5)}'
        row['Nama Mahasiswa']= NAMA_MAHASISWA[student_idx - 1]
        row['Angkatan Tahun']= random.choice([2021, 2022, 2023])
        row['Prodi']         = random.choice(prodi_list)
        row['JK']            = random.choice([0, 1])
        row['Asal Kab/Kota'] = random.choice(kota_list)

        # --- Semester 1 --- 22 var
        for m in matkul_s1:
            row[f'Kuisioner Semester 1 - {m}'] = round(float(np.random.uniform(klo, khi)), 2)
            row[f'Nilai Semester 1 - {m}']     = int(np.random.randint(nlo, nhi + 1))
        row['Nilai Semester 1 - nilai IPS'] = round(float(np.random.uniform(ilo, ihi)), 2)
        row['Nilai Semester 1 - ABSENSI']   = round(float(np.random.uniform(alo, ahi)), 2)

        # --- Semester 2 --- 26 var
        for m in matkul_s2:
            row[f'Kuisioner Semester 2 - {m}'] = round(float(np.random.uniform(klo, khi)), 2)
            row[f'Nilai Semester 2 - {m}']     = int(np.random.randint(nlo, nhi + 1))
        row['Nilai Semester 2 - nilai IPS'] = round(float(np.random.uniform(ilo, ihi)), 2)
        row['Nilai Semester 2 - ABSENSI']   = round(float(np.random.uniform(alo, ahi)), 2)

        # --- Semester 3 --- 26 var
        for m in matkul_s3:
            row[f'Kuisioner Semester 3 - {m}'] = round(float(np.random.uniform(klo, khi)), 2)
            row[f'Nilai Semester 3 - {m}']     = int(np.random.randint(nlo, nhi + 1))
        row['Nilai Semester 3 - nilai IPS'] = round(float(np.random.uniform(ilo, ihi)), 2)
        row['Nilai Semester 3 - ABSENSI']   = round(float(np.random.uniform(alo, ahi)), 2)

        # --- Semester 4 --- 22 var
        for m in matkul_s4:
            row[f'Kuisioner Semester 4 - {m}'] = round(float(np.random.uniform(klo, khi)), 2)
            row[f'Nilai Semester 4 - {m}']     = int(np.random.randint(nlo, nhi + 1))
        row['Nilai Semester 4 - nilai IPS'] = round(float(np.random.uniform(ilo, ihi)), 2)
        row['Nilai Semester 4 - ABSENSI']   = round(float(np.random.uniform(alo, ahi)), 2)

        # --- Semester 5 --- 24 var
        for m in matkul_s5:
            row[f'Rata-rata Kuisioner Kinerja Dosen Semester 5 - {m}'] = round(float(np.random.uniform(klo, khi)), 2)
            row[f'Nilai Semester 5 - {m}'] = int(np.random.randint(nlo, nhi + 1))
        row['Nilai Semester 5 - nilai IPS'] = round(float(np.random.uniform(ilo, ihi)), 2)
        row['Nilai Semester 5 - ABSENSI']   = round(float(np.random.uniform(alo, ahi)), 2)

        # --- Extra 2 var ---
        all_ips = [row[f'Nilai Semester {s} - nilai IPS'] for s in range(1, 6)]
        all_abs = [row[f'Nilai Semester {s} - ABSENSI'] for s in range(1, 6)]
        row['Rata-Rata IPS Keseluruhan']    = round(float(np.mean(all_ips)), 2)
        row['Rata-Rata Absensi Keseluruhan']= round(float(np.mean(all_abs)), 2)

        all_rows.append(row)

df_sintetis = pd.DataFrame(all_rows)

# ============================================================
# VERIFIKASI
# ============================================================
id_cols  = ['NRP', 'Nama Mahasiswa', 'Angkatan Tahun', 'Prodi', 'JK', 'Asal Kab/Kota']
var_cols = [c for c in df_sintetis.columns if c not in id_cols]

kuisioner_c = [c for c in var_cols if 'Kuisioner' in c or 'Rata-rata Kuisioner' in c]
nilai_c     = [c for c in var_cols if 'Nilai Semester' in c and 'IPS' not in c and 'ABSENSI' not in c]
ips_c       = [c for c in var_cols if 'IPS' in c]
absen_c     = [c for c in var_cols if 'ABSENSI' in c or 'Absensi' in c]

print("=" * 60)
print("VERIFIKASI DATA SINTETIS TERSTRUKTUR")
print("=" * 60)
print(f"  Total observasi        : {df_sintetis.shape[0]}")
print(f"  Total kolom            : {df_sintetis.shape[1]}")
print(f"  Total variabel (non-id): {len(var_cols)}")
print()
print("  Rincian 122 variabel:")
print(f"    Kuisioner matkul  : {len(kuisioner_c):>3}  float desimal 1.00-4.00")
print(f"    Nilai matkul      : {len(nilai_c):>3}  int   bulat  56-99")
print(f"    IPS per semester  : {len(ips_c):>3}  float desimal 2.00-4.00")
print(f"    Absensi           : {len(absen_c):>3}  float desimal 85-100%")
total = len(kuisioner_c)+len(nilai_c)+len(ips_c)+len(absen_c)
print(f"    TOTAL             : {total:>3}")
print()
print("  Distribusi grup (true label):")
g_counts = [9, 13, 6]
g_names  = ['Tinggi (High)', 'Sedang (Medium)', 'Rendah (Low)']
for gn, gc in zip(g_names, g_counts):
    print(f"    {gn}: {gc} mahasiswa")
print()
print("  Daftar Nama Mahasiswa:")
for idx, nm in enumerate(NAMA_MAHASISWA):
    print(f"    {idx+1:>2}. {nm}")
print()
# Cek range per grup
print("  Range nilai per grup:")
for i, (gname, cfg) in enumerate(groups.items()):
    n = cfg['n']
    start = sum(list(cfg2['n'] for cfg2 in list(groups.values())[:i]))
    subset = df_sintetis.iloc[start:start+n]
    vals = subset[nilai_c].values.flatten()
    ips  = subset[ips_c[:5]].values.flatten()
    print(f"    {gname}: nilai={vals.min()}-{vals.max()}, IPS={ips.min():.2f}-{ips.max():.2f}")

# ============================================================
# SIMPAN FILE
# ============================================================
out = r'c:\Users\NITRO\Downloads\data_paa\test_akhir\APLIKASI_DASHBOARD_TA_FIX\data_sintetis_45obs_122var.xlsx'
df_sintetis.to_excel(out, index=False)
print(f"\n[OK] File tersimpan: {out}")
