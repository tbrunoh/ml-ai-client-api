from typing import List, Optional

from fastapi import APIRouter
from pydantic import BaseModel

from models.api_models import SkinToneResponse,SkinToneRequest
from mlaist.inference import classify_image


router = APIRouter(
    prefix="/skintones", #temp will be renamed later
    tags=["skintones"]
)


@router.post('/inferance', response_model=SkinToneResponse)
def inference(request: SkinToneRequest):
    response = classify_image(request.url)
    return response
