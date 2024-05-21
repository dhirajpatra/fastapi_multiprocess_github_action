from fastapi import FastAPI
from routers.batch_router import batch_router
import logging.config

# Load logging configuration from log.ini file
logging.config.fileConfig('log.ini', disable_existing_loggers=False)

app = FastAPI()

# Include routers
app.include_router(batch_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000,
                log_config="log.ini", reload=True)
    