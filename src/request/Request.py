from __future__ import absolute_import

import jsonpickle
import requests

from .Config import Config
from .Utilities import RemoveFromJson


class Request (object):

    def __getstate__(self):
        body = RemoveFromJson(self.__dict__.copy())
        return body

    def __init__(self, category, proxy, endpoint, method):
        self.queryParams = {}
        self.url = ("https://%s/%s/sp2/%s/v%s/%s" %
                    (Config.baseEndpoint, category,
                     proxy, Config.version, endpoint))
        self.method = method

    def send(self):
        if (Config.doNotSend):
            body = jsonpickle.encode(self, unpicklable=False)
            if (Config.printRequest):
                print(body)
            return body
        else:
            queryParamString = ''
            if (self.queryParams):
                queryParamString = "?"
                for key, value in self.queryParams.iteritems():
                    queryParamString += key + "=" + value + "&"
                queryParamString = queryParamString[:-1]
            url = self.url + queryParamString
            body = jsonpickle.encode(self, unpicklable=False)
            if (Config.printRequest):
                print (body)
            try:
                headers = {'Authorization':
                           'VANTIV license='+"\""+Config.license+"\"",
                           'Content-Type': 'application/json'}
                response = requests.get(url,
                                        proxies=Config.proxy,
                                        data=body,
                                        headers=headers)
                code = response.status_code
                import ipdb; ipdb.set_trace() # DEBUG
                contents = response.json
            except Exception as error:
                contents = error.read()
            if (Config.printResponse):
                print(contents)

            return contents
