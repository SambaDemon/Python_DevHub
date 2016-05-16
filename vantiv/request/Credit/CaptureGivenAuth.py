from . .Request import Request
from . .Utilities import RemoveFromJson

class CaptureGivenAuth (Request):
    Address = None
    Application = None
    Bml = None
    Card = None
    Credentials = None
    CustomBilling = None
    EnhancedData = None
    FraudResult = None
    PaymentAccount = None
    Reports = None
    Terminal = None
    Transaction = None
    Visa = None
    
    def __init__(self):
        super(CaptureGivenAuth, self).__init__("payment", "credit", "captureGivenAuth", "POST")
        