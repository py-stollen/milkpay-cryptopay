from typing import Optional

from stollen.enums import HTTPMethod

from ..types import Check
from ..types.custom import StringList
from .base import CryptopayMethod


class GetChecks(
    CryptopayMethod[list[Check]],
    http_method=HTTPMethod.GET,
    api_method="/getChecks",
    returning=list[Check],
    response_data_key=["items"],
):
    """
    Use this method to get invoices created by your app.
    On success, returns array of Invoice.

    Source: https://help.crypt.bot/crypto-pay-api#getInvoices
    """

    asset: Optional[str] = None
    check_ids: Optional[StringList] = None
    status: Optional[str] = None
    offset: Optional[int] = None
    count: Optional[int] = None
