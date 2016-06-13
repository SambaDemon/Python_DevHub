from ..schemas import Schema, fields
from ..utils import FrozenMixin


class EnhancedDataSchema(Schema):
    PurchaseOrder = fields.String()
    TaxAmount = fields.Decimal()
    TaxExempt = fields.Decimal()
    DiscountAmount = fields.Decimal()
    FreightAmount = fields.Decimal()
    DutyAmount = fields.String()
    ShipFromPostalCode = fields.String()
    DestinationPostalCode = fields.String()
    DestinationCountryCode = fields.String()
    InvoiceReferenceNumber = fields.String()
    OrderDate = fields.Date()
    DetailTaxArray = fields.String()
    DetailTax = fields.String()
    LineItemArray = fields.String()
    LineItem = fields.String()
    DeliveryType = fields.String()


class EnhancedData(FrozenMixin):
    __schema__ = EnhancedDataSchema

    PurchaseOrder = None
    TaxAmount = None
    TaxExempt = None
    DiscountAmount = None
    FreightAmount = None
    DutyAmount = None
    ShipFromPostalCode = None
    DestinationPostalCode = None
    DestinationCountryCode = None
    InvoiceReferenceNumber = None
    OrderDate = None
    DetailTaxArray = None
    DetailTax = None
    LineItemArray = None
    LineItem = None
    DeliveryType = None
