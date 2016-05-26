from . .utilities import frozen


class AdvancedFraudChecks(object):
    ThreatMetrixSessionID = None
    CustomAttribute1 = None
    CustomAttribute2 = None
    CustomAttribute3 = None
    CustomAttribute4 = None
    CustomAttribute5 = None

    __setattr__ = frozen(object.__setattr__)
