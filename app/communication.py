from typing import List, Optional

from fastapi import APIRouter
from app.models.communication_models import SendEmailModel
from app.services.communication_service import EmailService

router = APIRouter(
    prefix="/communication",
    tags=["communication"]
)


@router.post('/email/')
def generic_image(request: SendEmailModel):
    email = EmailService()
    try:
        response = email.send_email(request)
        return response
    except Exception as e:
        return {"error": str(e)}
