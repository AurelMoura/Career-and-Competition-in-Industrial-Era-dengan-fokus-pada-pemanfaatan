# Career-and-Competition-in-Industrial-Era-dengan-fokus-pada-pemanfaatan
# Public Facilities Mapping in Bengkulu City Using GIS

## 1. Deskripsi Proyek

Proyek ini merupakan implementasi sederhana dari materi Praktisi Mengajar berjudul *Career and Competition in Industrial Era* dengan fokus pada pemanfaatan Geographic Information System (GIS).

Proyek bertujuan membuat peta interaktif fasilitas umum menggunakan Python berdasarkan data koordinat simulasi.

## 2. Tujuan

- Memahami konsep dasar GIS.
- Mengolah data koordinat menggunakan Pandas.
- Memeriksa kualitas dan validitas data.
- Memetakan lokasi fasilitas berdasarkan koordinat.
- Menghitung jumlah fasilitas berdasarkan kategori.
- Menyajikan informasi melalui peta interaktif.

## 3. Tools yang Digunakan

- Python 3.13
- Pandas
- Folium
- Visual Studio Code

## 4. Dataset

Dataset terdiri dari nama fasilitas, kategori, latitude, dan longitude.

Seluruh nama fasilitas dan koordinat merupakan data simulasi untuk pembelajaran. Data tersebut tidak menunjukkan lokasi fasilitas nyata yang telah diverifikasi di Kota Bengkulu.

## 5. Metode

Program membaca dataset CSV, memeriksa kualitas data, menghitung jumlah fasilitas berdasarkan kategori, dan menampilkan koordinat dalam peta interaktif.

## 6. Hasil dan Insight

Proyek menghasilkan peta interaktif dengan delapan titik simulasi yang terdiri dari kategori sekolah, rumah sakit, tempat ibadah, dan ruang publik.

Peta membantu pengguna melihat persebaran titik berdasarkan koordinat dan membandingkan jumlah fasilitas per kategori. Karena menggunakan data simulasi, hasil ini tidak dapat digunakan untuk menyimpulkan persebaran fasilitas umum yang sebenarnya.

## 7. Cara Menjalankan

Instal library:

`python -m pip install pandas folium`

Jalankan program:

`python pemetaan_gis.py`

Buka file `peta_fasilitas.html` melalui browser untuk melihat peta interaktif.

## 8. Output

- `peta_fasilitas.html`: peta interaktif.
- `ringkasan_fasilitas.csv`: jumlah fasilitas per kategori.

## 9. Kesimpulan

Proyek ini menunjukkan penerapan dasar GIS melalui pemrosesan data koordinat, pemetaan lokasi, dan penyajian informasi spasial. Kemampuan tersebut dapat dikembangkan lebih lanjut dengan menggunakan data geografis nyata yang tervalidasi.

## 10. Catatan

Proyek ini merupakan demonstrasi pembelajaran dan bukan sistem informasi fasilitas umum resmi.
