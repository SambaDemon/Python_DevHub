from . .Request import Request
from . .Utilities import RemoveFromJson

class AuthorizationCompletion (Request):
    Application = None
    Credentials = None
    EnhancedData = None
    PayPal = None
    Reports = None
    Transaction = None
    
    def __init__(self):
        super(AuthorizationCompletion, self).__init__("payment", "credit", "authorizationCompletion", "POST")
        