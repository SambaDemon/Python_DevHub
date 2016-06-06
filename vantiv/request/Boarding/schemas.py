from marshmallow import Schema, fields


class CreateLegalEntitySchema (Schema):

    Address = fields.Nester("Address")
    Credentials = fields.Nested("Credentials")
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

    Address = fields.Nested("Address")
    BackgroundCheckFields = None
    Credentials = fields.Nested("Credentials")
    LegalEntity = None
    Principal = fields.Nested("Principal")
    PrincipalArray = None


class UpdateSubMerchantSchema (Schema):

    Address = fields.Nested("Address")
    Credentials = fields.Nested("Credentials")
    ECheck = None
    Merchant = fields.Nested("Merchant")
    PrimaryContact = None
    SubMerchantFunding = None
