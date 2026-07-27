from utils import muat_data, bersihkan_data, buat_grafik
import pandas as pd

def main():
    path_dataset = "dataset/data_mentah.csv"
    
    df = muat_data(path_dataset)
    df = bersihkan_data(df)
    
    df['Stok Awal'] = pd.to_numeric(df['Stok Awal'])
    df['Terjual'] = pd.to_numeric(df['Terjual'])
    
    total_terjual = df['Terjual'].sum()
    rata_stok_awal = df['Stok Awal'].mean()
    
    produk_terlaris = df.loc[df['Terjual'].idxmax()]
    produk_terendah = df.loc[df['Terjual'].idxmin()]
    
    analisis_kendaraan = df.groupby('Tipe Kendaraan')['Terjual'].sum().reset_index()
    analisis_kendaraan = analisis_kendaraan.sort_values(by='Terjual', ascending=False)
    
    with open("hasil_analisis.txt", "w") as f:
        f.write("==================================================\n")
        f.write(" LAPORAN ANALISIS PENJUALAN SPAREPART \n")
        f.write("==================================================\n\n")
        f.write(f"Total Seluruh Produk Terjual : {total_terjual} unit\n")
        f.write(f"Rata-rata Stok Awal Toko     : {rata_stok_awal:.2f} unit\n\n")
        f.write(f"Produk Terlaris:\n")
        f.write(f"- Nama Produk : {produk_terlaris['Nama Produk']}\n")
        f.write(f"- Kendaraan   : {produk_terlaris['Tipe Kendaraan']}\n")
        f.write(f"- Jumlah Laku : {produk_terlaris['Terjual']} unit\n\n")
        f.write(f"Produk Penjualan Terendah:\n")
        f.write(f"- Nama Produk : {produk_terendah['Nama Produk']}\n")
        f.write(f"- Kendaraan   : {produk_terendah['Tipe Kendaraan']}\n")
        f.write(f"- Jumlah Laku : {produk_terendah['Terjual']} unit\n\n")
        f.write("Total Penjualan Berdasarkan Tipe Kendaraan:\n")
        f.write(analisis_kendaraan.to_string(index=False))
        
    buat_grafik(df, "grafik_output.png")
    
    print("Analisis Berhasil! File 'hasil_analisis.txt' dan 'grafik_output.png' telah diperbarui.")

if __name__ == "__main__":
    main()
