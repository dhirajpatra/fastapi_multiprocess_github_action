# test_addition_logic.py
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

# Test for adding numbers
def test_add_numbers():
    payload = [1, 2, 3, 4]
    response = client.post("/add_numbers", json=payload)
    assert response.status_code == 200
    assert response.json() == [10]

