# -*- coding: UTF-8 -*-
#

import requests
import logging



def getSkuDetail(skuID = None):
    url = ('http://www.mia.com/item-%r.html' % (skuID))
    logging.debug('sku[%r] url:[%r]' % (skuID, url))
    
    ret = requests.get(url)
    
    content = ret.content
    logging.debug('sku[%r] content(%r):[%r]' % (skuID, type(content), content))


def initLogging():
    #formatStr = '|%(levelname)s|%(asctime)s|%(pathname)s:%(lineno)d(%(funcName)s)%(threadName)s-%(thread)d|-%(message)s'
    logging.basicConfig(
        #format=formatStr,
        filename=r'F:\mia.log',
        level=logging.DEBUG)
    
    
def main():
    initLogging()
    getSkuDetail(1151126)
    

if __name__ == '__main__':
    main()
