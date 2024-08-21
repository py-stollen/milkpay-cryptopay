from stollen import StollenObject

from ..client import Cryptopay


class Balance(StollenObject[Cryptopay]):
    currency_code: str
    available: float
    onhold: float
