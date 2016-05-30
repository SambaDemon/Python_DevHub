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

    Address = None
    BackgroundCheckFields = None
    Credentials = None
    LegalEntity = None
    Principal = None
    PrincipalArray = None


class UpdateSubMerchantSchema (Schema):

    Address = None
    Credentials = None
    ECheck = None
    Merchant = None
    PrimaryContact = None
    SubMerchantFunding = None
