from marshmallow import Schema, fields
from . .utilities import frozen


class BmlSchema(Schema):
    MerchantID = fields.String()
    ProductType = fields.String()
    TermsAndConditions = fields.String()
    PreApprovalNumber = fields.String()
    VirtualAuthenticationKeyPresenceIndicator = fields.String()
    VirtualAuthenticationKeyData = fields.String()
    ItemCategoryCode = fields.String()


class Bml(object):
    __schema__ = BmlSchema

    MerchantID = None
    ProductType = None
    TermsAndConditions = None
    PreApprovalNumber = None
    VirtualAuthenticationKeyPresenceIndicator = None
    VirtualAuthenticationKeyData = None
    ItemCategoryCode = None

    __setattr__ = frozen(object.__setattr__)
