from ..schemas import Schema, fields
from ..utils import FrozenMixin


class AdvancedFraudChecksSchema(Schema):
    ThreatMetrixSessionID = fields.String()
    CustomAttribute1 = fields.String()
    CustomAttribute2 = fields.String()
    CustomAttribute3 = fields.String()
    CustomAttribute4 = fields.String()
    CustomAttribute5 = fields.String()


class AdvancedFraudChecks(FrozenMixin):
    __schema__ = AdvancedFraudChecksSchema

    ThreatMetrixSessionID = None
    CustomAttribute1 = None
    CustomAttribute2 = None
    CustomAttribute3 = None
    CustomAttribute4 = None
    CustomAttribute5 = None
