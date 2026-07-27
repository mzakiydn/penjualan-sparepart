import pandas as pd
import matplotlib.pyplot as plt

def muat_data(path_file):
    return pd.read_csv(path_file)

def bersihkan_data(df):
    df.columns = df.columns.str.strip()
    return df.dropna()

def buat_grafik(df, nama_file_output):
    data_grafik = df.groupby('Nama Produk')['Terjual'].sum().sort_values(ascending=False)
    
    plt.figure(figsize=(10, 6))
    data_grafik.plot(kind='bar', color='teal', edgecolor='black')
    
    plt.title('Total Penjualan per Nama Produk Sparepart', fontsize=14, fontweight='bold')
    plt.xlabel('Nama Produk', fontsize=12)
    plt.ylabel('Jumlah Terjual (Unit)', fontsize=12)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    
    plt.savefig(nama_file_output)
    plt.close()
