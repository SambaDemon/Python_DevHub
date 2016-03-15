import sys
from . .Utilities import Frozen

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
    

    

    
    
    __setattr__=Frozen(object.__setattr__)