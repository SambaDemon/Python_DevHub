from ..schemas import Schema, fields
from ..utils import FrozenMixin


class CreateDiscountSchema(Schema):
    DiscountCode = fields.String()
    Name = fields.String()
    Amount = fields.String()
    StartDate = fields.Date()
    EndDate = fields.Date()


class CreateDiscount(FrozenMixin):
    __schema__ = CreateDiscountSchema

    DiscountCode = None
    Name = None
    Amount = None
    StartDate = None
    EndDate = None
