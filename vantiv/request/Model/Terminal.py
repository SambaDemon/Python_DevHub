from marshmallow import Schema, fields

from ..utilities import frozen


class TerminalSchema(Schema):
    TerminalID = fields.Integer()
    Capability = None
    EntryMode = None
    CardholderID = fields.Integer()
    CapabilityOfCatTerminal = None


class Terminal(object):
    __schema__ = TerminalSchema

    TerminalID = None
    Capability = None
    EntryMode = None
    CardholderID = None
    CapabilityOfCatTerminal = None

    __setattr__ = frozen(object.__setattr__)
