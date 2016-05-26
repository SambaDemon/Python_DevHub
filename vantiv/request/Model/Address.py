from . .utilities import frozen


class Address(object):
    BillingName = None
    BillingFirstName = None
    BillingMiddleInitial = None
    BillingLastName = None
    BillingCompanyName = None
    BillingAddress1 = None
    BillingAddress2 = None
    BillingAddress3 = None
    BillingCity = None
    BillingState = None
    BillingZipcode = None
    BillingEmail = None
    BillingPhone = None
    ShippingName = None
    ShippingFirstName = None
    ShippingMiddleInitial = None
    ShippingLastName = None
    ShippingCompanyName = None
    ShippingAddress1 = None
    ShippingAddress2 = None
    ShippingAddress3 = None
    ShippingCity = None
    ShippingState = None
    ShippingZipcode = None
    ShippingEmail = None
    ShippingPhone = None
    BillingCountry = None
    ShippingCountry = None
    __setattr__ = frozen(object.__setattr__)
