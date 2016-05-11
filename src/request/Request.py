from __future__ import absolute_import

import jsonpickle
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
        try:
            import urllib2
        except ImportError:
            import urllib.request as urllib2
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
            if(Config.proxy):
                proxy = urllib2.ProxyHandler(Config.proxy)
                auth = urllib2.HTTPBasicAuthHandler()
                opener = urllib2.build_opener(proxy, auth, urllib2.HTTPHandler)
                urllib2.install_opener(opener)
            req = urllib2.Request(url)
            req.add_header('Authorization',
                           'VANTIV license='+"\""+Config.license+"\"")
            req.add_header('Content-Type', 'application/json')
            try:
                import sys
                if sys.version_info.major == 3:
                    body = body.encode('utf-8')
                resp = urllib2.urlopen(req, body)
                code = resp.getcode()
                contents = resp.read()
            except urllib2.HTTPError as error:
                contents = error.read()
            if (Config.printResponse):
                print(contents)

            return contents
