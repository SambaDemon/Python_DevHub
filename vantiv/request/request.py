from __future__ import absolute_import
import logging
import ssl
import urllib.request as urllib
from .config import Config
from .utils import remove_from_json

logger = logging.getLogger(__name__)


class Request (object):
    def __getstate__(self):
        body = remove_from_json(self.__dict__.copy())
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
            body, error = self.__schema__().dumps(self)
            if error:
                logger.error(error)
                raise AttributeError()
                logger.debug(body)
            return body
        else:
            queryParamString = ''
            if (self.queryParams):
                queryParamString = "?"
                for key, value in self.queryParams.items():
                    queryParamString += key + "=" + value + "&"
                queryParamString = queryParamString[:-1]
            url = self.url + queryParamString
            body, error = self.__schema__().dumps(self)
            if error:
                raise AttributeError()
            logger.debug(body)
            if(Config.proxy):
                proxy = urllib.ProxyHandler(Config.proxy)
                auth = urllib.HTTPBasicAuthHandler()
                opener = urllib.build_opener(proxy,
                                             auth,
                                             urllib.request.HTTPHandler)
                urllib.install_opener(opener)
            req = urllib.Request(url)
            req.add_header('Authorization',
                           'VANTIV license=' + "\"" + Config.license + "\"")
            req.add_header('Content-Type', 'application/json')
            context = ssl._create_unverified_context()
            try:
                resp = urllib.urlopen(req,
                                      body.encode('UTF-8'),
                                      context=context)
                code = resp.getcode()
                logger.debug(code)
                contents = resp.read()
            except urllib.HTTPError as error:
                contents = error.read()
            logger.debug(contents)
            return contents
