from . .utilities import frozen


class PayPal(object):
    PayerID = None
    Token = None
    TransactionID = None
    PayPalOrderComplete = None
    PayPalNotes = None

    __setattr__ = frozen(object.__setattr__)
