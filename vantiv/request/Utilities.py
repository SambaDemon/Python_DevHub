def remove_from_json(dictionary):
    if 'url' in dictionary.keys():
        del dictionary['url']
    if 'method' in dictionary.keys():
        del dictionary['method']
    if 'queryParams' in dictionary.keys():
        del dictionary['queryParams']
    return dictionary


def frozen(set):
    def set_attr(self, name, value):
        if hasattr(self, name):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add attributesto %s" % self)
    # return set_attr
    return set


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
