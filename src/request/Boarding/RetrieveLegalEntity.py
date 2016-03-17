from . .Request import Request
from . .Utilities import RemoveFromJson


class RetrieveLegalEntity (Request):

    

    def __init__(self, entityID):
        super(RetrieveLegalEntity, self).__init__("boarding", "services", "retrieveLegalEntity", "GET")
        self.queryParams['entityID'] = entityID

    