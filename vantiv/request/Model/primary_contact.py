from ..schemas import Schema, fields
from ..utilities import frozen


class PrimaryContactSchema(Schema):
    FirstName = fields.String()
    LastName = fields.String()
    Email = fields.String()
    Phone = fields.String()


class PrimaryContact(object):
    __schema__ = PrimaryContactSchema

    FirstName = None
    LastName = None
    Email = None
    Phone = None

    __setattr__ = frozen(object.__setattr__)
