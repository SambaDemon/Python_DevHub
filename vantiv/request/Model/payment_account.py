import sys
from . .Utilities import Frozen

class PaymentAccount(object):
    PaymentAccountID = None
    
    
    __setattr__=Frozen(object.__setattr__)