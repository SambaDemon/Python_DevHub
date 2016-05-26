from . .utilities import frozen


class Application(object):
    ApplicationID = 11470043

    __setattr__ = frozen(object.__setattr__)
