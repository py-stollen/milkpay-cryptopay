from typing import Optional

from .base import CryptopayObject


class Currency(CryptopayObject):
    is_blockchain: bool
    is_stablecoin: bool
    is_fiat: bool
    name: str
    code: str
    url: Optional[str] = None
    decimals: int
