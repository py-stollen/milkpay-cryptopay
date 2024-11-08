from stollen.enums import HTTPMethod

from .base import CryptopayMethod


class DeleteCheck(
    CryptopayMethod[bool],
    http_method=HTTPMethod.POST,
    api_method="/deleteCheck",
    returning=bool,
):
    """
    Use this method to delete checks created by your app.
    Returns True on success.

    Source: https://help.crypt.bot/crypto-pay-api#deleteCheck
    """

    check_id: int
