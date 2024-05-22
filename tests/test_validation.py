import pytest
from fastapi.testclient import TestClient
# from unittest.mock import patch, MagicMock
from faker import Faker
from main import app
from controllers.batch_controller import add_numbers, process_batch
from models.batch import BatchRequest

client = TestClient(app)
fake = Faker()


@pytest.fixture(autouse=True)
def setup_teardown():
    yield
    # Any teardown actions if needed
    pass


def test_invalid_batch_payload():
    # Test for invalid payload containing a non-integer element
    response = client.post(
        "/process_batch", json={"batchid": "id0101", "payload": [[1, 2], [3, "a"]]})
    assert response.status_code == 422


def test_valid_batch_payload():
    # Test for valid payload containing only integer elements
    response = client.post(
        "/process_batch", json={"batchid": "id0101", "payload": [[5, 6], [7, 8]]})
    assert response.status_code == 200


def test_process_batch_function():
    # Mock input data
    batch_request = BatchRequest(batchid="id0101", payload=[[5, 6], [7, 8]])

    # Call the process_batch function directly
    response = process_batch(batch_request)

    # Validate the response
    assert response.batchid == "id0101"
    assert response.status == "complete"
    assert response.response == [[11], [15]]
    assert response.started_at is not None
    assert response.completed_at is not None


def test_fake_batch_payload():
    # Use Faker to generate fake batch payloads
    batchid = fake.uuid4()
    payload = [[fake.random_int(), fake.random_int()] for _ in range(2)]

    response = client.post(
        "/process_batch", json={"batchid": batchid, "payload": payload})
    assert response.status_code == 200
