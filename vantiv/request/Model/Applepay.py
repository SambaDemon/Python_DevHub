from marshmallow import Schema, fields
from . .utilities import frozen


class ApplepaySchema(Schema):
    Data = fields.String()
    Header = fields.String()
    Signature = fields.String()
    Version = fields.String()


class Applepay(object):
    __schema__ = ApplepaySchema

    Data = None
    Header = None
    Signature = None
    Version = None

    __setattr__ = frozen(object.__setattr__)
