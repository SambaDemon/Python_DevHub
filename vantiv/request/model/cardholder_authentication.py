from ..schemas import Schema, fields
from ..utils import frozen


class CardholderAuthenticationSchema(Schema):
    AuthenticationValue = fields.String()
    AuthenticationTransactionID = fields.String()
    CustomerIpAddress = fields.String()
    AuthenticatedByMerchant = fields.String()


class CardholderAuthentication(object):
    __schema__ = CardholderAuthenticationSchema

    AuthenticationValue = None
    AuthenticationTransactionID = None
    CustomerIpAddress = None
    AuthenticatedByMerchant = None

    __setattr__ = frozen(object.__setattr__)
