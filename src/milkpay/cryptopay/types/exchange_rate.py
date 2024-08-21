from stollen import StollenObject

from ..client import Cryptopay


class ExchangeRate(StollenObject[Cryptopay]):
    is_valid: bool
    source: str
    target: str
    rate: float
