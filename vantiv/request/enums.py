from enum import Enum
from marshmallow.fields import Field


class EnumField(Field):
    default_error_messages = {
        'by_name': 'Invalid enum member {name}',
        'by_value': 'Invalid enum value {value}'
    }

    def __init__(self, enum, by_value=False, *args, **kwargs):
        self.enum = enum
        self.by_value = by_value
        super(EnumField, self).__init__(*args, **kwargs)

    def _serialize(self, value, attr, obj):
        if value is None:
            return None

        if self.by_value:
            return value.value
        else:
            return value.name

    def _deserialize(self, value, attr, data):
        if self.by_value:
            return self._deserialize_by_value(value, attr, data)
        else:
            return self._deserialize_by_name(value, attr, data)

    def _deserialize_by_value(self, value, attr, data):
        try:
            return self.enum(value)
        except ValueError:
            self.fail('by_value', value=value)

    def _deserialize_by_name(self, value, attr, data):
        try:
            return getattr(self.enum, value)
        except AttributeError:
            self.fail('by_name', name=value)


class CountryEnum(Enum):
    USA = "USA"
    AF = "AF"
    AX = "AX"
    AL = "AL"
    DZ = "DZ"
    AS = "AS"
    AD = "AD"
    AO = "AO"
    AI = "AI"
    AQ = "AQ"
    AG = "AG"
    AR = "AR"
    AM = "AM"
    AW = "AW"
    AU = "AU"
    AT = "AT"
    AZ = "AZ"
    BS = "BS"
    BH = "BH"
    BD = "BD"
    BB = "BB"
    BY = "BY"
    BE = "BE"
    BZ = "BZ"
    BJ = "BJ"
    BM = "BM"
    BT = "BT"
    BO = "BO"
    BQ = "BQ"
    BA = "BA"
    BW = "BW"
    BV = "BV"
    BR = "BR"
    IO = "IO"
    BN = "BN"
    BG = "BG"
    BF = "BF"
    BI = "BI"
    KH = "KH"
    CM = "CM"
    CA = "CA"
    CV = "CV"
    KY = "KY"
    CF = "CF"
    TD = "TD"
    CL = "CL"
    CN = "CN"
    CX = "CX"
    CC = "CC"
    CO = "CO"
    KM = "KM"
    CG = "CG"
    CD = "CD"
    CK = "CK"
    CR = "CR"
    CI = "CI"
    HR = "HR"
    CU = "CU"
    CW = "CW"
    CY = "CY"
    CZ = "CZ"
    DK = "DK"
    DJ = "DJ"
    DM = "DM"
    DO = "DO"
    TL = "TL"
    EC = "EC"
    EG = "EG"
    SV = "SV"
    GQ = "GQ"
    ER = "ER"
    EE = "EE"
    ET = "ET"
    FK = "FK"
    FO = "FO"
    FJ = "FJ"
    FI = "FI"
    FR = "FR"
    GF = "GF"
    PF = "PF"
    TF = "TF"
    GA = "GA"
    GM = "GM"
    GE = "GE"
    DE = "DE"
    GH = "GH"
    GI = "GI"
    GR = "GR"
    GL = "GL"
    GD = "GD"
    GP = "GP"
    GU = "GU"
    GT = "GT"
    GG = "GG"
    GN = "GN"
    GW = "GW"
    GY = "GY"
    HT = "HT"
    HM = "HM"
    HN = "HN"
    HK = "HK"
    HU = "HU"
    IS = "IS"
    IN = "IN"
    ID = "ID"
    IR = "IR"
    IQ = "IQ"
    IE = "IE"
    IM = "IM"
    IL = "IL"
    IT = "IT"
    JM = "JM"
    JP = "JP"
    JE = "JE"
    JO = "JO"
    KZ = "KZ"
    KE = "KE"
    KI = "KI"
    KP = "KP"
    KR = "KR"
    KW = "KW"
    KG = "KG"
    LA = "LA"
    LV = "LV"
    LB = "LB"
    LS = "LS"
    LR = "LR"
    LY = "LY"
    LI = "LI"
    LT = "LT"
    LU = "LU"
    MO = "MO"
    MK = "MK"
    MG = "MG"
    MW = "MW"
    MY = "MY"
    MV = "MV"
    ML = "ML"
    MT = "MT"
    MH = "MH"
    MQ = "MQ"
    MR = "MR"
    MU = "MU"
    YT = "YT"
    MX = "MX"
    FM = "FM"
    MD = "MD"
    MC = "MC"
    MN = "MN"
    MS = "MS"
    MA = "MA"
    MZ = "MZ"
    MM = "MM"
    NA = "NA"
    NR = "NR"
    NP = "NP"
    NL = "NL"
    AN = "AN"
    NC = "NC"
    NZ = "NZ"
    NI = "NI"
    NE = "NE"
    NG = "NG"
    NU = "NU"
    NF = "NF"
    MP = "MP"
    NO = "NO"
    OM = "OM"
    PK = "PK"
    PW = "PW"
    PS = "PS"
    PA = "PA"
    PG = "PG"
    PY = "PY"
    PE = "PE"
    PH = "PH"
    PN = "PN"
    PL = "PL"
    PT = "PT"
    PR = "PR"
    QA = "QA"
    RE = "RE"
    RO = "RO"
    RU = "RU"
    RW = "RW"
    BL = "BL"
    KN = "KN"
    LC = "LC"
    MF = "MF"
    VC = "VC"
    WS = "WS"
    SM = "SM"
    ST = "ST"
    SA = "SA"
    SN = "SN"
    SC = "SC"
    SL = "SL"
    SG = "SG"
    SX = "SX"
    SK = "SK"
    SI = "SI"
    SB = "SB"
    SO = "SO"
    ZA = "ZA"
    GS = "GS"
    ES = "ES"
    LK = "LK"
    SH = "SH"
    PM = "PM"
    SD = "SD"
    SR = "SR"
    SJ = "SJ"
    SZ = "SZ"
    SE = "SE"
    CH = "CH"
    SY = "SY"
    TW = "TW"
    TJ = "TJ"
    TZ = "TZ"
    TH = "TH"
    TG = "TG"
    TK = "TK"
    TO = "TO"
    TT = "TT"
    TN = "TN"
    TR = "TR"
    TM = "TM"
    TC = "TC"
    TV = "TV"
    UG = "UG"
    UA = "UA"
    AE = "AE"
    GB = "GB"
    US = "US"
    UM = "UM"
    UY = "UY"
    UZ = "UZ"
    VU = "VU"
    VA = "VA"
    VE = "VE"
    VN = "VN"
    VG = "VG"
    VI = "VI"
    WF = "WF"
    EH = "EH"
    YE = "YE"
    ZM = "ZM"
    ZW = "ZW"
    RS = "RS"
    ME = "ME"
    SS = "SS"


