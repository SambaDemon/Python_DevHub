from . .Request import Request
from . .Utilities import RemoveFromJson

class FraudCheck (Request):
    Address = None
    AdvancedFraudChecks = None
    Application = None
    Credentials = None
    Reports = None
    ScheduledTask = None
    Transaction = None
    
    def __init__(self):
        super(FraudCheck, self).__init__("payment", "services", "fraudCheck", "POST")
        