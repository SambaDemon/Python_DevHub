from . .Request import Request
from . .Utilities import RemoveFromJson

class UpdatePlan (Request):
    Application = None
    Credentials = None
    Reports = None
    ScheduledTask = None
    Transaction = None
    
    def __init__(self):
        super(UpdatePlan, self).__init__("payment", "services", "updatePlan", "POST")
        