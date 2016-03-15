from . .Request import Request
from . .Utilities import RemoveFromJson


class TransactionQuery (Request):

    Application = None
    Card = None
    Credentials = None
    Reports = None
    Transaction = None

    def __init__(self):
        super(TransactionQuery, self).__init__("payment", "services", "transactionQuery", "POST")
        

    
    
    
    
    