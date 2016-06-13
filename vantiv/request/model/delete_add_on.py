from ..schemas import Schema, fields
from ..utils import FrozenMixin


class DeleteAddOnSchema(Schema):
    AddOnCode = fields.String()


class DeleteAddOn(FrozenMixin):
    __schema__ = DeleteAddOnSchema

    AddOnCode = None
