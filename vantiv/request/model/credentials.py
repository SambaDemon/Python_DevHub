from ..schemas import Schema, fields
from ..utils import frozen


class CredentialsSchema(Schema):
    AcceptorID = fields.String()


class Credentials(object):
    __schema__ = CredentialsSchema

    AcceptorID = None

    __setattr__ = frozen(object.__setattr__)
