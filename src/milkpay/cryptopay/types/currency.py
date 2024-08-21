from typing import Optional

from stollen import StollenObject

from ..client import Cryptopay


class Currency(StollenObject[Cryptopay]):
    is_blockchain: bool
    is_stablecoin: bool
    is_fiat: bool
    name: str
    code: str
    url: Optional[str] = None
    decimals: int
