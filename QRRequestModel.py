from pydantic import BaseModel
from typing import Optional, Union


class QRRequest(BaseModel):
    text: str | dict
    isAfip: Optional[bool] = False