import sys
from . .Utilities import Frozen

class PayPal(object):
    PayerID = None
    Token = None
    TransactionID = None
    PayPalOrderComplete = None
    PayPalNotes = None
    
    
    __setattr__=Frozen(object.__setattr__)