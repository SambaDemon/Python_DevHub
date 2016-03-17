from . .Request import Request
from . .Utilities import RemoveFromJson


class CreateSubMerchant (Request):

    Address = None
    Credentials = None
    ECheck = None
    Merchant = None
    PrimaryContact = None
    SubMerchantFunding = None

    def __init__(self, entityID):
        super(CreateSubMerchant, self).__init__("boarding", "services", "createSubMerchant", "POST")
        self.queryParams['entityID'] = entityID

    
    
    
    
    
    