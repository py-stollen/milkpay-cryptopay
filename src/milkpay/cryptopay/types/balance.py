from .base import CryptopayObject


class Balance(CryptopayObject):
    currency_code: str
    available: float
    onhold: float
