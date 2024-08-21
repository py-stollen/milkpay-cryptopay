from __future__ import annotations

import logging
from typing import Annotated, Any, Final

from fastapi import APIRouter, Body, Header, HTTPException
from starlette.requests import Request

from milkpay.cryptopay import Cryptopay
from milkpay.cryptopay.types import Update

router: Final[APIRouter] = APIRouter()
logger: Final[logging.Logger] = logging.getLogger(name=__name__)


@router.post("/webhook/cryptopay")
async def via_cryptopay(
    request: Request,
    crypto_pay_api_signature: Annotated[str, Header()],
    update: Annotated[Update, Body()],
) -> Any:
    cryptopay: Cryptopay = request.app.state.cryptopay
    if not cryptopay.check_signature(
        body_text=(await request.body()).decode(),
        crypto_pay_signature=crypto_pay_api_signature,
    ):
        raise HTTPException(status_code=401, detail="Invalid signature")
    logger.info("Received update with id %d", update.id)
