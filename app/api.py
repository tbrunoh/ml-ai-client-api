from typing import List, Optional

from fastapi import APIRouter
from pydantic import BaseModel

from app.models.skintone_models import SkinToneResponse,SkinToneRequest
from mlaist.inference import classify_image


router = APIRouter(
    prefix="/skintone",
    tags=["skintone"]
)


@router.post('/infer', response_model=SkinToneResponse)
def generic_image(request: SkinToneRequest):
    response = classify_image(request.url)
    return response
