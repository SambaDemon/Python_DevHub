from . .utilities import frozen


class Credentials(object):
    AcceptorID = None

    __setattr__ = frozen(object.__setattr__)
