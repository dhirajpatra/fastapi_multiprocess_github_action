# batch.py
from pydantic import BaseModel
from typing import List, Union


# Define the request schema for the /batch endpoint
class BatchRequest(BaseModel):
    batchid: str
    payload: List[List[int]]


# Define the response schema for the /batch endpoint
class BatchResponse(BaseModel):
    batchid: str
    response: List[List[int]]
    status: str
    started_at: str
    completed_at: str
