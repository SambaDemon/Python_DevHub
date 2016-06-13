from ..schemas import Schema, fields
from ..utils import frozen


class CreateDiscountSchema(Schema):
    DiscountCode = fields.String()
    Name = fields.String()
    Amount = fields.String()
    StartDate = fields.Date()
    EndDate = fields.Date()


class CreateDiscount(object):
    __schema__ = CreateDiscountSchema

    DiscountCode = None
    Name = None
    Amount = None
    StartDate = None
    EndDate = None

    __setattr__ = frozen(object.__setattr__)
