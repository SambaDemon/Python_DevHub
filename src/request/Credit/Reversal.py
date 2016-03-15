from . .Request import Request
from . .Utilities import RemoveFromJson


class Reversal (Request):

    Application = None
    Credentials = None
    PayPal = None
    Reports = None
    Transaction = None

    def __init__(self):
        super(Reversal, self).__init__("payment", "credit", "reversal", "POST")
        

    
    
    
    
    