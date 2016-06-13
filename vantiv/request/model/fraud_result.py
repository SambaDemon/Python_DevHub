from ..schemas import Schema, fields
from ..utilities import frozen


class FraudResultSchema(Schema):
    AvsResult = fields.String()
    CardValidationResult = fields.String()
    AuthenticationResult = fields.String()
    AdvancedAVSResult = fields.String()
    AdvancedFraudResults = fields.String()


class FraudResult(object):
    __schema__ = FraudResultSchema

    AvsResult = None
    CardValidationResult = None
    AuthenticationResult = None
    AdvancedAVSResult = None
    AdvancedFraudResults = None

    __setattr__ = frozen(object.__setattr__)
