### Python Assignment:

1. Task is to set up a FastAPI project and create an endpoint with request and response
validation using Pydantic models.
2. Implement the logic to perform addition on input lists of integers using Python's
multiprocessing pool, with appropriate error handling and logging for debugging and
monitoring activities.
3. Write unit tests for all edge cases and scenarios.
4. Additionally, please organize your project structure following the MVC (Model-View-
Controller) format.


> The request format should be as follows:

```
{
"batchid": "id0101",
"payload": [[1, 2], [3, 4]]
}
```

> The response format should be as follows:

```
{
"batchid": "id0101",
"response": [3, 7],
"status": "complete",
"started_at": "&lt;timestamp&gt;",
"completed_at": "&lt;timestamp&gt;"
}
```

### Application 

In the context of a FastAPI application structured according to the Model-View-Controller (MVC) pattern, the "view" typically corresponds to the router or endpoint definitions in your application. The view is responsible for handling incoming requests, invoking the appropriate logic (controller), and returning the response.


To run and test this FastAPI application along with sample test data, follow these steps:

1. **Install Dependencies**: First, make sure you have installed the required dependencies listed in your `requirements.txt` file. You can do this by running:

    ```
    pip install -r requirements.txt
    ```

2. **Run the FastAPI Application**: You can run your FastAPI application using the `uvicorn` ASGI server. Assuming your main script is named `main.py`, run the following command:

    ```
    uvicorn main:app --reload --log-config log.ini
    ```

    This command starts the FastAPI application and enables auto-reloading so that any changes you make to your code are automatically picked up without needing to restart the server.

3. **Test the Endpoints**: You can test your API endpoints using tools like cURL, Postman, or by writing Python scripts. Below are some sample test data and ways to test your endpoints:

    - **POST /add_numbers Endpoint**: This endpoint adds numbers in a list.
    
        Test Data:
        ```json
        {
            "numbers": [1, 2, 3, 4]
        }
        ```

        You can test this endpoint using cURL:
        ```
        curl -X POST "http://localhost:8000/add_number" -H "Content-Type: application/json" -d '{"numbers": [1, 2, 3, 4]}'
        ```

    - **POST /process_batch Endpoint**: This endpoint processes a batch of numbers using multiprocessing.

        Test Data:
        ```json
        {
            "batchid": "id0101",
            "payload": [[1, 2], [3, 4], [5, 6]]
        }
        ```

        You can test this endpoint using cURL:
        ```
        curl -X POST "http://localhost:8000/process_batch" -H "Content-Type: application/json" -d '{"batchid": "id0101", "payload": [[1, 2], [3, 4], [5, 6]]}'
        ```
4. **Unit Test**: To run the unit tests run `pytest tests/`

5. **Github Action**: Github action workflow added to make auto build and deploy whenever pushes the code into main.

