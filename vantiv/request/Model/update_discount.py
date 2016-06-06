from . .utilities import frozen


class UpdateDiscount(object):
    DiscountCode = None
    Name = None
    Amount = None
    StartDate = None
    EndDate = None

    __setattr__ = frozen(object.__setattr__)
