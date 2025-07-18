import qrcode
import io
import base64
from QRRequestModel import QRRequest

class QRMaker:
    def generate_qr(self, req: QRRequest):
        qr = qrcode.QRCode(version=1, box_size=10, border=4)
        qr.add_data(req.text)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        buffered = io.BytesIO()
        img.save(buffered, format="PNG")  # <-- esto es importante
        img_str = base64.b64encode(buffered.getvalue()).decode("iso8859-15")
        return {"qr_base64": img_str}
