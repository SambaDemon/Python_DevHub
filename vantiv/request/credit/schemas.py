from ..schemas import Schema, fields

from ..model.report import ReportSchema
from ..model.address import AddressSchema
from ..model.credentials import CredentialsSchema
from ..model.application import ApplicationSchema
from ..model.card import CardSchema
from ..model.transaction import TransactionSchema
from ..model.terminal import TerminalSchema


class AuthorizationSchema (Schema):
    Address = fields.Nested(AddressSchema)
    AdvancedFraudChecks = None
    Applepay = None
    Application = fields.Nested(ApplicationSchema)
    Bml = None
    Card = fields.Nested(CardSchema)
    CardholderAuthentication = None
    Credentials = fields.Nested(CredentialsSchema)
    CustomBilling = None
    EnhancedData = None
    Identification = None
    PayPal = None
    PaymentAccount = None
    RecyclingRequest = None
    Reports = fields.Nested(ReportSchema)
    ScheduledTask = None
    Terminal = None
    Transaction = fields.Nested(TransactionSchema)
    Visa = None
    Wallet = None


class AuthorizationCompletionSchema (Schema):
    Application = fields.Nested(ApplicationSchema)
    Credentials = fields.Nested(CredentialsSchema)
    EnhancedData = None
    PayPal = None
    Reports = fields.Nested(ReportSchema)
    Transaction = fields.Nested(TransactionSchema)


class CaptureGivenAuthSchema (Schema):
    Address = fields.Nested(AddressSchema)
    Application = fields.Nested(ApplicationSchema)
    Bml = None
    Card = fields.Nested(CardSchema)
    Credentials = fields.Nested(CredentialsSchema)
    CustomBilling = None
    EnhancedData = None
    FraudResult = None
    PaymentAccount = None
    Reports = fields.Nested(ReportSchema)
    Terminal = None
    Transaction = fields.Nested(TransactionSchema)
    Visa = None


class CreditSchema (Schema):
    Application = fields.Nested(ApplicationSchema)
    Credentials = fields.Nested(CredentialsSchema)
    CustomBilling = None
    EnhancedData = None
    PayPal = None
    Reports = fields.Nested(ReportSchema)
    Terminal = None
    Transaction = fields.Nested(TransactionSchema)


class ForceSchema (Schema):
    Address = fields.Nested(AddressSchema)
    Application = fields.Nested(ApplicationSchema)
    Card = fields.Nested(CardSchema)
    Credentials = fields.Nested(CredentialsSchema)
    CustomBilling = None
    EnhancedData = None
    PaymentAccount = None
    Reports = fields.Nested(ReportSchema)
    Terminal = None
    Transaction = fields.Nested(TransactionSchema)
    Visa = None


class ReturnSchema (Schema):
    Address = fields.Nested(AddressSchema)
    Application = fields.Nested(ApplicationSchema)
    Bml = None
    Card = fields.Nested(CardSchema)
    Credentials = fields.Nested(CredentialsSchema)
    CustomBilling = None
    EnhancedData = None
    PayPal = None
    PaymentAccount = None
    Reports = fields.Nested(ReportSchema)
    Terminal = fields.Nested(TerminalSchema)
    Transaction = fields.Nested(TransactionSchema)


class ReversalSchema (Schema):
    Application = fields.Nested(ApplicationSchema)
    Credentials = fields.Nested(CredentialsSchema)
    PayPal = None
    Reports = fields.Nested(ReportSchema)
    Transaction = fields.Nested(TransactionSchema)


class SaleSchema (Schema):
    Address = fields.Nested(AddressSchema)
    AdvancedFraudChecks = None
    Applepay = None
    Application = fields.Nested(ApplicationSchema)
    Bml = None
    Card = fields.Nested(CardSchema)
    CardholderAuthentication = None
    Credentials = fields.Nested(CredentialsSchema)
    CustomBilling = None
    EnhancedData = None
    FraudCheck = None
    Identification = None
    PayPal = None
    PaymentAccount = None
    RecyclingRequest = None
    Reports = fields.Nested(ReportSchema)
    ScheduledTask = None
    Terminal = None
    Transaction = fields.Nested(TransactionSchema)
    Visa = None
    Wallet = None


class VoidSchema (Schema):
    Application = fields.Nested(ApplicationSchema)
    Credentials = fields.Nested(CredentialsSchema)
    Reports = fields.Nested(ReportSchema)
    Transaction = fields.Nested(TransactionSchema)
