from marshmallow import Schema, fields


class CreatePlan (Schema):
    Application = fields.Nested("Application")
    Credentials = fields.Nested("Credentials")
    Reports = fields.Nested("Reports")
    ScheduledTask = None
    Transaction = fields.Nested("Transaction")


class FraudCheck (Schema):
    Address = fields.Nested("Address")
    AdvancedFraudChecks = None
    Application = fields.Nested("Application")
    Credentials = fields.Nested("Credentials")
    Reports = fields.Nested("Reports")
    ScheduledTask = None
    Transaction = fields.Nested("Transaction")


class PaymentAccountCreate (Schema):
    Applepay = None
    Application = fields.Nested("Application")
    Card = fields.Nested("Card")
    Credentials = None
    DemandDepositAccount = None
    Reports = fields.Nested("Reports")
    Transaction = fields.Nested("Transaction")


class PaymentAccountUpdate (Schema):
    Application = fields.Nested("Application")
    Card = fields.Nested("Card")
    Credentials = fields.Nested("Credentials")
    PaymentAccount = None
    Reports = None
    Transaction = fields.Nested("Transaction")


class ScheduledTaskDelete (Schema):
    Application = fields.Nested("Application")
    Credentials = fields.Nested("Credentials")
    Reports = None
    ScheduledTask = None
    Transaction = fields.Nested("Transaction")


class ScheduledTaskUpdate (Schema):
    Address = fields.Nested("Address")
    Application = fields.Nested("Application")
    Card = fields.Nested("Card")
    Credentials = fields.Nested("Credentials")
    PaymentAccount = None
    Reports = fields.Nested("Reports")
    ScheduledTask = None
    Transaction = fields.Nested("Transaction")


class TransactionQuery (Schema):
    Application = fields.Nested("Application")
    Card = fields.Nested("Card")
    Credentials = fields.Nested("Credentials")
    Reports = fields.Nested("Reports")
    Transaction = fields.Nested("Transaction")


class UpdatePlan (Schema):
    Application = None
    Credentials = None
    Reports = None
    ScheduledTask = None
    Transaction = None
