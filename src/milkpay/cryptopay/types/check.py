from datetime import datetime
from typing import Optional

from pydantic import Field
from stollen import StollenObject

from ..client import Cryptopay


class Check(StollenObject[Cryptopay]):
    id: int = Field(alias="check_id")
    hash: str
    asset: str
    amount: float
    bot_check_url: str
    status: str
    created_at: datetime
    activated_at: Optional[datetime] = None
