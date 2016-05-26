from . .utilities import frozen


class Card(object):
    CardNumber = None
    ExpirationMonth = None
    ExpirationYear = None
    CVV = None
    Track1Data = None
    Track2Data = None
    PaypageRegistrationID = None
    AccountNumber = None
    Type = None

    __setattr__ = frozen(object.__setattr__)
