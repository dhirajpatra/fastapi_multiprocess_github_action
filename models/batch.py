# batch.py
from typing import List
from pydantic import BaseModel


# Define the request schema for the /batch endpoint
class BatchRequest(BaseModel):
    """Batch request processing

    Args:
        BaseModel (_type_): _description_
    """
    batchid: str
    payload: List[List[int]]


# Define the response schema for the /batch endpoint
class BatchResponse(BaseModel):
    """Batch process response

    Args:
        BaseModel (_type_): _description_
    """
    batchid: str
    response: List[List[int]]
    status: str
    started_at: str
    completed_at: str
