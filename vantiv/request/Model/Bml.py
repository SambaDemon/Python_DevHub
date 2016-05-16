import sys
from . .Utilities import Frozen

class Bml(object):
    MerchantID = None
    ProductType = None
    TermsAndConditions = None
    PreApprovalNumber = None
    VirtualAuthenticationKeyPresenceIndicator = None
    VirtualAuthenticationKeyData = None
    ItemCategoryCode = None
    
    
    __setattr__=Frozen(object.__setattr__)