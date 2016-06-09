from marshmallow import Schema, fields

from ..Model.reports import ReportsSchema
from ..Model.address import AddressSchema
from ..Model.credentials import CredentialsSchema
from ..Model.application import ApplicationSchema
from ..Model.card import CardSchema
from ..Model.transaction import TransactionSchema
from ..Model.terminal import TerminalSchema
from ..Model.principal import PrincipalSchema
from ..Model.legal_entity import LegalEntitySchema


class CreateLegalEntitySchema (Schema):
    Address = fields.Nested(AddressSchema)
    Credentials = fields.Nested(CredentialsSchema)
    LegalEntity = fields.Nested(LegalEntitySchema)
    Principal = fields.Nested(PrincipalSchema)
    PrincipalArray = None


class CreateSubMerchantSchema (Schema):

    Address = fields.Nested(AddressSchema)
    Credentials = fields.Nested(CredentialsSchema)
    ECheck = None
    Merchant = None
    PrimaryContact = None
    SubMerchantFunding = None


class RetrieveLegalEntitySchema (Schema):
    pass


class RetrieveMccListSchema (Schema):
    pass


class RetrieveSubMerchantSchema (Schema):
    pass


class UpdateLegalEntitySchema (Schema):
    Address = fields.Nested(AddressSchema)
    BackgroundCheckFields = None
    Credentials = fields.Nested(CredentialsSchema)
    LegalEntity = None
    Principal = fields.Nested("PrincipalSchema")
    PrincipalArray = None


class UpdateSubMerchantSchema (Schema):
    Address = fields.Nested(AddressSchema)
    Credentials = fields.Nested(CredentialsSchema)
    ECheck = None
    Merchant = fields.Nested("MerchantSchema")
    PrimaryContact = None
    SubMerchantFunding = None
