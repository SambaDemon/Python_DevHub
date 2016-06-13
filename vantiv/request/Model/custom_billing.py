from . .utilities import frozen


class CustomBilling(object):
    PhoneNumber = None
    Descriptor = None
    Url = None
    City = None

    __setattr__ = frozen(object.__setattr__)
