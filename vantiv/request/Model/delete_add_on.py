from . .utilities import frozen


class DeleteAddOn(object):
    AddOnCode = None

    __setattr__ = frozen(object.__setattr__)
