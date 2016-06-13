from ..schemas import Schema, fields
from ..utils import FrozenMixin


class FraudCheckSchema(Schema):
    AuthenticationValue = fields.String()
    AuthenticationTransactionID = fields.String()
    CustomerIpAddress = fields.String()
    AuthenticatedByMerchant = fields.Bool()


class FraudCheck(FrozenMixin):
    __schema__ = FraudCheckSchema

    AuthenticationValue = None
    AuthenticationTransactionID = None
    CustomerIpAddress = None
    AuthenticatedByMerchant = None
