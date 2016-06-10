from ..schemas import Schema, fields
from ..utilities import frozen


class LegalEntitySchema(Schema):
    Name = fields.String()
    Type = fields.String()
    DoingBusinessAs = fields.String()
    TaxID = fields.String()
    Phone = fields.String()
    AnnualCreditCardSalesVolume = fields.String()
    HasAcceptedCreditCards = fields.String()
    YearsInBusiness = fields.Int()


class LegalEntity(object):
    Name = None
    Type = None
    DoingBusinessAs = None
    TaxID = None
    Phone = None
    AnnualCreditCardSalesVolume = None
    HasAcceptedCreditCards = None
    YearsInBusiness = None

    __setattr__ = frozen(object.__setattr__)
