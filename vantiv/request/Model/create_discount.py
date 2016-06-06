from . .utilities import frozen


class CreateDiscount(object):
    DiscountCode = None
    Name = None
    Amount = None
    StartDate = None
    EndDate = None

    __setattr__ = frozen(object.__setattr__)
