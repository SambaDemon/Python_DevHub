from ..utils import FrozenMixin
from ..schemas import Schema, fields


class PaymentAccountSchema(Schema):
    PaymentAccountID = fields.Integer(as_string=True)


class PaymentAccount(FrozenMixin):
    __schema__ = PaymentAccountSchema

    PaymentAccountID = None
