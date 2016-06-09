from marshmallow import Schema, fields

from ..Models.address import AddressSchema
from ..Models.credentials import CredentialsSchema
from ..Models.principal import PrincipalSchema
from ..Models.merchant import MerchantSchema


class CreateLegalEntitySchema (Schema):
    Address = fields.Nester(AddressSchema)
    Credentials = fields.Nested(CredentialsSchema)
    LegalEntity = None
    Principal = None
    PrincipalArray = None


class CreateSubMerchantSchema (Schema):

    Address = None
    Credentials = None
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
    Principal = fields.Nested(PrincipalSchema)
    PrincipalArray = None


class UpdateSubMerchantSchema (Schema):
    Address = fields.Nested(AddressSchema)
    Credentials = fields.Nested(CredentialsSchema)
    ECheck = None
    Merchant = fields.Nested(MerchantSchema)
    PrimaryContact = None
    SubMerchantFunding = None
