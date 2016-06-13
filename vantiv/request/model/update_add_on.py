from ..schemas import Schema, fields
from . .utils import FrozenMixin


class UpdateAddOnSchema(Schema):
    AddOnCode = fields.String()
    Name = fields.String()
    Amount = fields.Decimal()
    StartDate = fields.Date()
    EndDate = fields.Date()


class UpdateAddOn(FrozenMixin):
    __schema__ = UpdateAddOnSchema

    AddOnCode = None
    Name = None
    Amount = None
    StartDate = None
    EndDate = None
