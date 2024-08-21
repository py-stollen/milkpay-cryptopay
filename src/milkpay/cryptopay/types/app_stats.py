from datetime import datetime

from stollen import StollenObject

from ..client import Cryptopay


class AppStats(StollenObject[Cryptopay]):
    volume: float
    conversion: float
    unique_users_count: int
    created_invoice_count: int
    paid_invoice_count: int
    start_at: datetime
    end_at: datetime
