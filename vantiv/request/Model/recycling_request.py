from . .utilities import frozen


class RecyclingRequest(object):
    RecycleID = None
    RecycleBy = None

    __setattr__ = frozen(object.__setattr__)
