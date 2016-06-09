from . .utilities import frozen


class Wallet(object):
    WalletSourceType = None
    WalletSourceTypeID = None

    __setattr__ = frozen(object.__setattr__)
