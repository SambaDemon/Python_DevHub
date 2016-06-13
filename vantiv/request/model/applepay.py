from ..schemas import Schema, fields
from ..utils import FrozenMixin


class ApplepaySchema(Schema):
    Data = fields.String()
    Header = fields.String()
    Signature = fields.String()
    Version = fields.String()


class Applepay(FrozenMixin):
    __schema__ = ApplepaySchema

    Data = None
    Header = None
    Signature = None
    Version = None
