from . .Request import Request
from . .Utilities import RemoveFromJson


class PaymentAccountCreate (Request):

    Applepay = None
    Application = None
    Card = None
    Credentials = None
    DemandDepositAccount = None
    Reports = None
    Transaction = None

    def __init__(self):
        super(PaymentAccountCreate, self).__init__("payment", "services", "paymentAccountCreate", "POST")
        

    
    
    
    
    
    
    