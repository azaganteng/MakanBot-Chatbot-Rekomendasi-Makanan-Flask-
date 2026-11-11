"""Uji route Flask MakanBot."""
import pytest

from app import create_app


@pytest.fixture
def client(tmp_path):
    return create_app({"TESTING": True, "DATABASE": str(tmp_path / "test.db")}).test_client()


def test_halaman_utama_menampilkan_makanbot(client):
    response = client.get("/")
    assert response.status_code == 200
    assert "MakanBot" in response.get_data(as_text=True)


def test_halaman_chat(client):
    response = client.get("/chat/makanbot")
    assert response.status_code == 200
    assert "MakanBot" in response.get_data(as_text=True)


def test_api_chat_berhasil(client):
    response = client.post("/api/chat", json={"message": "aku ingin makanan pedas", "theme": "makanbot"})
    assert response.status_code == 200
    assert response.get_json()["intent"] == "makanan_pedas"


@pytest.mark.parametrize("payload", [{"message": "", "theme": "makanbot"}, {"message": "halo", "theme": "salah"}, {}])
def test_api_chat_input_tidak_valid(client, payload):
    assert client.post("/api/chat", json=payload).status_code == 400


def test_riwayat_dapat_disimpan_dan_dihapus(client):
    client.post("/api/chat", json={"message": "halo", "theme": "makanbot"})
    assert len(client.get("/api/history/makanbot").get_json()) == 2
    client.delete("/api/history/makanbot")
    assert client.get("/api/history/makanbot").get_json() == []
