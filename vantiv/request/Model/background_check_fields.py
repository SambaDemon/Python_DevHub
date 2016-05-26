import sys
from . .Utilities import Frozen

class BackgroundCheckFields(object):
    FirstName = None
    LastName = None
    SSN = None
    DateOfBirth = None
    DriversLicense = None
    DriversLicenseState = None
    Name = None
    Type = None
    TaxID = None
    

    

    
    
    __setattr__=Frozen(object.__setattr__)