from marshmallow import Schema, fields

from . .utilities import frozen


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
