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

    class DeliveryTypeEnum(object):
        def __init__(self, value):
            self.value = value

    DeliveryTypeEnum.CNC = "CNC"
    DeliveryTypeEnum.DIG = "DIG"
    DeliveryTypeEnum.PHY = "PHY"
    DeliveryTypeEnum.SVC = "SVC"
    DeliveryTypeEnum.TBD = "TBD"
    __setattr__ = frozen(object.__setattr__)
