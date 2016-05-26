from . .utilities import frozen


class PaymentAccount(object):
    PaymentAccountID = None

    __setattr__ = frozen(object.__setattr__)
