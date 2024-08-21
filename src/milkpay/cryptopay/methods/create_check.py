from typing import Optional

from stollen import StollenMethod
from stollen.enums import HTTPMethod

from ..client import Cryptopay
from ..types import Check


class CreateCheck(
    StollenMethod[Check, Cryptopay],
    http_method=HTTPMethod.POST,
    api_method="/createCheck",
    returning=Check,
):
    """
    Use this method to create a new check.
    On success, returns an object of the created check.

    Source: https://help.crypt.bot/crypto-pay-api#createCheck
    """

    asset: str
    amount: float
    pin_to_user_id: Optional[int] = None
    pin_to_username: Optional[str] = None
