from stollen.enums import HTTPMethod

from ..types import Profile
from .base import CryptopayMethod


class GetMe(
    CryptopayMethod[Profile],
    http_method=HTTPMethod.GET,
    api_method="/getMe",
    returning=Profile,
):
    """
    Use this method to test your app's authentication token. Requires no parameters.
    On success, returns basic information about an app.

    Source: https://help.crypt.bot/crypto-pay-api#getMe
    """
