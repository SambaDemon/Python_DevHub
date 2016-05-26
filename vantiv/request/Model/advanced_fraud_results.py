import sys
from . .Utilities import Frozen

class AdvancedFraudResults(object):
    DeviceReviewStatus = None
    DeviceReputationScore = None
    TriggeredRule = None
    
    
    __setattr__=Frozen(object.__setattr__)