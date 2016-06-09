from marshmallow import Schema, fields
from . .utilities import frozen


class ApplicationSchema(Schema):
    ApplicationID = fields.Integer()


class Application(object):
    __schema__ = ApplicationSchema

    ApplicationID = None

    __setattr__ = frozen(object.__setattr__)
