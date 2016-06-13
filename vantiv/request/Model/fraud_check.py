from ..schemas import Schema, fields
from . .utilities import frozen


class FraudCheckSchema(Schema):
    AuthenticationValue = fields.String()
    AuthenticationTransactionID = fields.String()
    CustomerIpAddress = fields.String()
    AuthenticatedByMerchant = fields.Bool()


class FraudCheck(object):
    __schema__ = FraudCheckSchema

    AuthenticationValue = None
    AuthenticationTransactionID = None
    CustomerIpAddress = None
    AuthenticatedByMerchant = None

    __setattr__ = frozen(object.__setattr__)
