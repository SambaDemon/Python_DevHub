from ..schemas import Schema, fields
from ..utils import FrozenMixin


class ReportSchema(Schema):
    ReportGroup = fields.String()
    Affiliate = fields.String()
    Campaign = fields.String()
    MerchantGroupingID = fields.String()


class Report(FrozenMixin):
    __schema__ = ReportSchema

    ReportGroup = None
    Affiliate = None
    Campaign = None
    MerchantGroupingID = None
