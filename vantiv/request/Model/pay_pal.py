from ..schemas import Schema, fields
from ..utilities import frozen


class PayPalSchema(Schema):
    PayerID = fields.String()
    Token = fields.String()
    TransactionID = fields.String()
    PayPalOrderComplete = fields.String()
    PayPalNotes = fields.String()


class PayPal(object):
    __schema__ = PayPalSchema

    PayerID = None
    Token = None
    TransactionID = None
    PayPalOrderComplete = None
    PayPalNotes = None

    __setattr__ = frozen(object.__setattr__)
