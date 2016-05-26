from . .utilities import frozen


class Terminal(object):
    TerminalID = None
    Capability = None
    EntryMode = None
    CardholderID = None
    CapabilityOfCatTerminal = None
    __setattr__ = frozen(object.__setattr__)
