# batch_controller.py
import os
import logging
import multiprocessing
from datetime import datetime
from typing import List
from fastapi import HTTPException
from models.batch import BatchRequest, BatchResponse


# Get the absolute path to the root directory of the application
root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Specify the absolute path to the log file in the root directory
log_file = os.path.join(root_dir, 'app.log')

# Configure logging to write logs to the specified log file
# loglevel decided in log.ini file
logging.basicConfig(filename=log_file)
logger = logging.getLogger(__name__)


def add_numbers(numbers: List[int]) -> List[int]:
    """Function to perform addition on a list of integers."""
    return [sum(numbers)]


def process_batch(batch: BatchRequest) -> BatchResponse:
    """Function to process batch using multiprocessing pool."""
    # Validate input payload blank or not
    if not batch.payload:
        # Update the status code to 400
        raise HTTPException(status_code=400, detail="Payload is empty")

    # Custom validation to check if each element in the payload is an integer
    for sublist in batch.payload:
        for item in sublist:
            if not isinstance(item, int):
                raise HTTPException(
                    status_code=422, detail=f"Invalid payload: {item} is not an integer")
    try:
        # Start timestamp
        started_at = datetime.now().isoformat()

        # Create a multiprocessing pool
        pool = multiprocessing.Pool()

        # Perform addition on input lists of integers in parallel
        result = pool.map(add_numbers, batch.payload)

        # Close the pool to free resources
        pool.close()
        pool.join()

        # End timestamp
        completed_at = datetime.now().isoformat()

        # Return BatchResponse with result and timestamps
        return BatchResponse(
            batchid=batch.batchid,
            response=result,
            status="complete",
            started_at=started_at,
            completed_at=completed_at
        )
    except Exception as e:
        # Log any errors
        logger.exception(f"Error processing batch {e}")
        # Raise HTTPException with 500 status code and error message
        raise HTTPException(status_code=500, detail="Internal server error")
