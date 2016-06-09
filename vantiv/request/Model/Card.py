from marshmallow import Schema, fields
from ..utilities import frozen
from ..enums import EnumField, CardTypeEnum


class CardSchema(Schema):
    CardNumber = fields.Integer()
    ExpirationMonth = fields.Integer()
    ExpirationYear = fields.Integer()
    CVV = fields.Integer()
    Track1Data = None
    Track2Data = None
    PaypageRegistrationID = None
    AccountNumber = None
    Type = EnumField(CardTypeEnum, by_value=True)


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
