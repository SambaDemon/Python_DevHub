import sys
from . .Utilities import Frozen

class PrimaryContact(object):
    FirstName = None
    LastName = None
    Email = None
    Phone = None
    

    

    
    
    __setattr__=Frozen(object.__setattr__)