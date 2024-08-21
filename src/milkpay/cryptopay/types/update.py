from datetime import datetime

from pydantic import Field
from stollen import StollenObject

from ..client import Cryptopay
from .invoice import Invoice


class Update(StollenObject[Cryptopay]):
    id: int = Field(alias="update_id")
    update_type: str
    request_date: datetime
    payload: Invoice
