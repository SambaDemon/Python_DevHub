from marshmallow import Schema, fields


class CreatePlanSchema (Schema):
    Application = fields.Nested("ApplicationSchema")
    Credentials = fields.Nested("CredentialsSchema")
    Reports = fields.Nested("ReportsSchema")
    ScheduledTask = None
    Transaction = fields.Nested("TransactionSchema")


class FraudCheckSchema (Schema):
    Address = fields.Nested("AddressSchema")
    AdvancedFraudChecks = None
    Application = fields.Nested("ApplicationSchema")
    Credentials = fields.Nested("CredentialsSchema")
    Reports = fields.Nested("ReportsSchema")
    ScheduledTask = None
    Transaction = fields.Nested("TransactionSchema")


class PaymentAccountCreateSchema (Schema):
    Applepay = None
    Application = fields.Nested("ApplicationSchema")
    Card = fields.Nested("CardSchema")
    Credentials = None
    DemandDepositAccount = None
    Reports = fields.Nested("ReportsSchema")
    Transaction = fields.Nested("TransactionSchema")


class PaymentAccountUpdateSchema (Schema):
    Application = fields.Nested("ApplicationSchema")
    Card = fields.Nested("CardSchema")
    Credentials = fields.Nested("CredentialsSchema")
    PaymentAccount = None
    Reports = None
    Transaction = fields.Nested("TransactionSchema")


class ScheduledTaskDeleteSchema (Schema):
    Application = fields.Nested("ApplicationSchema")
    Credentials = fields.Nested("CredentialsSchema")
    Reports = None
    ScheduledTask = None
    Transaction = fields.Nested("TransactionSchema")


class ScheduledTaskUpdateSchema (Schema):
    Address = fields.Nested("AddressSchema")
    Application = fields.Nested("ApplicationSchema")
    Card = fields.Nested("CardSchema")
    Credentials = fields.Nested("CredentialsSchema")
    PaymentAccount = None
    Reports = fields.Nested("ReportsSchema")
    ScheduledTask = None
    Transaction = fields.Nested("TransactionSchema")


class TransactionQuerySchema (Schema):
    Application = fields.Nested("ApplicationSchema")
    Card = fields.Nested("CardSchema")
    Credentials = fields.Nested("CredentialsSchema")
    Reports = fields.Nested("ReportsSchema")
    Transaction = fields.Nested("TransactionSchema")


class UpdatePlanSchema (Schema):
    Application = None
    Credentials = None
    Reports = None
    ScheduledTask = None
    Transaction = None
