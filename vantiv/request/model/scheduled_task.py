from ..schemas import Schema, fields
from ..utils import FrozenMixin


class ScheduledTaskSchema(Schema):
    ScheduledTaskID = fields.String()
    RunCycles = fields.String()
    RunStartDate = fields.Date()
    Amount = fields.Decimal()
    CreateDiscountArray = fields.String()
    CreateDiscount = fields.String()
    CreateAddOnArray = fields.String()
    CreateAddOn = fields.String()
    SubscriptionID = fields.String()
    Name = fields.String()
    Description = fields.String()
    RunFrequency = fields.String()
    TrialRunCycles = fields.String()
    TrialRunFrequency = fields.String()
    Active = fields.String()
    BillingDate = fields.Date()
    UpdateDiscountArray = fields.String()
    UpdateDiscount = fields.String()
    DeleteDiscountArray = fields.String()
    DeleteDiscount = fields.String()
    UpdateAddOnArray = fields.String()
    UpdateAddOn = fields.String()
    DeleteAddOnArray = fields.String()
    DeleteAddOn = fields.String()


class ScheduledTask(FrozenMixin):
    __schema__ = ScheduledTaskSchema

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
