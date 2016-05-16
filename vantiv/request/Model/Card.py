import sys
from . .Utilities import Frozen

class Card(object):
    CardNumber = None
    ExpirationMonth = None
    ExpirationYear = None
    CVV = None
    Track1Data = None
    Track2Data = None
    PaypageRegistrationID = None
    AccountNumber = None
    Type = None
    class TypeEnum(object):
        def __init__(self, value):
            self.value=value
    TypeEnum.MC = "MC"
    TypeEnum.VI = "VI"
    TypeEnum.AX = "AX"
    TypeEnum.DC = "DC"
    TypeEnum.DI = "DI"
    TypeEnum.PP = "PP"
    TypeEnum.JC = "JC"
    TypeEnum.BL = "BL"
    TypeEnum.EC = "EC"
    TypeEnum.GC = "GC"
    TypeEnum.NONE = ""
    __setattr__=Frozen(object.__setattr__)