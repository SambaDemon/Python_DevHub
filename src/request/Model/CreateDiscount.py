import sys
from . .Utilities import Frozen

class CreateDiscount(object):
    DiscountCode = None
    Name = None
    Amount = None
    StartDate = None
    EndDate = None
    

    

    
    
    __setattr__=Frozen(object.__setattr__)