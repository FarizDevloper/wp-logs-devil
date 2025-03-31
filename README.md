![devillll-removebg-preview](https://github.com/user-attachments/assets/20c9e119-c0b8-4a10-b82e-5f923c812b5f)



# WP Logs Devil - WordPress Login Checker 🔥

**WP Logs Devil** adalah alat powerful untuk menguji kredensial login di situs WordPress. Dapatkan akses lebih cepat dengan pemindaian login otomatis menggunakan teknik **brute force**! Alat ini dirancang untuk membantu Anda memverifikasi login di situs WordPress dengan efisien, mengidentifikasi kombinasi kredensial yang berhasil, dan memberikan statistik pemindaian yang berguna.

## Fitur Utama 🚀
- **Pemeriksaan Massal**: Uji banyak URL dan kombinasi username/password sekaligus.
- **Threading & Kecepatan**: Proses lebih cepat dengan teknik multithreading.
- **Validasi Domain**: Memastikan hanya domain yang sah yang diproses.
- **Statistik Scan Lengkap**: Laporan sukses, gagal, error, dan kredensial tidak valid.
- **Output File**: Hasil login yang berhasil disimpan dalam file terpisah untuk analisis lebih lanjut.

## Cara Penggunaan 📜
1. **Siapkan Dua File**:
   - **URL Logs**: Berisi daftar URL situs WordPress yang ingin dipindai.
   - **Credentials Logs**: Berisi kombinasi username dan password yang ingin diuji.
   
2. **Jalankan Skrip**: Eksekusi skrip Python dan masukkan nama file ketika diminta.

3. **Hasil Pemindaian**: Hasil login yang berhasil disimpan dalam `wp-success.txt`, sementara URL yang gagal atau tidak valid tercatat di `invalid-logs.txt`.

4. **Lihat Statistik**: Setelah pemindaian selesai, statistik hasilnya akan ditampilkan secara otomatis.

## Instalasi & Prasyarat ⚙️
- **Python 3.x** (disarankan versi terbaru)
- Modul `requests`: Install dengan perintah `pip install requests`

## Contoh Format Input 📂
- **URL Logs**: 
https://example.com https://another-site.com



- **Credentials Logs**:
admin:password123 user:12345678


## Disclaimer ⚠️
- Alat ini **hanya untuk tujuan edukasi** dan **penelitian keamanan**.
- Pastikan Anda memiliki **izin eksplisit** sebelum menggunakan alat ini pada situs apa pun.
- Penggunaan tanpa izin atau untuk tujuan ilegal dapat berakibat **hukuman pidana**.


