from . .Request import Request
from . .Utilities import RemoveFromJson


class CreateLegalEntity (Request):

    Address = None
    Credentials = None
    LegalEntity = None
    Principal = None
    PrincipalArray = None

    def __init__(self):
        super(CreateLegalEntity, self).__init__("boarding", "services", "createLegalEntity", "POST")
        

    
    
    
    
    