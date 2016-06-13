from ..schemas import Schema, fields
from ..utils import FrozenMixin


class CustomBillingSchema(Schema):
    PhoneNumber = fields.String()
    Descriptor = fields.String()
    Url = fields.String()
    City = fields.String()


class CustomBilling(FrozenMixin):
    __schema__ = CustomBillingSchema

    PhoneNumber = None
    Descriptor = None
    Url = None
    City = None
