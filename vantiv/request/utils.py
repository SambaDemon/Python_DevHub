class FrozenMixin:
    def __setattr__(self, name, value):
        if hasattr(self, name):
            return super().__setattr__(name, value)
        raise AttributeError("You cannot add attributes to %s" % self)


def remove_from_json(dictionary):
    for key in ("url", "method", "queryParams"):
        dictionary.pop(key, None)
    return dictionary


def get_transaction_id(response):
    response = response.decode('utf-8')
    key = 'TransactionID\":\"'
    location = response.find(key)
    value = response[location + len(key):]
    location = value.find('\"')
    value = value[:location]
    return value


def get_value_from_key(response, key):
    response = response.decode('utf-8')
    key = key + '\":\"'
    location = response.find(key)
    if location == -1:
        return None
    response = response[location + len(key):]
    location = response.find('\"')
    if location == -1:
        return None
    value = response[:location]
    return value
