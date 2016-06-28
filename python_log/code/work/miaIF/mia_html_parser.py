# -*- coding: UTF-8 -*-

try: # for python 3.x
    from html.parser import HTMLParser
except: # for python 2.x
    from HTMLParser import HTMLParser

import requests
import logging

imgFilePath = 'f:\\'
logFile = 'f:\\mia.log'

def getContent(url, fileName):
    r = requests.get(url, stream=True)
    if r.status_code != 200:
        logging.debug('url get failed:[%r], url:[%r], filePath:[%r]' % (r.status_code, url, fileName))
        return False
    with open(fileName, 'wb') as fd:
        for chunk in r.iter_content(32384): # 32k buffer
            fd.write(chunk)
    return True

def getFileType(url):
    r = url.split('.')
    return r[len(r)-1]

class MiaHtmlParser(HTMLParser):
    def __init__(self, skuID):
        try: # for python 3.x
            super(MiaHtmlParser, self).__init__() ## call parent init method
        except: # for python 2.x
            HTMLParser.__init__(self)
        self.skuID = skuID
        self.headImgs = []
        self.headImg = False
        self.detailImgs = []
        self.detailImg = False
        self.divLevel = 0
        
    def handle_starttag(self, tag, attrs):
        if tag == 'div':
            for attr in attrs:
                attrName, attrVal = attr
                if attrName == 'class' and attrVal == 'small':
                    self.headImg = True
                    logging.debug('headImg on')
                    logging.debug('tag %r start, attrs:[%r]' % (tag, attrs))
                    return
                if attrName == 'class' and attrVal == 'clearfix datacon':
                    self.detailImg = True
                    logging.debug('detailImg on')
                    logging.debug('tag %r start, attrs:[%r]' % (tag, attrs))
                    return
                
        if tag == 'div' and (self.headImg or self.detailImg):
            self.divLevel = self.divLevel + 1
            logging.debug('start tag div, div level:[%r]' % (self.divLevel))
            
        if self.headImg and self.divLevel == 0:
            if tag == 'img':
                imgUrl = None
                for attr in attrs:
                    attrName, attrVal = attr
                    if not attrName == 'src':
                        continue
                    imgUrl = attrVal
                headImgUrl = imgUrl
                headImgFileName = ('%s%s_img_%s.%s' % 
                                   (imgFilePath, self.skuID, len(self.headImgs), getFileType(headImgUrl)))
                logging.debug('get head img:[%r], local file:[%r]' % (headImgUrl, headImgFileName))
                getContent(headImgUrl, headImgFileName)
                self.headImgs.append((headImgUrl, headImgFileName))
                
        if self.detailImg and self.divLevel == 0:
            if tag == 'img':
                imgUrl = None
                for attr in attrs:
                    attrName, attrVal = attr
                    if not attrName == 'data-src':
                        continue
                    imgUrl = attrVal
                detailImgUrl = imgUrl
                detailImgFileName = ('%s%s_detail_%s.%s' % 
                                   (imgFilePath, self.skuID, len(self.detailImgs), getFileType(detailImgUrl)))
                logging.debug('get detail img:[%r], local file:[%r]' % (detailImgUrl, detailImgFileName))
                getContent(detailImgUrl, detailImgFileName)
                self.detailImgs.append((detailImgUrl, detailImgFileName))            
        
    def handle_endtag(self, tag):
        if tag == 'div' and (self.headImg or self.detailImg):
            logging.debug('end tag div, div level:[%r], headImg:[%r], detailImg[%r]' % 
                  (self.divLevel, self.headImg, self.detailImg))
            if self.divLevel == 0:
                logging.debug('close img mode, headImg:[%r], detailImg:[%r]' % (self.headImg, self.detailImg))
                self.headImg = False if self.headImg else False
                self.detailImg = False if self.detailImg else False
            if self.divLevel > 0:
                self.divLevel = self.divLevel - 1
        
    def handle_data(self, data):
        pass
        
        

