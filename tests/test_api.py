from fastapi.testclient import TestClient
from src.api import app

client = TestClient(app)

def test_api_redact():
    response = client.post("/redact", json={"text": "my email is test@test.com", "is_json": False})
    assert response.status_code == 200
    assert "EMAIL_REDACTED" in response.json()["redacted_text"]