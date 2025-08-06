from fastapi.testclient import TestClient
from main import app

print(TestClient.__module__)


client = TestClient(app)

def test_get_all_blogs():
    response = client.get("/blog/all")
    assert response.status_code == 200
