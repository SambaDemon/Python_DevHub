from marshmallow import Schema, fields


class Authorization (Schema):
    Address = fields.Nested("Address")
    AdvancedFraudChecks = None
    Applepay = None
    Application = fields.Nested("Application")
    Bml = None
    Card = fields.Nested("Card")
    CardholderAuthentication = None
    Credentials = fields.Nested("Credentials")
    CustomBilling = None
    EnhancedData = None
    Identification = None
    PayPal = None
    PaymentAccount = None
    RecyclingRequest = None
    Reports = fields.Nested("Report")
    ScheduledTask = None
    Terminal = None
    Transaction = fields.Nested("Transaction")
    Visa = None
    Wallet = None


class AuthorizationCompletion (Schema):
    Application = fields.Nested("Application")
    Credentials = fields.Nested("Credentials")
    EnhancedData = None
    PayPal = None
    Reports = fields.Nested("Reports")
    Transaction = fields.Nested("Transaction")


class CaptureGivenAuth (Schema):
    Address = fields.Nested("Address")
    Application = fields.Nested("Application")
    Bml = None
    Card = fields.Nested("Card")
    Credentials = fields.Nested("Credentials")
    CustomBilling = None
    EnhancedData = None
    FraudResult = None
    PaymentAccount = None
    Reports = fields.Nested("Reports")
    Terminal = None
    Transaction = fields.Nested("Transaction")
    Visa = None


class Credit (Schema):
    Application = fields.Nested("Application")
    Credentials = fields.Nested("Credentials")
    CustomBilling = None
    EnhancedData = None
    PayPal = None
    Reports = None
    Terminal = None
    Transaction = fields.Nested("Transaction")


class Force (Schema):
    Address = fields.Nested("Address")
    Application = fields.Nested("Application")
    Card = fields.Nested("Card")
    Credentials = fields.Nested("Credentials")
    CustomBilling = None
    EnhancedData = None
    PaymentAccount = None
    Reports = fields.Nested("Repors")
    Terminal = None
    Transaction = fields.Nested("Transaction")
    Visa = None


class Return (Schema):
    Address = fields.Nested("Address")
    Application = fields.Nested("Application")
    Bml = None
    Card = fields.Nested("Card")
    Credentials = fields.Nested("Credentials")
    CustomBilling = None
    EnhancedData = None
    PayPal = None
    PaymentAccount = None
    Reports = fields.Nested("Reports")
    Terminal = fields.Nested("Terminal")
    Transaction = fields.Nested("Transaction")


class Reversal (Schema):
    Application = fields.Nested("Application")
    Credentials = fields.Nested("Credentials")
    PayPal = None
    Reports = fields.Nested("Reports")
    Transaction = fields.Nested("Transaction")


class Sale (Schema):
    Address = fields.Nested("Address")
    AdvancedFraudChecks = None
    Applepay = None
    Application = fields.Nested("Application")
    Bml = None
    Card = fields.Nested("Card")
    CardholderAuthentication = None
    Credentials = fields.Nested("Credentials")
    CustomBilling = None
    EnhancedData = None
    FraudCheck = None
    Identification = None
    PayPal = None
    PaymentAccount = None
    RecyclingRequest = None
    Reports = fields.Nested("Reports")
    ScheduledTask = None
    Terminal = None
    Transaction = fields.Nested("Transaction")
    Visa = None
    Wallet = None


class Void (Schema):
    Application = fields.Nested("Application")
    Credentials = fields.Nested("Credentials")
    Reports = fields.Nested("Reports")
    Transaction = fields.Transaction("Transaction")

