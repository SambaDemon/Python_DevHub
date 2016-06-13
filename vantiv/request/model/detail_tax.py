from ..schemas import Schema, fields
from ..utils import FrozenMixin


class DetailTaxSchema(Schema):
    TaxIncludedInTotal = fields.String()
    TaxAmount = fields.String()
    TaxRate = fields.String()
    AlternateTaxIdentifier = fields.String()
    TaxTypeIdentifier = fields.String()


class DetailTax(FrozenMixin):
    __schema__ = DetailTaxSchema

    TaxIncludedInTotal = None
    TaxAmount = None
    TaxRate = None
    AlternateTaxIdentifier = None
    TaxTypeIdentifier = None
