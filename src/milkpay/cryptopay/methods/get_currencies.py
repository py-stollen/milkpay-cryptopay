from stollen import StollenMethod
from stollen.enums import HTTPMethod

from ..client import Cryptopay
from ..types import Currency


class GetCurrencies(
    StollenMethod[list[Currency], Cryptopay],
    http_method=HTTPMethod.GET,
    api_method="/getCurrencies",
    returning=list[Currency],
):
    """
    Use this method to get a list of supported currencies. Requires no parameters.
    Returns a list of fiat and cryptocurrency alphabetic codes.

    Source: https://help.crypt.bot/crypto-pay-api#getCurrencies
    """
