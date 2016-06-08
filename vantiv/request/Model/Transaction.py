from marshmallow import Schema, fields

from . .utilities import frozen


class TransactionSchema(Schema):
    CustomerID = fields.Integer()
    PartialCapture = None
    ReferenceNumber = None
    AuthorizationDate = None
    ApprovalNumber = None
    TransactionAmount = None
    TransactionID = None
    ConvenienceFeeAmount = None
    PartialApprovedFlag = None
    FraudFilterOverride = None
    SurchargeFee = None
    ActionReason = None
    Verify = None
    TransactionType = None
    OrderSource = None
    TaxType = None
    OrderSource = None


class Transaction(object):
    __schema__ = TransactionSchema

    CustomerID = None
    PartialCapture = None
    ReferenceNumber = None
    AuthorizationDate = None
    ApprovalNumber = None
    TransactionAmount = None
    TransactionID = None
    ConvenienceFeeAmount = None
    PartialApprovedFlag = None
    FraudFilterOverride = None
    SurchargeFee = None
    ActionReason = None
    Verify = None
    TransactionType = None
    OrderSource = None
    TaxType = None
    OrderSource = None

    __setattr__ = frozen(object.__setattr__)
