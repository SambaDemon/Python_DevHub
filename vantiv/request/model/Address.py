from ..schemas import Schema, fields
from ..enums import EnumField, CountryEnum
from ..utilities import frozen


class AddressSchema(Schema):
    BillingName = fields.String()
    BillingFirstName = fields.String()
    BillingMiddleInitial = fields.String()
    BillingLastName = fields.String()
    BillingCompanyName = fields.String()
    BillingAddress1 = fields.String()
    BillingAddress2 = fields.String()
    BillingAddress3 = fields.String()
    BillingCity = fields.String()
    BillingState = fields.String()
    BillingZipcode = fields.String()
    BillingEmail = fields.String()
    BillingPhone = fields.String()
    ShippingName = fields.String()
    ShippingFirstName = fields.String()
    ShippingMiddleInitial = fields.String()
    ShippingLastName = fields.String()
    ShippingCompanyName = fields.String()
    ShippingAddress1 = fields.String()
    ShippingAddress2 = fields.String()
    ShippingAddress3 = fields.String()
    ShippingCity = fields.String()
    ShippingState = fields.String()
    ShippingZipcode = fields.String()
    ShippingEmail = fields.String()
    ShippingPhone = fields.String()
    BillingCountry = EnumField(CountryEnum)
    ShippingCountry = EnumField(CountryEnum)


class Address(object):
    __schema__ = AddressSchema

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
