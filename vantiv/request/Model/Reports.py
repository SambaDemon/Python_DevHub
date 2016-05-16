import sys
from . .Utilities import Frozen

class Reports(object):
    ReportGroup = None
    Affiliate = None
    Campaign = None
    MerchantGroupingID = None
    
    
    __setattr__=Frozen(object.__setattr__)