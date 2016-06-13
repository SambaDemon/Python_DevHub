from ..schemas import Schema, fields
from ..utils import FrozenMixin


class VisaSchema(Schema):
    DebtRepayment = fields.String()


class Visa(FrozenMixin):
    __schema__ = VisaSchema

    DebtRepayment = None
