from . .utilities import frozen


class Reports(object):
    ReportGroup = None
    Affiliate = None
    Campaign = None
    MerchantGroupingID = None

    __setattr__ = frozen(object.__setattr__)
