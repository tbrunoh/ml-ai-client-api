from typing import List, Optional

from fastapi import APIRouter
from pydantic import BaseModel

from models.api_models import SkinToneResponse,SkinToneRequest
from mlaist.inference import classify_image


router = APIRouter(
    prefix="/skintone",
    tags=["skintone"]
)


@router.post('/infer', response_model=SkinToneResponse)
def generic_image(request: SkinToneRequest):
    response = classify_image(request.url)
    return response


# Example usage
# image_path_or_url = 'https://sdrimltdata.blob.core.windows.net/melanintrainingimages/mst/PXL_20220922_185757301.jpg'  #input("Enter the image path or URL: ")
# result = classify_image(image_path_or_url)
# print(result)