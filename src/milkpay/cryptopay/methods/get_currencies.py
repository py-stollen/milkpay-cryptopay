from stollen.enums import HTTPMethod

from ..types import Currency
from .base import CryptopayMethod


class GetCurrencies(
    CryptopayMethod[list[Currency]],
    http_method=HTTPMethod.GET,
    api_method="/getCurrencies",
    returning=list[Currency],
):
    """
    Use this method to get a list of supported currencies. Requires no parameters.
    Returns a list of fiat and cryptocurrency alphabetic codes.

    Source: https://help.crypt.bot/crypto-pay-api#getCurrencies
    """
