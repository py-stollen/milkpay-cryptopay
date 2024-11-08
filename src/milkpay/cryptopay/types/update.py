from datetime import datetime

from pydantic import Field

from .base import CryptopayObject
from .invoice import Invoice


class Update(CryptopayObject):
    id: int = Field(alias="update_id")
    update_type: str
    request_date: datetime
    payload: Invoice
