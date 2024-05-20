# batch_router.py
from typing import List
from fastapi import APIRouter, HTTPException
from models.batch import BatchRequest, BatchResponse
from controllers.batch_controller import add_numbers, process_batch

batch_router = APIRouter()


@batch_router.post("/add_numbers")
# both async and sync we can call depends on our requirement
# if it is io heavy then can make async is useful
async def add_numbers_endpoint(numbers: List[int]) -> List[int]:
    """Endpoint to perform addition on a list of integers."""
    return add_numbers(numbers)


@batch_router.post("/process_batch", response_model=BatchResponse)
# both async and sync we can call depends on our requirement
# if it is io heavy then can make async is useful
async def process_batch_endpoint(batch: BatchRequest) -> BatchResponse:
    """Endpoint to process batch using multiprocessing pool."""
    try:
        result = process_batch(batch)
        return result  # Directly return the BatchResponse object
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except RuntimeError as e:
        raise HTTPException(status_code=500, detail=str(e))
