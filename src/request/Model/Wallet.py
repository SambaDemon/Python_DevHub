import sys
from . .Utilities import Frozen

class Wallet(object):
    WalletSourceType = None
    WalletSourceTypeID = None
    
    
    __setattr__=Frozen(object.__setattr__)