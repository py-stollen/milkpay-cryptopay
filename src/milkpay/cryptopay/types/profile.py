from .base import CryptopayObject


class Profile(CryptopayObject):
    app_id: int
    name: str
    payment_processing_bot_username: str
