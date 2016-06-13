from ..schemas import Schema, fields
from ..utilities import frozen


class MerchantSchema(Schema):
    Name = fields.String()
    AmexMid = fields.String()
    DiscoverConveyedMid = fields.String()
    URL = fields.String()
    CustomerServiceNumber = fields.String()
    HardCodedBillingDescriptor = fields.String()
    MaxTransactionAmount = fields.String()
    PurchaseCurrency = fields.String()
    CategoryCode = fields.String()
    BankRoutingNumber = fields.String()
    BankAccountNumber = fields.String()
    PSPMerchantID = fields.String()
    Disable = fields.String()
    CreateCredentials = fields.String()
    SettlementCurrency = fields.String()
    FraudEnabled = fields.String()


class Merchant(object):
    __schema__ = MerchantSchema()

    Name = None
    AmexMid = None
    DiscoverConveyedMid = None
    URL = None
    CustomerServiceNumber = None
    HardCodedBillingDescriptor = None
    MaxTransactionAmount = None
    PurchaseCurrency = None
    CategoryCode = None
    BankRoutingNumber = None
    BankAccountNumber = None
    PSPMerchantID = None
    Disable = None
    CreateCredentials = None
    SettlementCurrency = None
    FraudEnabled = None

    __setattr__ = frozen(object.__setattr__)
