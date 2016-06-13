from ..schemas import Schema, fields
from ..utils import FrozenMixin


class HeaderSchema(Schema):
    ApplicationData = fields.String()
    EphemeralPublicKey = fields.String()
    PublicKeyHash = fields.String()
    TransactionID = fields.String()


class Header(FrozenMixin):
    __schema__ = HeaderSchema

    ApplicationData = None
    EphemeralPublicKey = None
    PublicKeyHash = None
    TransactionID = None
