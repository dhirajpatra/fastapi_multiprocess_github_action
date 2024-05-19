# test_error_handling.py
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

# Test for invalid payload containing a non-integer element
def test_empty_payload():
    payload = {"batchid": "id0101", "payload": []}
    response = client.post("/process_batch", json=payload)
    assert response.status_code == 400  # Check for status code 400 (Bad Request)
    assert response.json()['detail'] == "Payload is empty"  # Check for the error message

# Test for valid payload containing only integer elements
def test_invalid_batch_payload():
    payload = {"batchid": "id123"}  # Missing 'payload' key
    response = client.post("/process_batch", json=payload)
    assert response.status_code == 422  # Check for status code 422 (Unprocessable Entity)
    assert response.json()['detail'][0]['msg'].lower() == "field required"  # Check for the error message
