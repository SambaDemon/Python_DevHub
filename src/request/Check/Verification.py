from . .Request import Request
from . .Utilities import RemoveFromJson
from . .Model.Address import Address
from . .Model.Application import Application
from . .Model.Credentials import Credentials
from . .Model.DemandDepositAccount import DemandDepositAccount
from . .Model.PaymentAccount import PaymentAccount
from . .Model.Reports import Reports
from . .Model.Transaction import Transaction

class Verification (Request):

    Address = None
    Application = None
    Credentials = None
    DemandDepositAccount = None
    PaymentAccount = None
    Reports = None
    Transaction = None

    def __init__(self):
        super(Verification, self).__init__("payment", "check", "verification", "POST")
        

    
    
    
    
    
    
    