def initLogging():
    #formatStr = '|%(levelname)s|%(asctime)s|%(pathname)s:%(lineno)d(%(funcName)s)%(threadName)s-%(thread)d|-%(message)s'
    logging.basicConfig(
        #format=formatStr,
        #filename = logFile,
        level = logging.DEBUG)
    

def getSkuDetail(skuID = None):
    url = ('http://www.mia.com/item-%s.html' % (skuID))
    logging.debug('sku[%r] url:[%r]' % (skuID, url))
    
    ret = requests.get(url)
    
    #content = ret.content # content return binary data, text return encoding data
    #logging.debug('sku[%r] content(%r):[%r]' % (skuID, type(content), content))
    
    parser = MiaHtmlParser(skuID)
    parser.feed(ret.text)
    
    logging.debug('getSkuDetail(%r) Done!!!' % (skuID))
    logging.debug('Sku image detail:\n\thead[%r]\n\tdetail:[%r]' % (parser.headImgs, parser.detailImgs))
    
    return (parser.headImgs, parser.detailImgs, url)
    
    
def main():
    initLogging()
    getSkuDetail(1151126)
    #parser = MiaHtmlParser(1151126)
    #content = '<!DOCTYPE html>\n<html>\n<head>\n    <meta charset="utf-8">\n    <meta http-equiv="X-UA-Compatible" content="IE=Edge,chrome=1" />\n    <meta http-equiv="Cache-Control" content="no-transform" />\n    <meta http-equiv="Cache-Control" content="no-siteapp" />\n        <meta name="mobile-agent" content="format=html5;url=http://m.mia.com/item-1151126.html">\n        <title>\xe6\xa0\xbc\xe6\x9e\x97\xe5\x8d\x9a\xe5\xa3\xab  \xe5\xa9\xb4\xe5\xb9\xbc\xe5\x84\xbf\xe6\x8a\xa4\xe8\x82\x9a\xe8\x82\x9a\xe5\x85\x9c\xe5\xbd\xa9\xe6\xa3\x89\xe9\x80\xa0\xe5\x9e\x8b\xe8\x82\x9a\xe5\x85\x9c \xe5\xbd\xa9\xe6\xa3\x89\xe6\xa3\x95\xe3\x80\x90\xe4\xbb\xb7\xe6\xa0\xbc \xe7\x89\xb9\xe5\x8d\x96 \xe5\x9b\xbe\xe7\x89\x87100%\xe6\xad\xa3\xe5\x93\x81\xe3\x80\x91-\xe8\x9c\x9c\xe8\x8a\xbd</title>\n    <meta name="Keywords" content="\xe6\xa0\xbc\xe6\x9e\x97\xe5\x8d\x9a\xe5\xa3\xab ,\xe6\xa0\xbc\xe6\x9e\x97\xe5\x8d\x9a\xe5\xa3\xab  \xe4\xbb\xb7\xe6\xa0\xbc\xef\xbc\x8c\xe7\x89\xb9\xe5\x8d\x96" />\n    <meta name="Description" content="\xe8\x9c\x9c\xe8\x8a\xbd\xe6\x8f\x90\xe4\xbe\x9b\xe6\xa0\xbc\xe6\x9e\x97\xe5\x8d\x9a\xe5\xa3\xab  \xe9\x99\x90\xe6\x97\xb6\xe7\x89\xb9\xe5\x8d\x96\xef\xbc\x8c100%\xe6\xad\xa3\xe5\x93\x81\xe6\xa0\xbc\xe6\x9e\x97\xe5\x8d\x9a\xe5\xa3\xab  \xe6\x8a\x98\xe6\x89\xa3\xe4\xbb\xb7\xe6\xa0\xbc\xef\xbc\x8c\xe5\x8f\xa3\xe7\xa2\x91\xef\xbc\x8c\xe5\x9b\xbe\xe7\x89\x87\xe7\xad\x89\xe4\xbf\xa1\xe6\x81\xaf\xef\xbc\x8c\xe7\xbd\x91\xe8\xb4\xad\xe6\xa0\xbc\xe6\x9e\x97\xe5\x8d\x9a\xe5\xa3\xab  \xe5\xb0\xb1\xe4\xb8\x8a\xe8\x9c\x9c\xe8\x8a\xbd\xef\xbc\x81 " />\n    <meta property="qc:admins" content="145316263765116375" />\n            <link rel="canonical" href="http://www.mia.com/item-1151126.html"/>\n        <link rel="stylesheet" type="text/css" href="http://file02.miyabaobei.com/resources/styles/newPub.css?v=0413">\n    <link rel="stylesheet" href="http://file02.miyabaobei.com/resources/styles/headerFooter.css?v=2a02781ea6974d9ebcf1af31e29ca6db" type="text/css">        <link rel="stylesheet" href="http://file02.miyabaobei.com/resources/styles/main.css?v=20160531" type="text/css">\n    <link rel="stylesheet" href="http://file02.miyabaobei.com/resources/styles/add.css?v=1601131623" type="text/css">\n        <script src="http://file02.miyabaobei.com/resources/scripts/jquery-1.8.2.min.js" type="text/javascript"></script>\n    <script src="http://file02.miyabaobei.com/resources/scripts/newMiYaPub.js?v=9749d6625bbced56e67974c66fb11234" type="text/javascript"></script>\n\n            <script type="text/javascript" src="http://file02.miyabaobei.com/resources/scripts/init.js?v=20151102"></script>\n        <script type="text/javascript" src="http://file02.miyabaobei.com/resources/scripts/lwt.js?v=20160613"></script>\n    <script type="text/javascript">\n                    </script>\n</head>\n<body>\n<div class="header">\n    <div class="header-topbar">\n        <div class="w1100 clearfix">\n            <div class="l">\n                <a href="/app.html" target="_blank" title="\xe6\x89\x8b\xe6\x9c\xba\xe8\x9c\x9c\xe8\x8a\xbd" class="m"><i class="mia-icon icon-mobile">&#xe800;</i>\xe6\x89\x8b\xe6\x9c\xba\xe8\x9c\x9c\xe8\x8a\xbd</a>\n            </div>\n            <!-- \xe7\x99\xbb\xe5\xbd\x95\xe5\x89\x8d -->\n            <div class="r" style="display:none" id="unloginBox">\n                <span class="welcome">\xe4\xbd\xa0\xe5\xa5\xbd\xef\xbc\x8c\xe6\xac\xa2\xe8\xbf\x8e\xe6\x9d\xa5\xe5\x88\xb0\xe8\x9c\x9c\xe8\x8a\xbd\xef\xbc\x81</span><a href="http://www.mia.com/login?url=http%3A%2F%2Fwww.mia.com%2Fitem-1151126.html" title="\xe7\x82\xb9\xe5\x87\xbb\xe7\x99\xbb\xe5\xbd\x95" rel="nofollow">\xe7\x99\xbb\xe5\xbd\x95</a><em>|</em><a href="http://www.mia.com/register?url=http%3A%2F%2Fwww.mia.com%2Fitem-1151126.html" title="\xe7\x82\xb9\xe5\x87\xbb\xe6\xb3\xa8\xe5\x86\x8c" rel="nofollow">\xe5\x85\x8d\xe8\xb4\xb9\xe6\xb3\xa8\xe5\x86\x8c</a><a href="http://www.mia.com/help.html" target="_blank">\xe5\xb8\xae\xe5\x8a\xa9\xe4\xb8\xad\xe5\xbf\x83</a>\n            </div>\n            <!-- \xe7\x99\xbb\xe5\xbd\x95\xe5\x90\x8e -->\n            <div cla
    #parser.feed(content)
    logging.debug('Done!!!')
    

if __name__ == '__main__':
    main()
    
