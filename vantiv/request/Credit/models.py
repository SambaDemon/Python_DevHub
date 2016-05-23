from . .Request import Request
from . .Utilities import RemoveFromJson


class Authorization (Request):
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
    Application = None
    Credentials = None
    PayPal = None
    Reports = None
    Transaction = None

    def __init__(self):
        super(Reversal, self).__init__("payment", "credit", "reversal", "POST")


class Sale (Request):
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
    Application = None
    Credentials = None
    Reports = None
    Transaction = None

    def __init__(self):
        super(Void, self).__init__("payment", "credit", "void", "POST")
