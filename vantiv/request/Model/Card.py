from marshmallow import Schema, fields
from . .utilities import frozen


class CardSchema(Schema):
    CardNumber = fields.Integer()
    ExpirationMonth = fields.Integer()
    ExpirationYear = fields.Integer()
    CVV = None
    Track1Data = None
    Track2Data = None
    PaypageRegistrationID = None
    AccountNumber = None
    Type = None


class Card(object):
    __schema__ = CardSchema

    CardNumber = None
    ExpirationMonth = None
    ExpirationYear = None
    CVV = None
    Track1Data = None
    Track2Data = None
    PaypageRegistrationID = None
    AccountNumber = None
    Type = None

    __setattr__ = frozen(object.__setattr__)
