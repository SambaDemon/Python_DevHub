from . .Request import Request
from .schemas import (CreateLegalEntitySchema, CreateSubMerchantSchema,
                      RetrieveLegalEntitySchema, RetrieveMccListSchema,
                      RetrieveSubMerchantSchema, UpdateLegalEntitySchema,
                      UpdateSubMerchantSchema)


class CreateLegalEntity (Request):
    __schema__ = CreateLegalEntitySchema

    Address = None
    Credentials = None
    LegalEntity = None
    Principal = None
    PrincipalArray = None

    def __init__(self):
        super(CreateLegalEntity, self).__init__("boarding",
                                                "services",
                                                "createLegalEntity",
                                                "POST")


class CreateSubMerchant (Request):
    __schema__ = CreateSubMerchantSchema

    Address = None
    Credentials = None
    ECheck = None
    Merchant = None
    PrimaryContact = None
    SubMerchantFunding = None

    def __init__(self, entityID):
        super(CreateSubMerchant, self).__init__("boarding",
                                                "services",
                                                "createSubMerchant",
                                                "POST")
        self.queryParams['entityID'] = entityID


class RetrieveLegalEntity (Request):
    __schema__ = RetrieveLegalEntitySchema

    def __init__(self, entityID):
        super(RetrieveLegalEntity, self).__init__("boarding",
                                                  "services",
                                                  "retrieveLegalEntity",
                                                  "GET")
        self.queryParams['entityID'] = entityID


class RetrieveMccList (Request):
    __schema__ = RetrieveMccListSchema

    def __init__(self):
        super(RetrieveMccList, self).__init__("boarding",
                                              "services",
                                              "retrieveMccList",
                                              "GET")


class RetrieveSubMerchant (Request):
    __schema__ = RetrieveSubMerchantSchema

    def __init__(self, entityID, subMerchantID):
        super(RetrieveSubMerchant, self).__init__("boarding",
                                                  "services",
                                                  "retrieveSubMerchant",
                                                  "GET")
        self.queryParams['entityID'] = entityID
        self.queryParams['subMerchantID'] = subMerchantID


class UpdateLegalEntity (Request):
    __schema__ = UpdateLegalEntitySchema

    Address = None
    BackgroundCheckFields = None
    Credentials = None
    LegalEntity = None
    Principal = None
    PrincipalArray = None

    def __init__(self, entityID):
        super(UpdateLegalEntity, self).__init__("boarding",
                                                "services",
                                                "updateLegalEntity",
                                                "PUT")
        self.queryParams['entityID'] = entityID


class UpdateSubMerchant (Request):
    __schema__ = UpdateSubMerchantSchema

    Address = None
    Credentials = None
    ECheck = None
    Merchant = None
    PrimaryContact = None
    SubMerchantFunding = None

    def __init__(self, entityID, subMerchantID):
        super(UpdateSubMerchant, self).__init__("boarding",
                                                "services",
                                                "updateSubMerchant",
                                                "PUT")
        self.queryParams['entityID'] = entityID
        self.queryParams['subMerchantID'] = subMerchantID
