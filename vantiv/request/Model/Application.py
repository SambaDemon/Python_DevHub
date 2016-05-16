from . .Utilities import Frozen


class Application(object):
    ApplicationID = 11470043

    __setattr__ = Frozen(object.__setattr__)
