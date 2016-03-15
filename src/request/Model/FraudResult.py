import sys
from . .Utilities import Frozen

class FraudResult(object):
    AvsResult = None
    CardValidationResult = None
    AuthenticationResult = None
    AdvancedAVSResult = None
    AdvancedFraudResults = None
    

    

    
    
    __setattr__=Frozen(object.__setattr__)