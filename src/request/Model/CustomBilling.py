import sys
from . .Utilities import Frozen

class CustomBilling(object):
    PhoneNumber = None
    Descriptor = None
    Url = None
    City = None
    
    
    __setattr__=Frozen(object.__setattr__)