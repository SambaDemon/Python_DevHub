from marshmallow import Schema, fields

from . .utilities import frozen


class CredentialsSchema(Schema):
    AcceptorID = fields.Integer()


class Credentials(object):
    __schema__ = CredentialsSchema

    AcceptorID = None

    __setattr__ = frozen(object.__setattr__)
