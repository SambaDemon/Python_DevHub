from . .utilities import frozen


class Bml(object):
    MerchantID = None
    ProductType = None
    TermsAndConditions = None
    PreApprovalNumber = None
    VirtualAuthenticationKeyPresenceIndicator = None
    VirtualAuthenticationKeyData = None
    ItemCategoryCode = None

    __setattr__ = frozen(object.__setattr__)
