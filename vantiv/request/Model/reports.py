from marshmallow import Schema, fields

from ..utilities import frozen


class ReportSchema(Schema):
    ReportGroup = fields.String()
    Affiliate = fields.String()
    Campaign = fields.String()
    MerchantGroupingID = fields.String()


class Report(object):
    __schema__ = ReportSchema

    ReportGroup = None
    Affiliate = None
    Campaign = None
    MerchantGroupingID = None

    __setattr__ = frozen(object.__setattr__)
