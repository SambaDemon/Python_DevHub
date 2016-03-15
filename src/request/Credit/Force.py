from . .Request import Request
from . .Utilities import RemoveFromJson


class Force (Request):

    Address = None
    Application = None
    Card = None
    Credentials = None
    CustomBilling = None
    EnhancedData = None
    PaymentAccount = None
    Reports = None
    Terminal = None
    Transaction = None
    Visa = None

    def __init__(self):
        super(Force, self).__init__("payment", "credit", "force", "POST")
        

    
    
    
    
    
    
    
    
    
    
    