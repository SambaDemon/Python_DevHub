from . .Request import Request
from . .Utilities import RemoveFromJson

class Return (Request):
    Address = None
    Application = None
    Bml = None
    Card = None
    Credentials = None
    CustomBilling = None
    EnhancedData = None
    PayPal = None
    PaymentAccount = None
    Reports = None
    Terminal = None
    Transaction = None
    
    def __init__(self):
        super(Return, self).__init__("payment", "credit", "return", "POST")
        