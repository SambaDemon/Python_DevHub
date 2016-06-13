from ..schemas import Schema, fields
from ..utils import FrozenMixin
from ..enums import (EnumField, CapabilityEnum, EntryModeEnum,
                     CardholderIDEnum, CapabilityOfCatTerminalEnum)


class TerminalSchema(Schema):
    TerminalID = fields.String()
    Capability = EnumField(CapabilityEnum, by_value=True)
    EntryMode = EnumField(EntryModeEnum, by_value=True)
    CardholderID = EnumField(CardholderIDEnum, by_value=True)
    CapabilityOfCatTerminal = EnumField(CapabilityOfCatTerminalEnum,
                                        by_value=True)


class Terminal(FrozenMixin):
    __schema__ = TerminalSchema

    TerminalID = None
    Capability = None
    EntryMode = None
    CardholderID = None
    CapabilityOfCatTerminal = None
