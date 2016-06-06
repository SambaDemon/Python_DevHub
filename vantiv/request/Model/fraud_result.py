from . .utilities import frozen


class FraudResult(object):
    AvsResult = None
    CardValidationResult = None
    AuthenticationResult = None
    AdvancedAVSResult = None
    AdvancedFraudResults = None

    __setattr__ = frozen(object.__setattr__)
