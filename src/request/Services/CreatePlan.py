from . .Request import Request
from . .Utilities import RemoveFromJson


class CreatePlan (Request):

    Application = None
    Credentials = None
    Reports = None
    ScheduledTask = None
    Transaction = None

    def __init__(self):
        super(CreatePlan, self).__init__("payment", "services", "createPlan", "POST")
        

    
    
    
    
    