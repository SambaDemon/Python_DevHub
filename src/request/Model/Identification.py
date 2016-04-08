import sys
from . .Utilities import Frozen

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
    class CustomerTypeEnum(object):
        def __init__(self, value):
            self.value=value
    CustomerTypeEnum.NEW = "New"
    CustomerTypeEnum.EXISTING = "Existing"
    class IncomeCurrencyEnum(object):
        def __init__(self, value):
            self.value=value
    IncomeCurrencyEnum.AUD = "AUD"
    IncomeCurrencyEnum.CAD = "CAD"
    IncomeCurrencyEnum.CHF = "CHF"
    IncomeCurrencyEnum.DKK = "DKK"
    IncomeCurrencyEnum.EUR = "EUR"
    IncomeCurrencyEnum.GBP = "GBP"
    IncomeCurrencyEnum.HKD = "HKD"
    IncomeCurrencyEnum.JPY = "JPY"
    IncomeCurrencyEnum.NOK = "NOK"
    IncomeCurrencyEnum.NZD = "NZD"
    IncomeCurrencyEnum.SEK = "SEK"
    IncomeCurrencyEnum.SGD = "SGD"
    IncomeCurrencyEnum.USD = "USD"
    class ResidenceStatusEnum(object):
        def __init__(self, value):
            self.value=value
    ResidenceStatusEnum.OWN = "Own"
    ResidenceStatusEnum.RENT = "Rent"
    ResidenceStatusEnum.OTHER = "Other"
    __setattr__=Frozen(object.__setattr__)