from . .Request import Request
from . .Utilities import RemoveFromJson

class Credit (Request):
    Application = None
    Credentials = None
    CustomBilling = None
    Reports = None
    Transaction = None
    
    def __init__(self):
        super(Credit, self).__init__("payment", "check", "credit", "POST")
        