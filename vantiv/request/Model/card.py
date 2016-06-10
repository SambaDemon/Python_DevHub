from ..schemas import Schema, fields
from ..utilities import frozen
from ..enums import EnumField, CardTypeEnum


class CardSchema(Schema):
    CardNumber = fields.String()
    ExpirationMonth = fields.String()
    ExpirationYear = fields.String()
    CVV = fields.Integer()
    Track1Data = fields.String()
    Track2Data = fields.String()
    PaypageRegistrationID = fields.String()
    AccountNumber = fields.String()
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
