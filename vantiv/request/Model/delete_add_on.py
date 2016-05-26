import sys
from . .Utilities import Frozen

class DeleteAddOn(object):
    AddOnCode = None
    
    
    __setattr__=Frozen(object.__setattr__)