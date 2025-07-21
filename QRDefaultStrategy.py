from QRStrategy import QRStrategy

class QRDefaultStrategy(QRStrategy):
    def generate_qr(self, data: str) -> dict:
        return super().generate_default_qr(data)