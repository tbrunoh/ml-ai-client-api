from pydantic import BaseModel

class SendEmailModel(BaseModel):
    fromAddress: str
    toAddress: str
    subject: str
    body: str