class CardTypeEnum(Enum):
    MC = "MC"
    VI = "VI"
    AX = "AX"
    DC = "DC"
    DI = "DI"
    PP = "PP"
    JC = "JC"
    BL = "BL"
    EC = "EC"
    GC = "GC"
    NONE = ""


class TaxTypeIdentifierEnum(Enum):
    UNKOWN = "00"
    NATL_SALES = "01"
    ST_SALES = "02"
    CTY_SALES = "03"
    LCL_SALES = "04"
    MUN_SALES = "05"
    OTHER = "06"
    VAT = "10"
    GST = "11"
    PST = "12"
    HST = "13"
    QST = "14"
    ROOM = "20"
    OCCUPANCY = "21"
    ENERGY = "22"


class DeliveryTypeEnum(Enum):
    CNC = "CNC"
    DIG = "DIG"
    PHY = "PHY"
    SVC = "SVC"
    TBD = "TBD"


class CustomerTypeEnum(Enum):
    NEW = "New"
    EXISTING = "Existing"


class CurrencyEnum(Enum):
    AUD = "AUD"
    CAD = "CAD"
    CHF = "CHF"
    DKK = "DKK"
    EUR = "EUR"
    GBP = "GBP"
    HKD = "HKD"
    JPY = "JPY"
    NOK = "NOK"
    NZD = "NZD"
    SEK = "SEK"
    SGD = "SGD"
    USD = "USD"


class ResidenceStatusEnum(Enum):
    OWN = "Own"
    RENT = "Rent"
    OTHER = "Other"


class RecycleByEnum(Enum):
    MERCHANT = "Merchant"
    LITLE = "Litle"
    NONE = "None"


class OrderSourceEnum(Enum):
    ECOMMERCE = "ecommerce"
    INSTALLMENT = "installment"
    MAIL_ORDER = "mailorder"
    RECURRING = "recurring"
    RETAIL = "retail"
    TELEPHONE = "telephone"
    AUTH_3DS = "3dsAuthenticated"
    ATTEMPTED_3DS = "3dsAttempted"
    RECURRING_TEL = "recurringtel"
    ECHECK_PPD = "echeckppd"
    APPLEPAY = "applepay"


class TaxTypeEnum(Enum):
    PAYMENT = "payment"
    FEE = "fee"


class CapabilityEnum(Enum):
    NOT_USED = "notused"
    MAG_STRIPE = "magstripe"
    KEYED_ONLY = "keyedonly"


class EntryModeEnum(Enum):
    NOT_USED = "notused"
    KEYED = "keyed"
    TRACK1 = "track1"
    TRACK2 = "track2"
    COMPLETE_READ = "completeread"


class CardholderIDEnum(Enum):
    SIGNATURE = "signature"
    PIN = "pin"
    NO_PIN = "nopin"
    DIRECT_MARKET = "directmarket"


class CapabilityOfCatTerminalEnum(Enum):
    SELF_SERVICE = "self service"
