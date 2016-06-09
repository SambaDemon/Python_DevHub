from . .utilities import frozen


class Visa(object):
    DebtRepayment = None

    __setattr__ = frozen(object.__setattr__)
