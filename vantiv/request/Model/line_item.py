from . .utilities import frozen


class LineItem(object):
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

    __setattr__ = frozen(object.__setattr__)
