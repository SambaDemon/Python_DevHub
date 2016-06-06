from . .utilities import frozen


class PrimaryContact(object):
    FirstName = None
    LastName = None
    Email = None
    Phone = None

    __setattr__ = frozen(object.__setattr__)
