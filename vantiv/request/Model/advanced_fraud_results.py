from . .utilities import frozen
from marshmallow import Schema, fields


class AdvancedFraudResultsSchema(Schema):
    DeviceReviewStatus = None
    DeviceReputationScore = None
    TriggeredRule = None


class AdvancedFraudResults(object):
    __schema__ = AdvancedFraudResultsSchema

    DeviceReviewStatus = None
    DeviceReputationScore = None
    TriggeredRule = None

    __setattr__ = frozen(object.__setattr__)
