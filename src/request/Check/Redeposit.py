from . .Request import Request
from . .Utilities import RemoveFromJson

class Redeposit (Request):
    Application = None
    Credentials = None
    DemandDepositAccount = None
    PaymentAccount = None
    Reports = None
    Transaction = None
    
    def __init__(self):
        super(Redeposit, self).__init__("payment", "check", "redeposit", "POST")
        