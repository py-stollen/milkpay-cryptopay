from typing import Optional

from stollen import StollenMethod
from stollen.enums import HTTPMethod

from ..client import Cryptopay
from ..types import TransferType
from ..types.custom import StringList


class GetTransfers(
    StollenMethod[list[TransferType], Cryptopay],
    http_method=HTTPMethod.GET,
    api_method="/getTransfers",
    returning=list[TransferType],
    response_data_key=["items"],
):
    """
    Use this method to get transfers created by your app.
    On success, returns array of TransferType.

    Source: https://help.crypt.bot/crypto-pay-api#getTransfers
    """

    asset: Optional[str] = None
    transfer_ids: Optional[StringList] = None
    offset: Optional[int] = None
    count: Optional[int] = None
