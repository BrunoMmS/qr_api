from abc import ABC, abstractmethod

class QRStrategy(ABC):
    @abstractmethod
    def generate_qr(self, data: str) -> dict:
        pass