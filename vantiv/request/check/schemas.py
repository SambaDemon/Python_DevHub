from ..schemas import Schema, fields

from ..model.application import ApplicationSchema
from ..model.credentials import CredentialsSchema
from ..model.report import ReportSchema
from ..model.transaction import TransactionSchema
from ..model.address import AddressSchema


class CreditSchema (Schema):
    Application = fields.Nested(ApplicationSchema)
    Credentials = fields.Nested(CredentialsSchema)
    CustomBilling = None
    Reports = fields.Nested(ReportSchema)
    Transaction = fields.Nested(TransactionSchema)


class RedepositSchema (Schema):
    Application = fields.Nested(ApplicationSchema)
    Credentials = fields.Nested(CredentialsSchema)
    DemandDepositAccount = None
    PaymentAccount = None
    Reports = fields.Nested(ReportSchema)
    Transaction = fields.Nested(TransactionSchema)


class ReturnSchema (Schema):
    Address = fields.Nested(AddressSchema)
    Application = fields.Nested(ApplicationSchema)
    Credentials = fields.Nested(CredentialsSchema)
    CustomBilling = None
    DemandDepositAccount = None
    PaymentAccount = None
    Reports = fields.Nested(ReportSchema)
    Transaction = fields.Nested(TransactionSchema)


class SaleSchema (Schema):
    Address = fields.Nested(AddressSchema)
    Application = fields.Nested(ApplicationSchema)
    Credentials = fields.Nested(CredentialsSchema)
    CustomBilling = None
    DemandDepositAccount = None
    PaymentAccount = None
    Reports = fields.Nested(ReportSchema)
    Transaction = fields.Nested(TransactionSchema)


class VerificationSchema (Schema):
    Address = fields.Nested(AddressSchema)
    Application = fields.Nested(ApplicationSchema)
    Credentials = fields.Nested(CredentialsSchema)
    DemandDepositAccount = None
    PaymentAccount = None
    Reports = fields.Nested(ReportSchema)
    Transaction = fields.Nested(TransactionSchema)


class VoidSchema (Schema):
    Application = fields.Nested(ApplicationSchema)
    Credentials = fields.Nested(CredentialsSchema)
    Reports = fields.Nested(ReportSchema)
    Transaction = fields.Nested(TransactionSchema)
