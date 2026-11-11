# MakanBot

Chatbot rekomendasi makanan berbasis aturan menggunakan Flask. MakanBot dapat membantu memilih makanan berdasarkan selera, waktu makan, bahan yang tersedia, serta memberikan resep sederhana.

## Menjalankan

```powershell
cd MakanBot
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Buka `http://127.0.0.1:5000`.

## Fitur

- Rekomendasi makanan pedas, manis, murah, sehat, berkuah, dan tanpa nasi
- Rekomendasi menu sarapan, makan siang, dan makan malam
- Saran berdasarkan bahan makanan
- Resep makanan sederhana
- Riwayat chat, statistik admin, REST API, dan mode belajar

Data intent berada di `themes/makanbot.json`.
