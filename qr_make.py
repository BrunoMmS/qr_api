from QRRequestModel import QRRequest
from QRStrategy import QRStrategy
from QRDefaultStrategy import QRDefaultStrategy
from QRAfipStrategy import QRAfipStrategy

class QRMaker:
    def __init__(self):
        self.qrStrategy: QRStrategy = None
    
    def generate_qr(self, req: QRRequest):
        self.__setStrategy(req.isAfip)
        return self.qrStrategy.generate_qr(req.text)

    def __setStrategy(self, isAfip: bool):
        if isAfip:
            self.qrStrategy = QRAfipStrategy()
        else:
            self.qrStrategy = QRDefaultStrategy()

        