from stollen import StollenMethod
from stollen.enums import HTTPMethod

from ..client import Cryptopay
from ..types import Profile


class GetMe(
    StollenMethod[Profile, Cryptopay],
    http_method=HTTPMethod.GET,
    api_method="/getMe",
    returning=Profile,
):
    """
    Use this method to test your app's authentication token. Requires no parameters.
    On success, returns basic information about an app.

    Source: https://help.crypt.bot/crypto-pay-api#getMe
    """
