from ..schemas import Schema, fields
from ..utils import FrozenMixin


class AdvancedFraudResultsSchema(Schema):
    DeviceReviewStatus = fields.String()
    DeviceReputationScore = fields.String()
    TriggeredRule = fields.String()


class AdvancedFraudResults(FrozenMixin):
    __schema__ = AdvancedFraudResultsSchema

    DeviceReviewStatus = None
    DeviceReputationScore = None
    TriggeredRule = None
