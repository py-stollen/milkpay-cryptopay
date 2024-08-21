from typing import Optional

from stollen import StollenMethod
from stollen.enums import HTTPMethod

from ..client import Cryptopay
from ..types import AppStats
from ..types.custom import DateTime


class GetStats(
    StollenMethod[AppStats, Cryptopay],
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
