from ..schemas import Schema, fields
from ..utilities import frozen


class UpdateDiscountSchema(Schema):
    DiscountCode = fields.String()
    Name = fields.String()
    Amount = fields.Decimal()
    StartDate = fields.Date()
    EndDate = fields.Date()


class UpdateDiscount(object):
    __schema__ = UpdateDiscountSchema

    DiscountCode = None
    Name = None
    Amount = None
    StartDate = None
    EndDate = None

    __setattr__ = frozen(object.__setattr__)
