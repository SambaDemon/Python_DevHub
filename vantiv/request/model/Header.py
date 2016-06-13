from ..schemas import Schema, fields
from ..utilities import frozen


class HeaderSchema(Schema):
    ApplicationData = fields.String()
    EphemeralPublicKey = fields.String()
    PublicKeyHash = fields.String()
    TransactionID = fields.String()


class Header(object):
    __schema__ = HeaderSchema

    ApplicationData = None
    EphemeralPublicKey = None
    PublicKeyHash = None
    TransactionID = None

    __setattr__ = frozen(object.__setattr__)
