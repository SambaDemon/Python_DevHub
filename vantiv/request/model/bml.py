from ..schemas import Schema, fields
from ..utils import FrozenMixin


class BmlSchema(Schema):
    MerchantID = fields.String()
    ProductType = fields.String()
    TermsAndConditions = fields.String()
    PreApprovalNumber = fields.String()
    VirtualAuthenticationKeyPresenceIndicator = fields.String()
    VirtualAuthenticationKeyData = fields.String()
    ItemCategoryCode = fields.String()


class Bml(FrozenMixin):
    __schema__ = BmlSchema

    MerchantID = None
    ProductType = None
    TermsAndConditions = None
    PreApprovalNumber = None
    VirtualAuthenticationKeyPresenceIndicator = None
    VirtualAuthenticationKeyData = None
    ItemCategoryCode = None
