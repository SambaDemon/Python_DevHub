from marshmallow import Schema, fields

from ..utilities import frozen


class ReportsSchema(Schema):
    ReportGroup = fields.String()
    Affiliate = fields.String()
    Campaign = fields.String()
    MerchantGroupingID = fields.String()


class Reports(object):
    __schema__ = ReportsSchema

    ReportGroup = None
    Affiliate = None
    Campaign = None
    MerchantGroupingID = None

    __setattr__ = frozen(object.__setattr__)
