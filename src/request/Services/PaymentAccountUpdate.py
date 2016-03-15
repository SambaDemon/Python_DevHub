from . .Request import Request
from . .Utilities import RemoveFromJson


class PaymentAccountUpdate (Request):

    Application = None
    Card = None
    Credentials = None
    PaymentAccount = None
    Reports = None
    Transaction = None

    def __init__(self):
        super(PaymentAccountUpdate, self).__init__("payment", "services", "paymentAccountUpdate", "POST")
        

    
    
    
    
    
    