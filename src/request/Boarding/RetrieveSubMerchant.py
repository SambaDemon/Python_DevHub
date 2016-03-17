from . .Request import Request
from . .Utilities import RemoveFromJson


class RetrieveSubMerchant (Request):

    

    def __init__(self, entityID, subMerchantID):
        super(RetrieveSubMerchant, self).__init__("boarding", "services", "retrieveSubMerchant", "GET")
        self.queryParams['entityID'] = entityID
        self.queryParams['subMerchantID'] = subMerchantID

    