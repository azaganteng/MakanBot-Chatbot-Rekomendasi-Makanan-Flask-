"""Uji unit untuk mesin MakanBot."""
from pathlib import Path

import pytest

from chatbot.engine import ChatbotEngine, load_themes, preprocess, similarity

THEMES = load_themes(Path(__file__).resolve().parent.parent / "themes")


def test_preprocess_normalisasi_dan_stopword():
    assert preprocess("Gimana rekomendasi makanan, kak?") == ["bagaimana", "rekomendasi", "makanan"]


def test_similarity_kalimat_sama_bernilai_satu():
    assert similarity(["makanan", "pedas"], ["makanan", "pedas"]) == 1.0


def test_makanbot_termuat_dan_valid():
    assert set(THEMES) == {"makanbot"}
    assert len(THEMES["makanbot"]["intents"]) >= 10


@pytest.mark.parametrize("pesan, intent", [
    ("halo makanbot", "salam"),
    ("aku ingin makanan pedas", "makanan_pedas"),
    ("enaknya sarapan apa", "menu_sarapan"),
    ("resep nasi goreng", "resep_makanan"),
    ("makasih", "terima_kasih"),
])
def test_klasifikasi_intent(pesan, intent):
    tag, _ = ChatbotEngine(THEMES["makanbot"]).classify(pesan)
    assert tag == intent


def test_pertanyaan_di_luar_tema_memberi_fallback():
    hasil = ChatbotEngine(THEMES["makanbot"]).reply("berapa harga tiket pesawat")
    assert hasil["intent"] is None
    assert hasil["reply"] in THEMES["makanbot"]["fallback"]


def test_placeholder_nama_bot_diganti():
    hasil = ChatbotEngine(THEMES["makanbot"]).reply("siapa kamu")
    assert "{nama_bot}" not in hasil["reply"]
    assert "MakanBot" in hasil["reply"]
