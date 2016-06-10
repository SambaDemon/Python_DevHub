from ..schemas import Schema, fields
from ..utilities import frozen
from ..enums import (EnumField, CustomerTypeEnum, CurrencyEnum,
                     ResidenceStatusEnum)


class IdentificationSchema(Schema):
    Ssn = fields.String()
    BirthDate = fields.Date()
    CustomerRegistrationDate = fields.Date()
    IncomeAmount = fields.Decimal()
    CustomerCheckingAccount = fields.String()
    CustomerSavingsAccount = fields.String()
    EmployerName = fields.String()
    CustomerWorkTelephone = fields.String()
    YearsAtResidence = fields.String()
    YearsAtEmployer = fields.String()
    CustomerType = EnumField(CustomerTypeEnum, by_value=True)
    IncomeCurrency = EnumField(CurrencyEnum, by_value=True)
    ResidenceStatus = EnumField(ResidenceStatusEnum, by_value=True)


class Identification(object):
    Ssn = None
    BirthDate = None
    CustomerRegistrationDate = None
    IncomeAmount = None
    CustomerCheckingAccount = None
    CustomerSavingsAccount = None
    EmployerName = None
    CustomerWorkTelephone = None
    YearsAtResidence = None
    YearsAtEmployer = None
    CustomerType = None
    IncomeCurrency = None
    ResidenceStatus = None

    __setattr__ = frozen(object.__setattr__)
