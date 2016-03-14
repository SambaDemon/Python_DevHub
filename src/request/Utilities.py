
def RemoveFromJson(dictionary):
    if 'url' in dictionary.keys():
        del dictionary['url']
    if 'method' in dictionary.keys():
        del dictionary['method']
    if 'queryParams' in dictionary.keys():
    	del dictionary['queryParams']
    return dictionary

def Frozen(set):
    def set_attr(self,name,value):
        if hasattr(self,name):
            set(self,name,value) 
        else:
            raise AttributeError("You cannot add attributes to %s" % self)
    return set_attr

def getTransactionID(response):
    key = 'TransactionID\":\"'
    location = response.find(key)
    value = response[location + len(key):]
    location = value.find('\"')
    value = value[:location]
    return value


def getValueFromKey(response, key):
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
