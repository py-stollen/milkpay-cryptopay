from stollen.enums import HTTPMethod

from ..types import Balance
from .base import CryptopayMethod


class GetBalance(
    CryptopayMethod[list[Balance]],
    http_method=HTTPMethod.GET,
    api_method="/getBalance",
    returning=list[Balance],
):
    """
    Use this method to get balances of your app. Requires no parameters.
    Returns array of Balance.

    Source: https://help.crypt.bot/crypto-pay-api#getBalance
    """
