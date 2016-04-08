from . .Request import Request
from . .Utilities import RemoveFromJson

class Void (Request):
    Application = None
    Credentials = None
    Reports = None
    Transaction = None
    
    def __init__(self):
        super(Void, self).__init__("payment", "credit", "void", "POST")
        