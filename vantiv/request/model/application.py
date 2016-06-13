from ..schemas import Schema, fields
from ..utils import FrozenMixin


class ApplicationSchema(Schema):
    ApplicationID = fields.String()


class Application(FrozenMixin):
    __schema__ = ApplicationSchema

    ApplicationID = None
