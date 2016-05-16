import sys
from . .Utilities import Frozen

class ECheck(object):
    Enabled = None
    CompanyName = None
    BillingDescriptor = None
    

    

    
    
    __setattr__=Frozen(object.__setattr__)