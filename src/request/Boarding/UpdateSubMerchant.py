from . .Request import Request
from . .Utilities import RemoveFromJson


class UpdateSubMerchant (Request):

    Address = None
    Credentials = None
    ECheck = None
    Merchant = None
    PrimaryContact = None
    SubMerchantFunding = None

    def __init__(self):
        super(UpdateSubMerchant, self).__init__("boarding", "services", "updateSubMerchant", "POST")
        

    
    
    
    
    
    