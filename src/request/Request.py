
from .Config import Config
from .Utilities import RemoveFromJson
import jsonpickle
import ssl
import sys

if sys.version_info.major < 3:
    import urllib2 as urllib
else:
    import urllib.request, urllib.error, urllib.parse


class Request (object):
    def __getstate__(self):
        body = RemoveFromJson(self.__dict__.copy())
        return body

    def __init__(self, category, proxy, endpoint, method):
        self.queryParams = {}

        self.url = ("https://%s/%s/sp2/%s/v%s/%s" %
                    (Config.baseEndpoint,
                     category,
                     proxy,
                     Config.version,
                     endpoint))
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
                for key, value in self.queryParams.items():
                    queryParamString += key + "=" + value + "&"
                queryParamString = queryParamString[:-1]
            url = self.url + queryParamString
            body = jsonpickle.encode(self, unpicklable=False)
            if (Config.printRequest):
                print (body)
            if(Config.proxy):
                proxy = urllib.request.ProxyHandler(Config.proxy)
                auth = urllib.request.HTTPBasicAuthHandler()
                opener = urllib.request.build_opener(proxy,
                                                     auth,
                                                     urllib.request.HTTPHandler)
                urllib.request.install_opener(opener)
            req = urllib.request.Request(url)
            req.add_header('Authorization',
                           'VANTIV license=' + "\"" + Config.license + "\"")
            req.add_header('Content-Type', 'application/json')
            context = ssl._create_unverified_context()
            try:
                resp = urllib.request.urlopen(req,
                                              body.encode('UTF-8'),
                                              context=context)
                code = resp.getcode()
                contents = resp.read()
            except urllib.error.HTTPError as error:
                contents = error.read()
            if (Config.printResponse):
                print(contents)

            return contents
