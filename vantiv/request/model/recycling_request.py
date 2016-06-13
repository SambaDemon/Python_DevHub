from ..schemas import Schema, fields
from ..utils import FrozenMixin


class RecyclingRequestSchema(Schema):
    RecycleID = fields.String()
    RecycleBy = fields.String()


class RecyclingRequest(FrozenMixin):
    __schema__ = RecyclingRequestSchema

    RecycleID = None
    RecycleBy = None
