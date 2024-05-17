# test_logging.py
import logging
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_logging():
    # Clear the log file before running the test
    open("app.log", "w").close()

    # Send a request to trigger logging with a payload containing numbers
    payload = {"numbers": [[1, 2], [3, 4], [5, 6]]}
    response = client.post("/process_batch", json=payload)

    # Check if the log file has been created and contains the expected log message
    with open("app.log", "r") as f:
        logs = f.readlines()
        assert len(logs) == 1

