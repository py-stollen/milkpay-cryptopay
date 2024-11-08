from typing import Optional

from stollen.enums import HTTPMethod

from ..types import AppStats
from ..types.custom import DateTime
from .base import CryptopayMethod


class GetStats(
    CryptopayMethod[AppStats],
    http_method=HTTPMethod.GET,
    api_method="/getStats",
    returning=AppStats,
):
    """
    Use this method to get app statistics.
    On success, returns AppStats.

    Source: https://help.crypt.bot/crypto-pay-api#jvP3
    """

    start_at: Optional[DateTime] = None
    end_at: Optional[DateTime] = None
