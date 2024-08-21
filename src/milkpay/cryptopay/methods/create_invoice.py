from typing import Optional

from stollen import StollenMethod
from stollen.enums import HTTPMethod

from ..client import Cryptopay
from ..types import Invoice
from ..types.custom import StringList


class CreateInvoice(
    StollenMethod[Invoice, Cryptopay],
    http_method=HTTPMethod.POST,
    api_method="/createInvoice",
    returning=Invoice,
):
    """
    Use this method to create a new invoice.
    On success, returns an object of the created invoice.

    Source: https://help.crypt.bot/crypto-pay-api#createInvoice
    """

    currency_type: Optional[str] = None
    asset: Optional[str] = None
    fiat: Optional[str] = None
    accepted_assets: Optional[StringList] = None
    amount: float
    description: Optional[str] = None
    hidden_message: Optional[str] = None
    paid_btn_name: Optional[str] = None
    paid_btn_url: Optional[str] = None
    payload: Optional[str] = None
    allow_comments: Optional[bool] = None
    allow_anonymous: Optional[bool] = None
    expires_in: Optional[int] = None
