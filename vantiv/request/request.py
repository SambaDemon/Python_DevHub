from __future__ import absolute_import
import logging
import requests
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
                proxies = Config.proxy
            else:
                proxies = {}
            headers = {
                'Authorization':
                    'VANTIV license=' + "\"" + Config.license + "\"",
                'Content-Type': 'application/json'}
            resp = requests.post(url=url, headers=headers, proxies=proxies,
                                 data=body.encode('UTF-8'))
            if resp.ok:
                contents = resp.content
                logger.debug(contents)
            else:
                contents = resp.content
                logger.debug(contents)
            return contents
