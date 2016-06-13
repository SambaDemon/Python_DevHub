from ..schemas import Schema, fields
from ..utils import FrozenMixin


class LineItemSchema(Schema):
    ItemSequenceNumber = fields.String()
    ItemDescription = fields.String()
    ProductCode = fields.String()
    LineItemCount = fields.String()
    UnitOfMeasure = fields.String()
    TaxAmount = fields.Decimal()
    LineItemTotalAmount = fields.Decimal()
    LineItemTotalWithTax = fields.Decimal()
    LineItemDiscountAmount = fields.Decimal()
    ItemCommodityCode = fields.String()
    UnitCost = fields.Decimal()
    DetailTaxArray = fields.String()
    DetailTax = fields.String()


class LineItem(FrozenMixin):
    __schema__ = LineItemSchema

    ItemSequenceNumber = None
    ItemDescription = None
    ProductCode = None
    LineItemCount = None
    UnitOfMeasure = None
    TaxAmount = None
    LineItemTotalAmount = None
    LineItemTotalWithTax = None
    LineItemDiscountAmount = None
    ItemCommodityCode = None
    UnitCost = None
    DetailTaxArray = None
    DetailTax = None
