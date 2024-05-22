# batch_controller.py
import os
import logging
import multiprocessing
from datetime import datetime
from typing import List
from fastapi import HTTPException
from models.batch import BatchRequest, BatchResponse
# from .executor import ProcessPullExecutor


# Get the absolute path to the root directory of the application
root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Specify the absolute path to the log file in the root directory
log_file = os.path.join(root_dir, 'app.log')

# Configure logging to write logs to the specified log file
logging.basicConfig(filename=log_file, level=logging.INFO)
logger = logging.getLogger(__name__)

# Create a global instance of ProcessPulleceExecutor
# executor = ProcessPullExecutor()


def add_numbers(numbers: List[int]) -> List[int]:
    """Function to perform addition on a list of integers."""
    logger.info(f"Adding numbers: {numbers}")
    return [sum(numbers)]


def process_batch(batch: BatchRequest) -> BatchResponse:
    """Function to process batch using multiprocessing pool."""
    # Validate input payload blank or not
    if not batch.payload:
        # Update the status code to 400
        raise HTTPException(status_code=400, detail="Payload is empty")

    try:
        logger.info(f"Process batch with payload: {batch.payload}")
        # Start timestamp
        started_at = datetime.now().isoformat()

        # Create a multiprocessing pool
        pool = multiprocessing.Pool()

        # Perform addition on input lists of integers in parallel
        result = pool.map(add_numbers, batch.payload)
        # result = executor.map(add_numbers, batch.payload)
        logger.info(f"Processed Result: {result}")
        # Close the pool to free resources
        pool.close()
        pool.join()
        # executor.shutdown()

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
        logger.exception(f"Error processing batch: {e}")
        # Raise HTTPException with 500 status code and error message
        raise HTTPException(status_code=500, detail="Internal server error")
    
