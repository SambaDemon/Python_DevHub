from ..schemas import Schema, fields
from ..utils import frozen


class CustomBillingSchema(Schema):
    PhoneNumber = fields.String()
    Descriptor = fields.String()
    Url = fields.String()
    City = fields.String()


class CustomBilling(object):
    __schema__ = CustomBillingSchema

    PhoneNumber = None
    Descriptor = None
    Url = None
    City = None

    __setattr__ = frozen(object.__setattr__)
