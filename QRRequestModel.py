from pydantic import BaseModel

class QRRequest(BaseModel):
    text: str
    isAfip: bool = False