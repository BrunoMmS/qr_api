from abc import ABC, abstractmethod
import qrcode
import io
import base64

class QRStrategy(ABC):
    @abstractmethod
    def generate_qr(self, data: str) -> dict:
        pass

    def generate_default_qr(self, data: str) -> dict:
        qr = qrcode.QRCode(version=1, box_size=10, border=4)
        qr.add_data(data)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        buffered = io.BytesIO()
        img.save(buffered, format="PNG")
        img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")
        return {"qr_base64": img_str}