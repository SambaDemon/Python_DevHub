from ..schemas import Schema, fields
from ..utils import FrozenMixin


class UpdateDiscountSchema(Schema):
    DiscountCode = fields.String()
    Name = fields.String()
    Amount = fields.Decimal()
    StartDate = fields.Date()
    EndDate = fields.Date()


class UpdateDiscount(FrozenMixin):
    __schema__ = UpdateDiscountSchema

    DiscountCode = None
    Name = None
    Amount = None
    StartDate = None
    EndDate = None
