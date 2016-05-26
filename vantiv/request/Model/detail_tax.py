from . .utilities import frozen


class DetailTax(object):
    TaxIncludedInTotal = None
    TaxAmount = None
    TaxRate = None
    AlternateTaxIdentifier = None
    TaxTypeIdentifier = None

    __setattr__ = frozen(object.__setattr__)
