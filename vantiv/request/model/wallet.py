from ..schemas import Schema, fields
from ..utils import FrozenMixin


class WalletSchema(Schema):
    WalletSourceType = fields.String()
    WalletSourceTypeID = fields.String()


class Wallet(FrozenMixin):
    __schema__ = WalletSchema

    WalletSourceType = None
    WalletSourceTypeID = None
