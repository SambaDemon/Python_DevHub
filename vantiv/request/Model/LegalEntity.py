import sys
from . .Utilities import Frozen

class LegalEntity(object):
    Name = None
    Type = None
    DoingBusinessAs = None
    TaxID = None
    Phone = None
    AnnualCreditCardSalesVolume = None
    HasAcceptedCreditCards = None
    YearsInBusiness = None
    

    

    
    
    __setattr__=Frozen(object.__setattr__)