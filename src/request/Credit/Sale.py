from . .Request import Request
from . .Utilities import RemoveFromJson


class Sale (Request):

    Address = None
    AdvancedFraudChecks = None
    Applepay = None
    Application = None
    Bml = None
    Card = None
    CardholderAuthentication = None
    Credentials = None
    CustomBilling = None
    EnhancedData = None
    FraudCheck = None
    Identification = None
    PayPal = None
    PaymentAccount = None
    RecyclingRequest = None
    Reports = None
    ScheduledTask = None
    Terminal = None
    Transaction = None
    Visa = None
    Wallet = None

    def __init__(self):
        super(Sale, self).__init__("payment", "credit", "sale", "POST")
        

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    