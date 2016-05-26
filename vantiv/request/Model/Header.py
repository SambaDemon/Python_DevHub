from . .utilities import frozen


class Header(object):
    ApplicationData = None
    EphemeralPublicKey = None
    PublicKeyHash = None
    TransactionID = None

    __setattr__ = frozen(object.__setattr__)
