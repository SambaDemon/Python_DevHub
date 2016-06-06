from . .utilities import frozen


class DeleteDiscount(object):
    DiscountCode = None

    __setattr__ = frozen(object.__setattr__)
