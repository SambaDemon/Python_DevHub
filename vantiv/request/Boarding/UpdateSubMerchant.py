from . .Request import Request
from . .Utilities import RemoveFromJson


class UpdateSubMerchant (Request):

    Address = None
    Credentials = None
    ECheck = None
    Merchant = None
    PrimaryContact = None
    SubMerchantFunding = None

    def __init__(self, entityID, subMerchantID):
        super(UpdateSubMerchant, self).__init__("boarding", "services", "updateSubMerchant", "PUT")
        self.queryParams['entityID'] = entityID
        self.queryParams['subMerchantID'] = subMerchantID

    
    
    
    
    
    