import sys
from . .Utilities import Frozen

class DemandDepositAccount(object):
    DDAAccountType = None
    AccountNumber = None
    RoutingNumber = None
    CheckNumber = None
    CCDPaymentInformation = None
    

    

    
    
    __setattr__=Frozen(object.__setattr__)