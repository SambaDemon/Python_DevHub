from ..schemas import Schema, fields
from ..utilities import frozen
from ..enums import (EnumField, CapabilityEnum, EntryModeEnum,
                     CardholderIDEnum, CapabilityOfCatTerminalEnum)


class TerminalSchema(Schema):
    TerminalID = fields.String()
    Capability = EnumField(CapabilityEnum, by_value=True)
    EntryMode = EnumField(EntryModeEnum, by_value=True)
    CardholderID = EnumField(CardholderIDEnum, by_value=True)
    CapabilityOfCatTerminal = EnumField(CapabilityOfCatTerminalEnum,
                                        by_value=True)


class Terminal(object):
    __schema__ = TerminalSchema

    TerminalID = None
    Capability = None
    EntryMode = None
    CardholderID = None
    CapabilityOfCatTerminal = None

    __setattr__ = frozen(object.__setattr__)
