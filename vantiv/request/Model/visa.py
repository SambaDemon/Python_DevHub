from ..schemas import Schema, fields
from ..utilities import frozen


class VisaSchema(Schema):
    DebtRepayment = fields.String()


class Visa(object):
    __schema__ = VisaSchema

    DebtRepayment = None

    __setattr__ = frozen(object.__setattr__)
