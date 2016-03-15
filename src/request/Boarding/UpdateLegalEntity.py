from . .Request import Request
from . .Utilities import RemoveFromJson


class UpdateLegalEntity (Request):

    Address = None
    BackgroundCheckFields = None
    Credentials = None
    LegalEntity = None
    Principal = None
    PrincipalArray = None

    def __init__(self):
        super(UpdateLegalEntity, self).__init__("boarding", "services", "updateLegalEntity", "POST")
        

    
    
    
    
    
    