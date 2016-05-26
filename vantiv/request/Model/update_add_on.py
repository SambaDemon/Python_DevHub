from . .utilities import frozen


class UpdateAddOn(object):
    AddOnCode = None
    Name = None
    Amount = None
    StartDate = None
    EndDate = None

    __setattr__ = frozen(object.__setattr__)
