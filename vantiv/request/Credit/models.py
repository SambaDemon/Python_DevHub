from ..request import Request
from .schemas import (AuthorizationSchema, AuthorizationCompletionSchema,
                      CaptureGivenAuthSchema, CreditSchema,
                      ForceSchema, ReturnSchema,
                      ReversalSchema, SaleSchema, VoidSchema)


class Authorization (Request):
    __schema__ = AuthorizationSchema

    Address = None
    AdvancedFraudChecks = None
    Applepay = None
    Application = None
    Bml = None
    Card = None
    CardholderAuthentication = None
    Credentials = None
    CustomBilling = None
    EnhancedData = None
    Identification = None
    PayPal = None
    PaymentAccount = None
    RecyclingRequest = None
    Reports = None
    ScheduledTask = None
    Terminal = None
    Transaction = None
    Visa = None
    Wallet = None

    def __init__(self):
        super(
            Authorization,
            self).__init__(
            "payment",
            "credit",
            "authorization",
            "POST")


class AuthorizationCompletion (Request):
    __schema__ = AuthorizationCompletionSchema

    Application = None
    Credentials = None
    EnhancedData = None
    PayPal = None
    Reports = None
    Transaction = None

    def __init__(self):
        super(
            AuthorizationCompletion,
            self).__init__(
            "payment",
            "credit",
            "authorizationCompletion",
            "POST")


class CaptureGivenAuth (Request):
    __schema__ = CaptureGivenAuthSchema

    Address = None
    Application = None
    Bml = None
    Card = None
    Credentials = None
    CustomBilling = None
    EnhancedData = None
    FraudResult = None
    PaymentAccount = None
    Reports = None
    Terminal = None
    Transaction = None
    Visa = None

    def __init__(self):
        super(
            CaptureGivenAuth,
            self).__init__(
            "payment",
            "credit",
            "captureGivenAuth",
            "POST")


class Credit (Request):
    __schema__ = CreditSchema

    Application = None
    Credentials = None
    CustomBilling = None
    EnhancedData = None
    PayPal = None
    Reports = None
    Terminal = None
    Transaction = None

    def __init__(self):
        super(Credit, self).__init__("payment", "credit", "credit", "POST")


class Force (Request):
    __schema__ = ForceSchema

    Address = None
    Application = None
    Card = None
    Credentials = None
    CustomBilling = None
    EnhancedData = None
    PaymentAccount = None
    Reports = None
    Terminal = None
    Transaction = None
    Visa = None

    def __init__(self):
        super(Force, self).__init__("payment", "credit", "force", "POST")


class Return (Request):
    __schema__ = ReturnSchema

    Address = None
    Application = None
    Bml = None
    Card = None
    Credentials = None
    CustomBilling = None
    EnhancedData = None
    PayPal = None
    PaymentAccount = None
    Reports = None
    Terminal = None
    Transaction = None

    def __init__(self):
        super(Return, self).__init__("payment", "credit", "return", "POST")


class Reversal (Request):
    __schema__ = ReversalSchema

    Application = None
    Credentials = None
    PayPal = None
    Reports = None
    Transaction = None

    def __init__(self):
        super(Reversal, self).__init__("payment", "credit", "reversal", "POST")


class Sale (Request):
    __schema__ = SaleSchema

    Address = None
    AdvancedFraudChecks = None
    Applepay = None
    Application = None
    Bml = None
    Card = None
    CardholderAuthentication = None
    Credentials = None
    CustomBilling = None
    EnhancedData = None
    FraudCheck = None
    Identification = None
    PayPal = None
    PaymentAccount = None
    RecyclingRequest = None
    Reports = None
    ScheduledTask = None
    Terminal = None
    Transaction = None
    Visa = None
    Wallet = None

    def __init__(self):
        super(Sale, self).__init__("payment", "credit", "sale", "POST")


class Void (Request):
    __schema__ = VoidSchema

    Application = None
    Credentials = None
    Reports = None
    Transaction = None

    def __init__(self):
        super(Void, self).__init__("payment", "credit", "void", "POST")
