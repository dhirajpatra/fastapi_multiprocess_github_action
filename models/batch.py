# batch.py
from typing import List
from pydantic import BaseModel, validator


# Define the request schema for add_number
class NumbersRequest(BaseModel):
    numbers: List[int]

    @validator('numbers')
    def must_contain_only_integers(cls, value):
        if not all(isinstance(i, int) for i in value):
            raise ValueError('All elements must be integers')
        return value


# Define the response for add_number
class NumbersResponse(BaseModel):
    result: List[int]


# Define the request schema for the /batch endpoint
class BatchRequest(BaseModel):
    """Batch request processing

    Args:
        BaseModel (_type_): _description_
    """
    batchid: str
    payload: List[List[int]]

    @validator('batchid')
    def batchid_must_not_be_empty(cls, value):
        if not value.strip():
            raise ValueError('batchid must not be empty')
        return value

    @validator('payload')
    def payload_must_contain_lists_of_integers(cls, value):
        if not isinstance(value, list) or not all(isinstance(sublist, list) for sublist in value):
            raise ValueError('payload must be a list of lists')
        for sublist in value:
            if not all(isinstance(i, int) for i in sublist):
                raise ValueError('payload must contain only integers')
        return value


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
