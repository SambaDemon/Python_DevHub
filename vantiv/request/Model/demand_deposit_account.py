from . .utilities import frozen


class DemandDepositAccount(object):
    DDAAccountType = None
    AccountNumber = None
    RoutingNumber = None
    CheckNumber = None
    CCDPaymentInformation = None

    __setattr__ = frozen(object.__setattr__)
