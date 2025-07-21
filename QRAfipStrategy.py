import base64
import json
from QRStrategy import QRStrategy
from QRRequestModel import QRRequest  

class QRAfipStrategy(QRStrategy):
    def generate_qr(self, data) -> dict:
        url_afip = "https://www.afip.gob.ar/fe/qr/?p="

        if isinstance(data, dict):
            text_str = json.dumps(data, separators=(',', ':'))  
        else:
            text_str = data

        data_base64 = base64.b64encode(text_str.encode('utf-8')).decode('utf-8')
        qr_data = url_afip + data_base64

        return super().generate_default_qr(qr_data)
