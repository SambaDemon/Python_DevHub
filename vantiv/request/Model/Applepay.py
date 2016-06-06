from . .utilities import frozen


class Applepay(object):
    Data = None
    Header = None
    Signature = None
    Version = None

    __setattr__ = frozen(object.__setattr__)
