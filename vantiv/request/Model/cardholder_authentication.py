from . .utilities import frozen


class CardholderAuthentication(object):
    AuthenticationValue = None
    AuthenticationTransactionID = None
    CustomerIpAddress = None
    AuthenticatedByMerchant = None

    __setattr__ = frozen(object.__setattr__)
