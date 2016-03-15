import sys
from . .Utilities import Frozen

class Principal(object):
    Title = None
    FirstName = None
    LastName = None
    Email = None
    SSN = None
    ContactPhone = None
    DateOfBirth = None
    DriversLicense = None
    DriversLicenseState = None
    Address = None
    BackgroundCheckFields = None
    

    

    
    
    __setattr__=Frozen(object.__setattr__)