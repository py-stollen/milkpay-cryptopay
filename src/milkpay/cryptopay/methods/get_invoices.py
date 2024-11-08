from typing import Optional

from stollen.enums import HTTPMethod

from ..types import Invoice
from ..types.custom import StringList
from .base import CryptopayMethod


class GetInvoices(
    CryptopayMethod[list[Invoice]],
    http_method=HTTPMethod.GET,
    api_method="/getInvoices",
    returning=list[Invoice],
    response_data_key=["items"],
):
    """
    Use this method to get invoices created by your app.
    On success, returns array of Invoice.

    Source: https://help.crypt.bot/crypto-pay-api#getInvoices
    """

    asset: Optional[str] = None
    invoice_ids: Optional[StringList] = None
    status: Optional[str] = None
    offset: Optional[int] = None
    count: Optional[int] = None
