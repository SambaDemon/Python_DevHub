from ..schemas import Schema, fields
from ..utilities import frozen


class RecyclingRequestSchema(Schema):
    RecycleID = fields.String()
    RecycleBy = fields.String()


class RecyclingRequest(object):
    __schema__ = RecyclingRequestSchema

    RecycleID = None
    RecycleBy = None

    __setattr__ = frozen(object.__setattr__)
