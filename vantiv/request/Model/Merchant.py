import sys
from . .Utilities import Frozen

class Merchant(object):
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
    

    

    
    
    __setattr__=Frozen(object.__setattr__)