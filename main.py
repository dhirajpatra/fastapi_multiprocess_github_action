# main.py
from fastapi import FastAPI
from controllers.batch_controller import batch_router
import logging.config

# Load logging configuration from log.ini file
logging.config.fileConfig('log.ini', disable_existing_loggers=False)

app = FastAPI()

# Include routers
app.include_router(batch_router)
