from typing import List, Optional
from fastapi import APIRouter, UploadFile, File

import mlaicore.azure_storage as storage

app = APIRouter(
    prefix="/upload",
    tags=["upload"]
)

@app.post("/images/")
async def upload_image(image: UploadFile = File(...)):
    data = storage.getBlobName(image.filename ,"images", True)
    filename = await storage.uploadImage(data["filename"], data["blob_name"], image)
    return {
        "filename" : filename
    }
