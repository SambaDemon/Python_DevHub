import sys
from . .Utilities import Frozen

class CardholderAuthentication(object):
    AuthenticationValue = None
    AuthenticationTransactionID = None
    CustomerIpAddress = None
    AuthenticatedByMerchant = None
    

    

    
    
    __setattr__=Frozen(object.__setattr__)