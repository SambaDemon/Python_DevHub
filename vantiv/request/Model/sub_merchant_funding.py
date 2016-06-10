from ..schemas import Schema, fields
from ..utilities import frozen


class SubMerchantFundingSchema(Schema):
    Enabled = fields.Bool()
    FeeProfile = fields.String()
    FundingSubmerchantID = fields.String()


class SubMerchantFunding(object):
    __schema__ = SubMerchantFundingSchema

    Enabled = None
    FeeProfile = None
    FundingSubmerchantID = None

    __setattr__ = frozen(object.__setattr__)
