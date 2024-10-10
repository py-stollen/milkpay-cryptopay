from enum import Enum


class Network(str, Enum):
    MAIN_NET = "pay.crypt.bot"
    TEST_NET = "testnet-pay.crypt.bot"
