# Cara Menjalankan Chatbot

Dokumen ini menjelaskan cara menjalankan aplikasi chatbot yang tersedia di folder ini.

## 1. Persiapan

Pastikan Python 3.10 atau lebih baru sudah terpasang:

```powershell
python --version
```

Buat dan aktifkan virtual environment dari folder utama proyek:

```powershell
python -m venv venv
venv\Scripts\Activate.ps1
```

Jika PowerShell menolak menjalankan skrip, jalankan satu kali:

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

Pasang dependensi:

```powershell
pip install -r requirements.txt
```

## 2. Menjalankan MakanBot

Masuk ke folder aplikasi:

```powershell
cd MakanBot
```

Jalankan server:

```powershell
python app.py
```

Buka alamat berikut di browser:

```text
http://127.0.0.1:5000
```

Halaman chat MakanBot tersedia di:

```text
http://127.0.0.1:5000/chat/makanbot
```

Hentikan server dengan menekan `Ctrl + C`.

## 3. Menjalankan MakanBot melalui terminal

Dari folder `MakanBot`:

```powershell
python cli.py
```

Ketik pertanyaan secara langsung di terminal. Ketik `keluar` untuk berhenti.

Untuk melihat intent, skor, dan pola yang dipilih:

```powershell
python cli.py --debug
```

`cli.py` menggunakan mesin chatbot yang sama dengan aplikasi web, tetapi tidak menampilkan HTML dan tidak menyimpan riwayat ke database.

## 4. Menguji akurasi MakanBot

Data pengujian berada di:

```text
MakanBot/evaluasi/makanbot.csv
```

Jalankan dari folder `MakanBot`:

```powershell
python evaluate.py --tema makanbot
```

Program akan menampilkan persentase akurasi, hasil per intent, dan pertanyaan yang salah dikenali.

## 5. Menjalankan pengujian otomatis

Dari folder `MakanBot`:

```powershell
pytest -v
```

Pengujian mencakup mesin intent, halaman Flask, API chat, dan riwayat percakapan.

## 6. File penting MakanBot

```text
MakanBot/
├── app.py                    route halaman dan REST API
├── cli.py                    chatbot melalui terminal
├── evaluate.py               pengukur akurasi
├── chatbot/
│   ├── engine.py             preprocessing dan pencocokan intent
│   └── database.py           penyimpanan riwayat SQLite
├── themes/makanbot.json      data intent dan respons MakanBot
├── templates/                file HTML Jinja2
├── static/                   CSS dan JavaScript
├── evaluasi/makanbot.csv     data uji akurasi
├── tests/                    pengujian otomatis
└── chat_history.db           database yang dibuat otomatis
```

## 7. Melihat riwayat chat

Riwayat tersimpan di:

```text
MakanBot/chat_history.db
```

Tabel utama yang digunakan adalah:

```text
messages
```

Database dapat dibuka menggunakan DB Browser for SQLite atau ekstensi SQLite Viewer di VS Code.

Riwayat juga dapat dilihat melalui API:

```text
http://127.0.0.1:5000/api/history/makanbot
```

## 8. Halaman admin dan API

Halaman statistik:

```text
http://127.0.0.1:5000/admin/makanbot
```

Endpoint utama:

| Metode | URL | Fungsi |
| --- | --- | --- |
| GET | `/` | Halaman utama |
| GET | `/chat/makanbot` | Halaman chat |
| GET | `/admin/makanbot` | Statistik dan pertanyaan tidak dikenali |
| GET | `/api/themes` | Daftar tema |
| POST | `/api/chat` | Mengirim pesan ke chatbot |
| POST | `/api/explain` | Melihat kandidat intent |
| GET | `/api/history/makanbot` | Melihat riwayat sesi |
| DELETE | `/api/history/makanbot` | Menghapus riwayat sesi |
| GET | `/api/stats/makanbot` | Melihat statistik intent |

Contoh request API:

```powershell
Invoke-RestMethod `
  -Uri http://127.0.0.1:5000/api/chat `
  -Method Post `
  -ContentType "application/json" `
  -Body '{"message":"rekomendasi makanan pedas","theme":"makanbot"}'
```

## 9. Mengubah pengetahuan MakanBot

Edit file berikut:

```text
MakanBot/themes/makanbot.json
```

Setiap intent memiliki:

- `tag` — nama intent
- `patterns` — variasi pertanyaan pengguna
- `responses` — variasi jawaban chatbot

Setelah mengubah JSON, periksa formatnya:

```powershell
python -m json.tool themes/makanbot.json
```

Kemudian jalankan kembali aplikasi dan uji akurasinya.

## 10. Masalah umum

| Masalah | Solusi |
| --- | --- |
| `ModuleNotFoundError: No module named flask` | Aktifkan virtual environment dan jalankan `pip install -r requirements.txt` |
| `File tema makanbot.json tidak valid` | Periksa dengan `python -m json.tool themes/makanbot.json` |
| `Address already in use` | Hentikan server lama dengan `Ctrl + C` |
| Database belum terlihat | Jalankan `python app.py`, lalu kirim minimal satu pesan |
| Bot sering memakai fallback | Tambahkan variasi pola pada `themes/makanbot.json` |
| Tampilan belum berubah | Tekan `Ctrl + Shift + R` di browser |
