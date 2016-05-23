from .Request import Request


class CreatePlan (Request):
    Application = None
    Credentials = None
    Reports = None
    ScheduledTask = None
    Transaction = None

    def __init__(self):
        super(CreatePlan, self).__init__("payment",
                                         "services",
                                         "createPlan",
                                         "POST")


class FraudCheck (Request):
    Address = None
    AdvancedFraudChecks = None
    Application = None
    Credentials = None
    Reports = None
    ScheduledTask = None
    Transaction = None

    def __init__(self):
        super(FraudCheck, self).__init__("payment",
                                         "services",
                                         "fraudCheck",
                                         "POST")


class PaymentAccountCreate (Request):
    Applepay = None
    Application = None
    Card = None
    Credentials = None
    DemandDepositAccount = None
    Reports = None
    Transaction = None

    def __init__(self):
        super(PaymentAccountCreate, self).__init__("payment",
                                                   "services",
                                                   "paymentAccountCreate",
                                                   "POST")


class PaymentAccountUpdate (Request):
    Application = None
    Card = None
    Credentials = None
    PaymentAccount = None
    Reports = None
    Transaction = None

    def __init__(self):
        super(PaymentAccountUpdate, self).__init__("payment",
                                                   "services",
                                                   "paymentAccountUpdate",
                                                   "POST")


class ScheduledTaskDelete (Request):
    Application = None
    Credentials = None
    Reports = None
    ScheduledTask = None
    Transaction = None

    def __init__(self):
        super(ScheduledTaskDelete, self).__init__("payment",
                                                  "services",
                                                  "scheduledTaskDelete",
                                                  "POST")


class ScheduledTaskUpdate (Request):
    Address = None
    Application = None
    Card = None
    Credentials = None
    PaymentAccount = None
    Reports = None
    ScheduledTask = None
    Transaction = None

    def __init__(self):
        super(ScheduledTaskUpdate, self).__init__("payment",
                                                  "services",
                                                  "scheduledTaskUpdate",
                                                  "POST")


class TransactionQuery (Request):
    Application = None
    Card = None
    Credentials = None
    Reports = None
    Transaction = None

    def __init__(self):
        super(TransactionQuery, self).__init__("payment",
                                               "services",
                                               "transactionQuery",
                                               "POST")


class UpdatePlan (Request):
    Application = None
    Credentials = None
    Reports = None
    ScheduledTask = None
    Transaction = None

    def __init__(self):
        super(UpdatePlan, self).__init__("payment",
                                         "services",
                                         "updatePlan",
                                         "POST")
