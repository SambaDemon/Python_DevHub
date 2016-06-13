from ..schemas import Schema, fields
from ..utilities import frozen


class ECheckSchema(Schema):
    Enabled = fields.Bool()
    CompanyName = fields.String()
    BillingDescriptor = fields.String()


class ECheck(object):
    __schema__ = ECheckSchema

    Enabled = None
    CompanyName = None
    BillingDescriptor = None

    __setattr__ = frozen(object.__setattr__)
