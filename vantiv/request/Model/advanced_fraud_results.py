from ..schemas import Schema, fields
from ..utilities import frozen


class AdvancedFraudResultsSchema(Schema):
    DeviceReviewStatus = fields.String()
    DeviceReputationScore = fields.String()
    TriggeredRule = fields.String()


class AdvancedFraudResults(object):
    __schema__ = AdvancedFraudResultsSchema

    DeviceReviewStatus = None
    DeviceReputationScore = None
    TriggeredRule = None

    __setattr__ = frozen(object.__setattr__)
