from ..schemas import Schema, fields
from ..utilities import frozen


class AdvancedFraudChecksSchema(Schema):
    ThreatMetrixSessionID = fields.String()
    CustomAttribute1 = fields.String()
    CustomAttribute2 = fields.String()
    CustomAttribute3 = fields.String()
    CustomAttribute4 = fields.String()
    CustomAttribute5 = fields.String()


class AdvancedFraudChecks(object):
    __schema__ = AdvancedFraudChecksSchema

    ThreatMetrixSessionID = None
    CustomAttribute1 = None
    CustomAttribute2 = None
    CustomAttribute3 = None
    CustomAttribute4 = None
    CustomAttribute5 = None

    __setattr__ = frozen(object.__setattr__)
