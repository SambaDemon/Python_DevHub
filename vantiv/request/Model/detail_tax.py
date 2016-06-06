from . .utilities import frozen


class DetailTax(object):
    TaxIncludedInTotal = None
    TaxAmount = None
    TaxRate = None
    AlternateTaxIdentifier = None
    TaxTypeIdentifier = None

    class TaxTypeIdentifierEnum(object):
        def __init__(self, value):
            self.value = value

    TaxTypeIdentifierEnum.UNKOWN = "00"
    TaxTypeIdentifierEnum.NATL_SALES = "01"
    TaxTypeIdentifierEnum.ST_SALES = "02"
    TaxTypeIdentifierEnum.CTY_SALES = "03"
    TaxTypeIdentifierEnum.LCL_SALES = "04"
    TaxTypeIdentifierEnum.MUN_SALES = "05"
    TaxTypeIdentifierEnum.OTHER = "06"
    TaxTypeIdentifierEnum.VAT = "10"
    TaxTypeIdentifierEnum.GST = "11"
    TaxTypeIdentifierEnum.PST = "12"
    TaxTypeIdentifierEnum.HST = "13"
    TaxTypeIdentifierEnum.QST = "14"
    TaxTypeIdentifierEnum.ROOM = "20"
    TaxTypeIdentifierEnum.OCCUPANCY = "21"
    TaxTypeIdentifierEnum.ENERGY = "22"

    __setattr__ = frozen(object.__setattr__)
