from . .utilities import frozen


class EnhancedData(object):
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

    __setattr__ = frozen(object.__setattr__)
