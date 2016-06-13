from ..schemas import Schema, fields
from ..utils import frozen


class DeleteAddOnSchema(Schema):
    AddOnCode = fields.String()


class DeleteAddOn(object):
    __schema__ = DeleteAddOnSchema

    AddOnCode = None

    __setattr__ = frozen(object.__setattr__)
