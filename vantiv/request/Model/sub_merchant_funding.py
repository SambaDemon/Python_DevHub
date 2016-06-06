from . .utilities import frozen


class SubMerchantFunding(object):
    Enabled = None
    FeeProfile = None
    FundingSubmerchantID = None

    __setattr__ = frozen(object.__setattr__)
