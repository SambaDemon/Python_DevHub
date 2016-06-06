from . .Request import Request
from .schemas import (CreditSchema, RedepositSchema, ReturnSchema,
                      SaleSchema, VerificationSchema, VoidSchema)


class Credit (Request):
    __schema__ = CreditSchema

    Application = None
    Credentials = None
    CustomBilling = None
    Reports = None
    Transaction = None

    def __init__(self):
        super(Credit, self).__init__("payment", "check", "credit", "POST")


class Redeposit (Request):
    __schema__ = RedepositSchema

    Application = None
    Credentials = None
    DemandDepositAccount = None
    PaymentAccount = None
    Reports = None
    Transaction = None

    def __init__(self):
        super(Redeposit, self).__init__("payment", "check", "redeposit", "POST")


class Return (Request):
    __schema__ = ReturnSchema

    Address = None
    Application = None
    Credentials = None
    CustomBilling = None
    DemandDepositAccount = None
    PaymentAccount = None
    Reports = None
    Transaction = None

    def __init__(self):
        super(Return, self).__init__("payment", "check", "return", "POST")


class Sale (Request):
    __schema__ = SaleSchema

    Address = None
    Application = None
    Credentials = None
    CustomBilling = None
    DemandDepositAccount = None
    PaymentAccount = None
    Reports = None
    Transaction = None

    def __init__(self):
        super(Sale, self).__init__("payment", "check", "sale", "POST")


class Verification (Request):
    __schema__ = VerificationSchema

    Address = None
    Application = None
    Credentials = None
    DemandDepositAccount = None
    PaymentAccount = None
    Reports = None
    Transaction = None

    def __init__(self):
        super(Verification, self).__init__("payment",
                                           "check",
                                           "verification",
                                           "POST")


class Void (Request):
    __schema__ = VoidSchema

    Application = None
    Credentials = None
    Reports = None
    Transaction = None

    def __init__(self):
        super(Void, self).__init__("payment", "check", "void", "POST")
