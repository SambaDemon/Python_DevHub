from . .Request import Request


class Credit (Request):
    Application = None
    Credentials = None
    CustomBilling = None
    Reports = None
    Transaction = None

    def __init__(self):
        super(Credit, self).__init__("payment", "check", "credit", "POST")


class Redeposit (Request):
    Application = None
    Credentials = None
    DemandDepositAccount = None
    PaymentAccount = None
    Reports = None
    Transaction = None

    def __init__(self):
        super(Redeposit, self).__init__("payment", "check", "redeposit", "POST")


class Return (Request):
    Address = None
    Application = None
    Credentials = None
    CustomBilling = None
    DemandDepositAccount = None
    PaymentAccount = None
    Reports = None
    Transaction = None

    def __init__(self):
        super(Return, self).__init__("payment", "check", "return", "POST")


class Sale (Request):
    Address = None
    Application = None
    Credentials = None
    CustomBilling = None
    DemandDepositAccount = None
    PaymentAccount = None
    Reports = None
    Transaction = None

    def __init__(self):
        super(Sale, self).__init__("payment", "check", "sale", "POST")


class Verification (Request):
    Address = None
    Application = None
    Credentials = None
    DemandDepositAccount = None
    PaymentAccount = None
    Reports = None
    Transaction = None

    def __init__(self):
        super(Verification, self).__init__("payment",
                                           "check",
                                           "verification",
                                           "POST")


class Void (Request):
    Application = None
    Credentials = None
    Reports = None
    Transaction = None

    def __init__(self):
        super(Void, self).__init__("payment", "check", "void", "POST")
