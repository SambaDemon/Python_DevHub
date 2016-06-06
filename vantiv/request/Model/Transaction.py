from . .utilities import frozen


class Transaction(object):
    CustomerID = None
    PartialCapture = None
    ReferenceNumber = None
    AuthorizationDate = None
    ApprovalNumber = None
    TransactionAmount = None
    TransactionID = None
    ConvenienceFeeAmount = None
    PartialApprovedFlag = None
    FraudFilterOverride = None
    SurchargeFee = None
    ActionReason = None
    Verify = None
    TransactionType = None
    OrderSource = None
    TaxType = None

    class OrderSourceEnum(object):
        def __init__(self, value):
            self.valuei = value

    OrderSourceEnum.ECOMMERCE = "ecommerce"
    OrderSourceEnum.INSTALLMENT = "installment"
    OrderSourceEnum.MAIL_ORDER = "mailorder"
    OrderSourceEnum.RECURRING = "recurring"
    OrderSourceEnum.RETAIL = "retail"
    OrderSourceEnum.TELEPHONE = "telephone"
    OrderSourceEnum.AUTH_3DS = "3dsAuthenticated"
    OrderSourceEnum.ATTEMPTED_3DS = "3dsAttempted"
    OrderSourceEnum.RECURRING_TEL = "recurringtel"
    OrderSourceEnum.ECHECK_PPD = "echeckppd"
    OrderSourceEnum.APPLEPAY = "applepay"

    class TaxTypeEnum(object):
        def __init__(self, value):
            self.value = value

    TaxTypeEnum.PAYMENT = "payment"
    TaxTypeEnum.FEE = "fee"

    __setattr__ = frozen(object.__setattr__)
