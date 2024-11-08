from stollen import StollenMethod
from stollen.types import StollenT

from ..client import Cryptopay


class CryptopayMethod(
    StollenMethod[StollenT, Cryptopay],
    abstract=True,
):
    pass
