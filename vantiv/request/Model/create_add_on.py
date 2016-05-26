from . .utilities import frozen


class CreateAddOn(object):
    AddOnCode = None
    Name = None
    Amount = None
    StartDate = None
    EndDate = None

    __setattr__ = frozen(object.__setattr__)
