from ..schemas import Schema, fields
from ..utils import FrozenMixin


class CredentialsSchema(Schema):
    AcceptorID = fields.String()


class Credentials(FrozenMixin):
    __schema__ = CredentialsSchema

    AcceptorID = None
