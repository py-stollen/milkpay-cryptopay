from typing import Optional

from stollen.enums import HTTPMethod

from ..types import Check
from .base import CryptopayMethod


class CreateCheck(
    CryptopayMethod[Check],
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
