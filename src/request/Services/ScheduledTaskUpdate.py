from . .Request import Request
from . .Utilities import RemoveFromJson

class ScheduledTaskUpdate (Request):
    Address = None
    Application = None
    Card = None
    Credentials = None
    PaymentAccount = None
    Reports = None
    ScheduledTask = None
    Transaction = None
    
    def __init__(self):
        super(ScheduledTaskUpdate, self).__init__("payment", "services", "scheduledTaskUpdate", "POST")
        