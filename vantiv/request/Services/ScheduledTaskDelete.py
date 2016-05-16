from . .Request import Request
from . .Utilities import RemoveFromJson

class ScheduledTaskDelete (Request):
    Application = None
    Credentials = None
    Reports = None
    ScheduledTask = None
    Transaction = None
    
    def __init__(self):
        super(ScheduledTaskDelete, self).__init__("payment", "services", "scheduledTaskDelete", "POST")
        