from stollen import StollenMethod
from stollen.enums import HTTPMethod

from ..client import Cryptopay
from ..types import Balance


class GetBalance(
    StollenMethod[list[Balance], Cryptopay],
    http_method=HTTPMethod.GET,
    api_method="/getBalance",
    returning=list[Balance],
):
    """
    Use this method to get balances of your app. Requires no parameters.
    Returns array of Balance.

    Source: https://help.crypt.bot/crypto-pay-api#getBalance
    """
