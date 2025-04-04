


![510](https://github.com/user-attachments/assets/d7ae14d3-7fa5-4125-9e0f-6f5d1d384ee1)

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


## Credits

Jika Anda ingin mendukung pengembangan lebih lanjut, beri kredit kepada pengembang berikut:


<a class="pin-payment-button" href="https://saweria.co/adminpusat2024"><img src="https://pinpayments.com/pay-button.png" alt="Pay Now" width="86" height="38"></a>


