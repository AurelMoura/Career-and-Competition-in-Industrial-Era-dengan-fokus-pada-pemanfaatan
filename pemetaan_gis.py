
import pandas as pd
import folium

# 1. Membaca dataset
df = pd.read_csv("fasilitas_umum.csv")

print("=== DATA FASILITAS UMUM ===")
print(df)

# 2. Memeriksa kualitas data
print("\n=== PEMERIKSAAN DATA ===")
print("Data kosong:")
print(df.isnull().sum())

print("\nJumlah data duplikat:", df.duplicated().sum())

# 3. Memastikan koordinat valid
kolom_wajib = [
    "nama_fasilitas",
    "kategori",
    "latitude",
    "longitude"
]

if df[kolom_wajib].isnull().any().any():
    raise ValueError("Ada data kosong. Periksa file CSV.")

df["latitude"] = pd.to_numeric(
    df["latitude"], errors="coerce"
)
df["longitude"] = pd.to_numeric(
    df["longitude"], errors="coerce"
)

if df[["latitude", "longitude"]].isnull().any().any():
    raise ValueError("Koordinat harus berupa angka.")

if not df["latitude"].between(-90, 90).all():
    raise ValueError("Latitude berada di luar rentang valid.")

if not df["longitude"].between(-180, 180).all():
    raise ValueError("Longitude berada di luar rentang valid.")

# 4. Menghitung jumlah fasilitas per kategori
ringkasan = (
    df.groupby("kategori")
    .size()
    .reset_index(name="jumlah")
)

print("\n=== RINGKASAN FASILITAS ===")
print(ringkasan)

ringkasan.to_csv(
    "ringkasan_fasilitas.csv", index=False
)

# 5. Membuat peta interaktif
pusat_peta = [
    df["latitude"].mean(),
    df["longitude"].mean()
]

peta = folium.Map(
    location=pusat_peta,
    zoom_start=14
)

warna_kategori = {
    "Sekolah": "blue",
    "Rumah Sakit": "red",
    "Tempat Ibadah": "green",
    "Ruang Publik": "orange"
}

for _, baris in df.iterrows():
    warna = warna_kategori.get(
        baris["kategori"], "gray"
    )

    folium.Marker(
        location=[
            baris["latitude"],
            baris["longitude"]
        ],
        tooltip=baris["nama_fasilitas"],
        popup=(
            f"Nama: {baris['nama_fasilitas']}<br>"
            f"Kategori: {baris['kategori']}<br>"
            "<b>Data simulasi</b>"
        ),
        icon=folium.Icon(
            color=warna,
            icon="info-sign"
        )
    ).add_to(peta)

# 6. Menambahkan keterangan pada peta
folium.map.Marker(
    location=pusat_peta,
    icon=folium.DivIcon(
        html="""
        <div style="
            font-size: 14px;
            font-weight: bold;
            background: white;
            padding: 6px;
            border: 1px solid gray;
        ">
        DATA SIMULASI - BUKAN LOKASI NYATA
        </div>
        """
    )
).add_to(peta)

# 7. Menyimpan hasil
peta.save("peta_fasilitas.html")

print("\nPeta berhasil dibuat: peta_fasilitas.html")
print("Ringkasan berhasil dibuat: ringkasan_fasilitas.csv")
print("Semua koordinat merupakan data simulasi.")
