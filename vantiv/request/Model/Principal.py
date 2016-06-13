from ..schemas import Schema, fields
from ..utilities import frozen
from ..Model.address import AddressSchema


class PrincipalSchema(Schema):
    Title = fields.String()
    FirstName = fields.String()
    LastName = fields.String()
    Email = fields.String()
    SSN = fields.String()
    ContactPhone = fields.String()
    DateOfBirth = fields.Date()
    DriversLicense = fields.String()
    DriversLicenseState = fields.String()
    Address = fields.Nested(AddressSchema)
    BackgroundCheckFields = fields.String()


class Principal(object):
    __schema__ = PrincipalSchema

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

    __setattr__ = frozen(object.__setattr__)
