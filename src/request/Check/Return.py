from . .Request import Request
from . .Utilities import RemoveFromJson

class Return (Request):
    Address = None
    Application = None
    Credentials = None
    CustomBilling = None
    DemandDepositAccount = None
    PaymentAccount = None
    Reports = None
    Transaction = None
    
    def __init__(self):
        super(Return, self).__init__("payment", "check", "return", "POST")
        