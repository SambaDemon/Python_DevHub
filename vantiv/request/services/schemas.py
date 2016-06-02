from marshmallow import Schema, fields


class CreatePlanSchema(Schema):
    Application = fields.nested('Application')
    Credentials = None
    Reports = None
    ScheduledTask = None
    Transaction = None


class FraudCheckSchema(Schema):
    Address = None
    AdvancedFraudChecks = None
    Application = None
    Credentials = None
    Reports = None
    ScheduledTask = None
    Transaction = None


class PaymentAccountCreateSchema(Schema):
    Applepay = None
    Application = None
    Card = None
    Credentials = None
    DemandDepositAccount = None
    Reports = None
    Transaction = None


class PaymentAccountUpdateSchema(Schema):
    Application = None
    Card = None
    Credentials = None
    PaymentAccount = None
    Reports = None
    Transaction = None


class ScheduledTaskDeleteSchema(Schema):
    Application = None
    Credentials = None
    Reports = None
    ScheduledTask = None
    Transaction = None


class ScheduledTaskUpdateSchema(Schema):
    Address = None
    Application = None
    Card = None
    Credentials = None
    PaymentAccount = None
    Reports = None
    ScheduledTask = None
    Transaction = None


class TransactionQuerySchema(Schema):
    Application = None
    Card = None
    Credentials = None
    Reports = None
    Transaction = None


class UpdatePlanSchema(Schema):
    Application = None
    Credentials = None
    Reports = None
    ScheduledTask = None
    Transaction = None
