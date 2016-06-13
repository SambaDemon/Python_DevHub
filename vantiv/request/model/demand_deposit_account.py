from ..schemas import Schema, fields
from ..utils import FrozenMixin


class DemandDepositAccountSchema(Schema):
    DDAAccountType = fields.String()
    AccountNumber = fields.String()
    RoutingNumber = fields.String()
    CheckNumber = fields.String()
    CCDPaymentInformation = fields.String()


class DemandDepositAccount(FrozenMixin):
    __schema__ = DemandDepositAccountSchema

    DDAAccountType = None
    AccountNumber = None
    RoutingNumber = None
    CheckNumber = None
    CCDPaymentInformation = None
