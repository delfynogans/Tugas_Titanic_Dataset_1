# Tugas_Titanic_Dataset_1

| Atribut         | Keterangan            |
| --------------- | --------------------- |
| **Nama**        | Delfyno Dwi Prastyo   |
| **NIM**         | 312310480        |
| **Kelas**       | TI.23.A.5             |
| **Mata Kuliah** | Pemrograman Website 2 |


# 1. Mengambil data langsung dari link GitHub yang kamu berikan
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

# 2. Melihat 5 data teratas untuk memastikan data terbaca
print("--- 5 Data Teratas ---")
print(df.head())

# 3. Mengecek informasi kolom dan data yang kosong (Missing Values)
print("\n--- Informasi Dataset ---")
print(df.info())

# 4. Pembersihan Data Dasar (Sangat Penting dalam Data Science)
# Mengisi umur yang kosong dengan nilai rata-rata (median)
df['Age'] = df['Age'].fillna(df['Age'].median())

# Menghapus kolom 'Cabin' karena terlalu banyak data kosong
df.drop(columns=['Cabin'], inplace=True)

# 5. Analisis Sederhana: Persentase Keberangkatan berdasarkan Jenis Kelamin
print("\n--- Persentase Keselamatan berdasarkan Gender ---")
print(df.groupby('Sex')['Survived'].mean() * 100)
