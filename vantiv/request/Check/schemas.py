from marshmallow import Schema, fields


class CreditSchema (Schema):
    Application = fields.Nested("Application")
    Credentials = fields.Nested("Credentials")
    CustomBilling = None
    Reports = fields.Nested("Reports")
    Transaction = fields.Nested("Transaction")


class RedepositSchema (Schema):
    Application = fields.Nested("Application")
    Credentials = fields.Nested("Credentials")
    DemandDepositAccount = None
    PaymentAccount = None
    Reports = fields.Nested("Reports")
    Transaction = fields.Nested("Transaction")


class ReturnSchema (Schema):
    Address = fields.Nested("Address")
    Application = fields.Nested("Application")
    Credentials = fields.Nested("Credentials")
    CustomBilling = None
    DemandDepositAccount = None
    PaymentAccount = None
    Reports = fields.Nested("Report")
    Transaction = fields.Nested("Transaction")


class SaleSchema (Schema):
    Address = fields.Nested("Address")
    Application = fields.Nested("Application")
    Credentials = fields.Nested("Credentials")
    CustomBilling = None
    DemandDepositAccount = None
    PaymentAccount = None
    Reports = fields.Nested("Reports")
    Transaction = fields.Nested("Transaction")


class VerificationSchema (Schema):
    Address = fields.Nested("Address")
    Application = fields.Nested("Application")
    Credentials = fields.Nested("Credentials")
    DemandDepositAccount = None
    PaymentAccount = None
    Reports = fields.Nested("Reports")
    Transaction = fields.Nested("Transaction")


class VoidSchema (Schema):
    Application = fields.Nested("Application")
    Credentials = fields.Nested("Credentials")
    Reports = fields.Nested("Reports")
    Transaction = fields.Nested("Transaction")
