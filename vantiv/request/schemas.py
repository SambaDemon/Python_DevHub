import simplejson
from marshmallow import Schema, fields


class Schema(Schema):

    class Meta:
        json_module = simplejson
