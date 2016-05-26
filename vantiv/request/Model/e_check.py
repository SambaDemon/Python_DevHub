from . .utilities import frozen


class ECheck(object):
    Enabled = None
    CompanyName = None
    BillingDescriptor = None

    __setattr__ = frozen(object.__setattr__)
