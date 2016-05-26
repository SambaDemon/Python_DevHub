from . .utilities import frozen


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
