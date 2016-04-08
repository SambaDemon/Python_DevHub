import sys
from . .Utilities import Frozen

class RecyclingRequest(object):
    RecycleID = None
    RecycleBy = None
    class RecycleByEnum(object):
        def __init__(self, value):
            self.value=value
    RecycleByEnum.MERCHANT = "Merchant"
    RecycleByEnum.LITLE = "Litle"
    RecycleByEnum.NONE = "None"
    __setattr__=Frozen(object.__setattr__)