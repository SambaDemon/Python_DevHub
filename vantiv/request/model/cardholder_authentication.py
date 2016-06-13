from ..schemas import Schema, fields
from ..utils import FrozenMixin


class CardholderAuthenticationSchema(Schema):
    AuthenticationValue = fields.String()
    AuthenticationTransactionID = fields.String()
    CustomerIpAddress = fields.String()
    AuthenticatedByMerchant = fields.String()


class CardholderAuthentication(FrozenMixin):
    __schema__ = CardholderAuthenticationSchema

    AuthenticationValue = None
    AuthenticationTransactionID = None
    CustomerIpAddress = None
    AuthenticatedByMerchant = None
