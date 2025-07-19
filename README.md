# NoPMsBot
Bot Telegram sederhana untuk meneruskan semua Pesan Pribadi yang masuk ke Saluran Auth.

## Variabel Lingkungan yang Diperlukan
* `TG_BOT_TOKEN`: Token Bot Telegram Anda, dari @BotFather
* `APP_ID`: ID Aplikasi Telegram Anda, dari my.telegram.org
* `API_HASH`: Hash API Telegram Anda, dari my.telegram.org
* `AUTH_CHANNEL`: ID Saluran Telegram, tempat bot harus meneruskan pesan.
* `DATABASE_URL`: URL basis data Anda.

## Cara Menjalankan di VPS
1.  **Kloning Repositori**:
    ```
    git clone https://github.com/SpEcHIDe/NoPMsBot.git
    cd NoPMsBot
    ```
2.  **Buat dan Aktifkan Lingkungan Virtual**:
    ```
    python3 -m venv venv
    source venv/bin/activate
    ```
3.  **Instal Dependensi**:
    ```
    pip install -r requirements.txt
    ```
4.  **Konfigurasi Variabel Lingkungan**:
    *   Salin `sample_config.env` ke `config.env`:
        ```
        cp sample_config.env config.env
        ```
    *   Edit `config.env` dengan editor teks favorit Anda (misalnya, `nano`):
        ```
        nano config.env
        ```
    *   Isi semua variabel yang diperlukan dengan nilai Anda sendiri.
5.  **Jalankan Bot**:
    ```
    python3 -m bot
    ```

## Cara Menggunakan
* Balas pesan apa pun yang diteruskan dengan `/ban` untuk memblokir pengguna agar tidak menggunakan bot.
* Balas pesan apa pun yang diteruskan dengan `/unban` untuk membuka blokir pengguna.
* Gunakan `/start` untuk memeriksa apakah bot sedang online.
* Kirim stiker apa pun sebagai balasan ke pesan yang diteruskan, untuk mengirim stiker itu kepada pengguna.
* Kirim media / file apa pun sebagai balasan ke pesan yang diteruskan, untuk mengirim media / file itu kepada pengguna.
* Kirim teks apa pun sebagai balasan ke pesan yang diteruskan, untuk mengirim teks itu kepada pengguna.

### Catatan
* Beberapa perintah mungkin tidak berfungsi dengan benar, jika Anda mengubah awalan perintah default.
* Jika Anda ingin menggunakan bot ini untuk tujuan komersial, silakan dapatkan lisensi yang sesuai.
* Bot ini tidak dimaksudkan untuk digunakan dalam grup.
* Bot ini tidak dimaksudkan untuk digunakan sebagai bot pengguna.

## Lisensi
* Program ini adalah perangkat lunak bebas: Anda dapat mendistribusikan kembali dan/atau memodifikasinya di bawah persyaratan Lisensi Publik Umum GNU Affero seperti yang diterbitkan oleh Free Software Foundation, baik versi 3 dari Lisensi, atau (sesuai pilihan Anda) versi yang lebih baru.
* Program ini didistribusikan dengan harapan akan bermanfaat, tetapi TANPA JAMINAN APA PUN; bahkan tanpa jaminan tersirat tentang KELAYAKAN DIPERDAGANGKAN atau KESESUAIAN UNTUK TUJUAN TERTENTU. Lihat Lisensi Publik Umum GNU Affero untuk detail lebih lanjut.
* Anda seharusnya sudah menerima salinan Lisensi Publik Umum GNU Affero bersama dengan program ini. Jika tidak, lihat <https://www.gnu.org/licenses/>.
