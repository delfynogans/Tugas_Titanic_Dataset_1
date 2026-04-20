# Tugas Data Mining - Titanic Dataset

| Atribut | Keterangan |
| :--- | :--- |
| **Nama** | Delfyno Dwi Prastyo, Bayu Yusuf, Tafsil, Joel, Filemon |
| **NIM** | 312310480 |
| **Mata Kuliah** | Data Mining |

## Kode Analisis (Python)
```python
import pandas as pd

# 1. Mengambil data langsung dari sumber resmi
url = "[https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv](https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv)"
df = pd.read_csv(url)

# 2. Melihat 5 data teratas
print("--- 5 Data Teratas ---")
print(df.head())

# 3. Mengecek informasi dataset dan data yang kosong
print("\n--- Informasi Dataset ---")
print(df.info())

# 4. Pembersihan Data Dasar
# Mengisi umur yang kosong dengan nilai tengah (median)
df['Age'] = df['Age'].fillna(df['Age'].median())

# Menghapus kolom Cabin karena terlalu banyak data kosong
df.drop(columns=['Cabin'], inplace=True)

# 5. Analisis Sederhana: Persentase Keselamatan berdasarkan Jenis Kelamin
print("\n--- Persentase Keselamatan berdasarkan Gender ---")
survival_rate = df.groupby('Sex')['Survived'].mean() * 100
print(survival_rate.round(2))
