from ..schemas import Schema, fields
from ..utils import FrozenMixin


class FraudResultSchema(Schema):
    AvsResult = fields.String()
    CardValidationResult = fields.String()
    AuthenticationResult = fields.String()
    AdvancedAVSResult = fields.String()
    AdvancedFraudResults = fields.String()


class FraudResult(FrozenMixin):
    __schema__ = FraudResultSchema

    AvsResult = None
    CardValidationResult = None
    AuthenticationResult = None
    AdvancedAVSResult = None
    AdvancedFraudResults = None
