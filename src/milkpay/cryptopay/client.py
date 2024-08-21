from __future__ import annotations

from datetime import datetime
from hashlib import sha256
from hmac import HMAC
from typing import TYPE_CHECKING, Any, Optional

from stollen import Stollen
from stollen.requests.fields import Header

from .enums import Network
from .exceptions import (
    CryptopayAPIError,
    CryptopayBadRequestError,
    CryptopayForbiddenError,
    CryptopayNotFoundError,
    CryptopayUnauthorizedError,
)

if TYPE_CHECKING:
    from .types import (
        AppStats,
        Balance,
        Check,
        Currency,
        ExchangeRate,
        Invoice,
        Profile,
        TransferType,
    )


class Cryptopay(Stollen):
    def __init__(
        self,
        api_token: str,
        production: bool = True,
        **stollen_kwargs: Any,
    ) -> None:
        if not isinstance(api_token, str):
            raise TypeError("api_token must be a string!")
        self._api_token = api_token
        self._production = production
        host: str = Network.MAIN_NET if production else Network.TEST_NET
        super().__init__(
            base_url=f"https://{host}/api",
            global_request_fields=[
                Header(name="Host", value=host),
                Header(name="Crypto-Pay-API-Token", value=api_token),
            ],
            response_data_key=["result"],
            error_message_key=["error", "name"],
            general_error_class=CryptopayAPIError,
            error_codes={
                400: CryptopayBadRequestError,
                401: CryptopayUnauthorizedError,
                403: CryptopayForbiddenError,
                404: CryptopayNotFoundError,
            },
            **stollen_kwargs,
        )

    @property
    def api_token(self) -> str:
        return self._api_token

    @property
    def production(self) -> bool:
        return self._production

    def check_signature(self, body_text: str, crypto_pay_signature: str) -> bool:
        """
        You can verify the received update and the integrity
        of the received data by comparing the header parameter
        crypto-pay-api-signature and the hexadecimal representation
        of HMAC-SHA-256 signature used to sign the entire request body
        (unparsed JSON string) with a secret key that is SHA256 hash of your app's token.

        Source: https://help.crypt.bot/crypto-pay-api#verifying-webhook-updates
        """
        hmac: HMAC = HMAC(
            key=sha256(string=self._api_token.encode("utf-8")).digest(),
            msg=body_text.encode("UTF-8"),
            digestmod=sha256,
        )
        return hmac.hexdigest() == crypto_pay_signature

    async def create_check(
        self,
        *,
        asset: str,
        amount: float,
        pin_to_user_id: Optional[int] = None,
        pin_to_username: Optional[str] = None,
    ) -> Check:
        from .methods import CreateCheck

        call: CreateCheck = CreateCheck(
            asset=asset,
            amount=amount,
            pin_to_user_id=pin_to_user_id,
            pin_to_username=pin_to_username,
        )
        return await self(call)

    async def create_invoice(
        self,
        *,
        currency_type: Optional[str] = None,
        asset: Optional[str] = None,
        fiat: Optional[str] = None,
        accepted_assets: Optional[list[str]] = None,
        amount: float,
        description: Optional[str] = None,
        hidden_message: Optional[str] = None,
        paid_btn_name: Optional[str] = None,
        paid_btn_url: Optional[str] = None,
        payload: Optional[str] = None,
        allow_comments: Optional[bool] = None,
        allow_anonymous: Optional[bool] = None,
        expires_in: Optional[int] = None,
    ) -> Invoice:
        from .methods import CreateInvoice

        call: CreateInvoice = CreateInvoice(
            currency_type=currency_type,
            asset=asset,
            fiat=fiat,
            accepted_assets=accepted_assets,
            amount=amount,
            description=description,
            hidden_message=hidden_message,
            paid_btn_name=paid_btn_name,
            paid_btn_url=paid_btn_url,
            payload=payload,
            allow_comments=allow_comments,
            allow_anonymous=allow_anonymous,
            expires_in=expires_in,
        )
        return await self(call)

    async def delete_check(self, *, check_id: int) -> bool:
        from .methods import DeleteCheck

        call: DeleteCheck = DeleteCheck(check_id=check_id)
        return await self(call)

    async def delete_invoice(self, *, invoice_id: int) -> bool:
        from .methods import DeleteInvoice

        call: DeleteInvoice = DeleteInvoice(invoice_id=invoice_id)
        return await self(call)

    async def get_balance(self) -> list[Balance]:
        from .methods import GetBalance

        call: GetBalance = GetBalance()
        return await self(call)

    async def get_checks(
        self,
        *,
        asset: Optional[str] = None,
        check_ids: Optional[list[int]] = None,
        status: Optional[str] = None,
        offset: Optional[int] = None,
        count: Optional[int] = None,
    ) -> list[Check]:
        from .methods import GetChecks

        call: GetChecks = GetChecks(
            asset=asset,
            check_ids=check_ids,
            status=status,
            offset=offset,
            count=count,
        )
        return await self(call)

    async def get_currencies(self) -> list[Currency]:
        from .methods import GetCurrencies

        call: GetCurrencies = GetCurrencies()
        return await self(call)

    async def get_exchange_rates(self) -> list[ExchangeRate]:
        from .methods import GetExchangeRates

        call: GetExchangeRates = GetExchangeRates()
        return await self(call)

    async def get_invoices(
        self,
        *,
        asset: Optional[str] = None,
        invoice_ids: Optional[list[int]] = None,
        status: Optional[str] = None,
        offset: Optional[int] = None,
        count: Optional[int] = None,
    ) -> list[Invoice]:
        from .methods import GetInvoices

        call: GetInvoices = GetInvoices(
            asset=asset,
            invoice_ids=invoice_ids,
            status=status,
            offset=offset,
            count=count,
        )
        return await self(call)

    async def get_me(self) -> Profile:
        from .methods import GetMe

        call: GetMe = GetMe()
        return await self(call)

    async def get_stats(
        self,
        *,
        start_at: Optional[datetime] = None,
        end_at: Optional[datetime] = None,
    ) -> AppStats:
        from .methods import GetStats

        call: GetStats = GetStats(
            start_at=start_at,
            end_at=end_at,
        )
        return await self(call)

    async def get_transfers(
        self,
        *,
        asset: Optional[str] = None,
        transfer_ids: Optional[list[int]] = None,
        offset: Optional[int] = None,
        count: Optional[int] = None,
    ) -> list[TransferType]:
        from .methods import GetTransfers

        call: GetTransfers = GetTransfers(
            asset=asset,
            transfer_ids=transfer_ids,
            offset=offset,
            count=count,
        )
        return await self(call)

    async def transfer(
        self,
        *,
        user_id: int,
        asset: str,
        amount: float,
        spend_id: int,
        comment: Optional[str] = None,
        disable_send_notification: Optional[bool] = None,
    ) -> TransferType:
        from .methods import Transfer

        call: Transfer = Transfer(
            user_id=user_id,
            asset=asset,
            amount=amount,
            spend_id=spend_id,
            comment=comment,
            disable_send_notification=disable_send_notification,
        )
        return await self(call)
