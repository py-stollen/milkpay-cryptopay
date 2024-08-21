from stollen import StollenMethod
from stollen.enums import HTTPMethod

from ..client import Cryptopay
from ..types import ExchangeRate


class GetExchangeRates(
    StollenMethod[list[ExchangeRate], Cryptopay],
    http_method=HTTPMethod.GET,
    api_method="/getExchangeRates",
    returning=list[ExchangeRate],
):
    """
    Use this method to get a list of supported currencies. Requires no parameters.
    Returns a list of fiat and cryptocurrency alphabetic codes.

    Source: https://help.crypt.bot/crypto-pay-api#getExchangeRates
    """
