from . .utilities import frozen


class ScheduledTask(object):
    ScheduledTaskID = None
    RunCycles = None
    RunStartDate = None
    Amount = None
    CreateDiscountArray = None
    CreateDiscount = None
    CreateAddOnArray = None
    CreateAddOn = None
    SubscriptionID = None
    Name = None
    Description = None
    RunFrequency = None
    TrialRunCycles = None
    TrialRunFrequency = None
    Active = None
    BillingDate = None
    UpdateDiscountArray = None
    UpdateDiscount = None
    DeleteDiscountArray = None
    DeleteDiscount = None
    UpdateAddOnArray = None
    UpdateAddOn = None
    DeleteAddOnArray = None
    DeleteAddOn = None

    __setattr__ = frozen(object.__setattr__)
