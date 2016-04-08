import sys
from . .Utilities import Frozen

class Terminal(object):
    TerminalID = None
    Capability = None
    EntryMode = None
    CardholderID = None
    CapabilityOfCatTerminal = None
    class CapabilityEnum(object):
        def __init__(self, value):
            self.value=value
    CapabilityEnum.NOT_USED = "notused"
    CapabilityEnum.MAG_STRIPE = "magstripe"
    CapabilityEnum.KEYED_ONLY = "keyedonly"
    class EntryModeEnum(object):
        def __init__(self, value):
            self.value=value
    EntryModeEnum.NOT_USED = "notused"
    EntryModeEnum.KEYED = "keyed"
    EntryModeEnum.TRACK1 = "track1"
    EntryModeEnum.TRACK2 = "track2"
    EntryModeEnum.COMPLETE_READ = "completeread"
    class CardholderIDEnum(object):
        def __init__(self, value):
            self.value=value
    CardholderIDEnum.SIGNATURE = "signature"
    CardholderIDEnum.PIN = "pin"
    CardholderIDEnum.NO_PIN = "nopin"
    CardholderIDEnum.DIRECT_MARKET = "directmarket"
    class CapabilityOfCatTerminalEnum(object):
        def __init__(self, value):
            self.value=value
    CapabilityOfCatTerminalEnum.SELF_SERVICE = "self service"
    __setattr__=Frozen(object.__setattr__)