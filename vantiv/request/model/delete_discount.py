from ..schemas import Schema, fields
from ..utils import FrozenMixin


class DeleteDiscountSchema(Schema):
    DiscountCode = fields.String()


class DeleteDiscount(FrozenMixin):
    __schema__ = DeleteDiscountSchema
    DiscountCode = None
