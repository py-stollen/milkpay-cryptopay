from stollen.enums import HTTPMethod

from ..types import ExchangeRate
from .base import CryptopayMethod


class GetExchangeRates(
    CryptopayMethod[list[ExchangeRate]],
    http_method=HTTPMethod.GET,
    api_method="/getExchangeRates",
    returning=list[ExchangeRate],
):
    """
    Use this method to get a list of supported currencies. Requires no parameters.
    Returns a list of fiat and cryptocurrency alphabetic codes.

    Source: https://help.crypt.bot/crypto-pay-api#getExchangeRates
    """
