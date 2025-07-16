from fastapi import FastAPI
from QRRequestModel import QRRequest
from qr_make import QRMaker

app = FastAPI()

@app.post("/generate_qr", response_model=dict)
def generate_qr(req: QRRequest) -> dict:
    qr_maker = QRMaker()
    return qr_maker.generate_qr(req)
