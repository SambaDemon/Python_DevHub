from marshmallow import Schema, fields


class CreatePlanSchema (Schema):
    Application = fields.Nested("Application")
    Credentials = fields.Nested("Credentials")
    Reports = fields.Nested("Reports")
    ScheduledTask = None
    Transaction = fields.Nested("Transaction")


class FraudCheckSchema (Schema):
    Address = fields.Nested("Address")
    AdvancedFraudChecks = None
    Application = fields.Nested("Application")
    Credentials = fields.Nested("Credentials")
    Reports = fields.Nested("Reports")
    ScheduledTask = None
    Transaction = fields.Nested("Transaction")


class PaymentAccountCreateSchema (Schema):
    Applepay = None
    Application = fields.Nested("Application")
    Card = fields.Nested("Card")
    Credentials = None
    DemandDepositAccount = None
    Reports = fields.Nested("Reports")
    Transaction = fields.Nested("Transaction")


class PaymentAccountUpdateSchema (Schema):
    Application = fields.Nested("Application")
    Card = fields.Nested("Card")
    Credentials = fields.Nested("Credentials")
    PaymentAccount = None
    Reports = None
    Transaction = fields.Nested("Transaction")


class ScheduledTaskDeleteSchema (Schema):
    Application = fields.Nested("Application")
    Credentials = fields.Nested("Credentials")
    Reports = None
    ScheduledTask = None
    Transaction = fields.Nested("Transaction")


class ScheduledTaskUpdateSchema (Schema):
    Address = fields.Nested("Address")
    Application = fields.Nested("Application")
    Card = fields.Nested("Card")
    Credentials = fields.Nested("Credentials")
    PaymentAccount = None
    Reports = fields.Nested("Reports")
    ScheduledTask = None
    Transaction = fields.Nested("Transaction")


class TransactionQuerySchema (Schema):
    Application = fields.Nested("Application")
    Card = fields.Nested("Card")
    Credentials = fields.Nested("Credentials")
    Reports = fields.Nested("Reports")
    Transaction = fields.Nested("Transaction")


class UpdatePlanSchema (Schema):
    Application = None
    Credentials = None
    Reports = None
    ScheduledTask = None
    Transaction = None
