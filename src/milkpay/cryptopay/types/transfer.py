from datetime import datetime
from typing import Optional

from .base import CryptopayObject


class TransferType(CryptopayObject):
    transfer_id: int
    user_id: int
    asset: str
    amount: float
    status: str
    completed_at: datetime
    comment: Optional[str] = None
