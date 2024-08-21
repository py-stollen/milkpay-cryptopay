from stollen import StollenMethod
from stollen.enums import HTTPMethod

from ..client import Cryptopay


class DeleteInvoice(
    StollenMethod[bool, Cryptopay],
    http_method=HTTPMethod.POST,
    api_method="/deleteInvoice",
    returning=bool,
):
    """
    Use this method to delete invoices created by your app.
    Returns True on success.

    Source: https://help.crypt.bot/crypto-pay-api#deleteInvoice
    """

    invoice_id: int
