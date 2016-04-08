from . .Request import Request
from . .Utilities import RemoveFromJson

class Verification (Request):
    Address = None
    Application = None
    Credentials = None
    DemandDepositAccount = None
    PaymentAccount = None
    Reports = None
    Transaction = None
    
    def __init__(self):
        super(Verification, self).__init__("payment", "check", "verification", "POST")
        