from ..schemas import Schema, fields
from ..utils import FrozenMixin


class PayPalSchema(Schema):
    PayerID = fields.String()
    Token = fields.String()
    TransactionID = fields.String()
    PayPalOrderComplete = fields.String()
    PayPalNotes = fields.String()


class PayPal(FrozenMixin):
    __schema__ = PayPalSchema

    PayerID = None
    Token = None
    TransactionID = None
    PayPalOrderComplete = None
    PayPalNotes = None
