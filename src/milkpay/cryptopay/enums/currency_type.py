from enum import Enum


class CurrencyType(str, Enum):
    CRYPTO = "crypto"
    FIAT = "fiat"
