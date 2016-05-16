import sys
from . .Utilities import Frozen

class Visa(object):
    DebtRepayment = None
    
    
    __setattr__=Frozen(object.__setattr__)