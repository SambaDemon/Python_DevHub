from . .utilities import frozen


class AdvancedFraudResults(object):
    DeviceReviewStatus = None
    DeviceReputationScore = None
    TriggeredRule = None

    __setattr__ = frozen(object.__setattr__)
