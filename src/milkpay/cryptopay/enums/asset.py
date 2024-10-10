from enum import Enum


class Asset(str, Enum):
    BTC = "BTC"
    TON = "TON"
    ETH = "ETH"
    USDT = "USDT"
    USDC = "USDC"
    BNB = "BNB"
    TRX = "TRX"
    LTC = "LTC"
    GRAM = "GRAM"
    NOT = "NOT"
    MY = "MY"
    SOL = "SOL"
