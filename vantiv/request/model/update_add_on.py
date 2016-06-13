from ..schemas import Schema, fields
from . .utilities import frozen


class UpdateAddOnSchema(Schema):
    AddOnCode = fields.String()
    Name = fields.String()
    Amount = fields.Decimal()
    StartDate = fields.Date()
    EndDate = fields.Date()


class UpdateAddOn(object):
    __schema__ = UpdateAddOnSchema

    AddOnCode = None
    Name = None
    Amount = None
    StartDate = None
    EndDate = None

    __setattr__ = frozen(object.__setattr__)
