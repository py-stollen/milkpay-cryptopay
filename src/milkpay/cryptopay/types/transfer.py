from datetime import datetime
from typing import Optional

from stollen import StollenObject

from ..client import Cryptopay


class TransferType(StollenObject[Cryptopay]):
    transfer_id: int
    user_id: int
    asset: str
    amount: float
    status: str
    completed_at: datetime
    comment: Optional[str] = None
