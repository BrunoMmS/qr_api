import qrcode
import io
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

        qr = qrcode.QRCode(version=1, box_size=10, border=4)
        qr.add_data(qr_data)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        buffered = io.BytesIO()
        img.save(buffered, format="PNG")
        img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")

        return {"qr_base64": img_str}
