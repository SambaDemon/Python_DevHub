from ..schemas import Schema, fields
from ..utilities import frozen


class DetailTaxSchema(Schema):
    TaxIncludedInTotal = fields.String()
    TaxAmount = fields.String()
    TaxRate = fields.String()
    AlternateTaxIdentifier = fields.String()
    TaxTypeIdentifier = fields.String()


class DetailTax(object):
    __schema__ = DetailTaxSchema

    TaxIncludedInTotal = None
    TaxAmount = None
    TaxRate = None
    AlternateTaxIdentifier = None
    TaxTypeIdentifier = None

    __setattr__ = frozen(object.__setattr__)
