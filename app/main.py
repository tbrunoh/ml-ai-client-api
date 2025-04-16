import logging
import os
import sys

from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import app.api as api

# Configure logging
logging.basicConfig(
    level=os.getenv('LOG_LEVEL', 'INFO'),  # Set the logging level to INFO
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler()  # Log to console
    ]
)
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI(
    title="Melanin Luxe Inference API",
    description="Melanin Luxe Inference API",
    version="1.0.0",
)

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:4200",
    "https://ml-ai-st-ui-a3chcug0c6g9a5b6.centralus-01.azurewebsites.net",  # Add your Next.js app's domain here

]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api.router)


@app.get("/health", include_in_schema=False)
def health():
    return {'status': 'Healthy'}