from . .utilities import frozen


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
