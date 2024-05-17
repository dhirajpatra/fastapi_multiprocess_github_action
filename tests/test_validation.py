# test_validation.py
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_invalid_batch_payload():
    # Test for invalid payload containing a non-integer element
    response = client.post("/process_batch", json={"batchid": "id0101", "payload": [[1, 2], [3, "a"]]})
    assert response.status_code == 422

def test_valid_batch_payload():
    # Test for valid payload containing only integer elements
    response = client.post("/process_batch", json={"batchid": "id0101", "payload": [[5, 6], [7, 8]]})
    assert response.status_code == 200
