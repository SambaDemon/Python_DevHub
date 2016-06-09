from ..schemas import Schema, fields
from ..utilities import frozen


class CreateAddOnSchema(Schema):
    AddOnCode = fields.String()
    Name = fields.String()
    Amount = fields.String()
    StartDate = fields.Date()
    EndDate = fields.Date()


class CreateAddOn(object):
    __schema__ = CreateAddOnSchema

    AddOnCode = None
    Name = None
    Amount = None
    StartDate = None
    EndDate = None

    __setattr__ = frozen(object.__setattr__)
