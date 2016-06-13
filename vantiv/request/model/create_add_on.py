from ..schemas import Schema, fields
from ..utils import FrozenMixin


class CreateAddOnSchema(Schema):
    AddOnCode = fields.String()
    Name = fields.String()
    Amount = fields.String()
    StartDate = fields.Date()
    EndDate = fields.Date()


class CreateAddOn(FrozenMixin):
    __schema__ = CreateAddOnSchema

    AddOnCode = None
    Name = None
    Amount = None
    StartDate = None
    EndDate = None
