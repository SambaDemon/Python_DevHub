from ..schemas import Schema, fields
from ..utilities import frozen


class WalletSchema(Schema):
    WalletSourceType = fields.String()
    WalletSourceTypeID = fields.String()


class Wallet(object):
    __schema__ = WalletSchema

    WalletSourceType = None
    WalletSourceTypeID = None

    __setattr__ = frozen(object.__setattr__)
