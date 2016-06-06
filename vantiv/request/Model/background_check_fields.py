from marshmallow import Schema, fields
from . .utilities import frozen


class BackgroundCheckFieldsSchema(Schema):
    FirstName = fields.String()
    LastName = fields.String()
    SSN = fields.String()
    DateOfBirth = fields.Date()
    DriversLicense = fields.String()
    DriversLicenseState = fields.String()
    Name = fields.String()
    Type = fields.String()
    TaxID = fields.String()


class BackgroundCheckFields(object):
    __schema__ = BackgroundCheckFieldsSchema
    __setattr__ = frozen(object.__setattr__)

    FirstName = None
    LastName = None
    SSN = None
    DateOfBirth = None
    DriversLicense = None
    DriversLicenseState = None
    Name = None
    Type = None
    TaxID = None
