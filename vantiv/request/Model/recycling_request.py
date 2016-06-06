from . .utilities import frozen


class RecyclingRequest(object):
    RecycleID = None
    RecycleBy = None

    class RecycleByEnum(object):
        def __init__(self, value):
            self.valuei = value

    RecycleByEnum.MERCHANT = "Merchant"
    RecycleByEnum.LITLE = "Litle"
    RecycleByEnum.NONE = "None"

    __setattr__ = frozen(object.__setattr__)
