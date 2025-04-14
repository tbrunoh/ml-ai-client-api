from pydantic import BaseModel

class SkinToneRequest(BaseModel):
    url: str
class SkinToneResponse(BaseModel):
    number: int
    name: str
    orb: str
