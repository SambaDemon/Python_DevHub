from . .utilities import frozen


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

    __setattr__ = frozen(object.__setattr__)
