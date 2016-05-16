import sys
from . .Utilities import Frozen

class Header(object):
    ApplicationData = None
    EphemeralPublicKey = None
    PublicKeyHash = None
    TransactionID = None
    
    
    __setattr__=Frozen(object.__setattr__)