from .base import CryptopayObject


class ExchangeRate(CryptopayObject):
    is_valid: bool
    source: str
    target: str
    rate: float
