from . .Request import Request
from . .Utilities import RemoveFromJson


class Sale (Request):

    Address = None
    Application = None
    Credentials = None
    CustomBilling = None
    DemandDepositAccount = None
    PaymentAccount = None
    Reports = None
    Transaction = None

    def __init__(self):
        super(Sale, self).__init__("payment", "check", "sale", "POST")
        

    
    
    
    
    
    
    
    