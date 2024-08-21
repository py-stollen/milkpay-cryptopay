from typing import Optional

from stollen import StollenMethod
from stollen.enums import HTTPMethod

from ..client import Cryptopay
from ..types import TransferType


class Transfer(
    StollenMethod[TransferType, Cryptopay],
    http_method=HTTPMethod.POST,
    api_method="/transfer",
    returning=TransferType,
):
    """
    Use this method to send coins from your app's balance to a user.
    On success, returns completed transfer.

    This method must first be enabled in the security settings of your app.
    Open @CryptoBot (@CryptoTestnetBot for testnet),
    go to CryptoPay → MyApps, choose an app,
    then go to Security -> Transfers... and tap Enable.

    Source: https://help.crypt.bot/crypto-pay-api#transfer
    """

    user_id: int
    asset: str
    amount: float
    spend_id: int
    comment: Optional[str] = None
    disable_send_notification: Optional[bool] = None
