# -*- coding: UTF-8 -*-

import xlrd
import logging
from decimal import Decimal


skuFile = u'f:\\现有sku.xlsx'
skuFile = u'f:\\现有sku.xls'

class SkuCol(object):
    prodSku = 'A'
    goodsPn = 'B'
    goodsName = 'D'
    store = 'I'
    goodsTag = 'J'
    goodsType = 'K'
    goodsStatus = 'L'
    goodsLikeCnt = 'M'
    goodsSellCnt = 'N'
    goodsVisibility = 'O'
    goodsCanSellWithoutStore = 'P'
    goodsActive = 'Q'
    goodsTemplate = 'R'
    
    prodPn = 'S'
    prodCategory = 'T'
    prodStatus = 'U'
    prodCost = 'V'
    prodMKPrice = 'W'
    prodPrice = 'X'
    prodFreight = 'AB'
    prodBrand = 'AI'
    prodFeedbackRule = 'Z'
    prodActive = 'AG'
    prodDefault = 'AE'
    
    prodProfit = 'AJ'
    prodProfitRate = 'AK'
    prodCpyProfit = 'AL'
    prodCpyProfitRate = 'AM'
    prodDistProfit = 'AN'
    prodDistProfitRate = 'AO'
    

_attrs = dir(SkuCol)
goodsAttrs = []
prodAttrs = []
for attr in _attrs:
    if 'goods' in attr:
        goodsAttrs.append(attr)
    if 'prod' in attr:
        prodAttrs.append(attr)
        
    goodsAttrs.append('marketTable')
    goodsAttrs.append('uptime')
    goodsAttrs.append('downtime')
    goodsAttrs.append('tmpID')
    goodsAttrs.append('typeID')
    goodsAttrs.append('catID')
    goodsAttrs.append('goodsSpecID')
    goodsAttrs.append('goodsSpecValueID')
    
    goodsAttrs.append('goodsRotateImg')
    goodsAttrs.append('description')
    goodsAttrs.append('qnDefaultImg')
    
    prodAttrs.append('prodStatus')
    prodAttrs.append('prodActive')
    prodAttrs.append('feedbackID')
    
    prodAttrs.append('qnHeadImgs')
    prodAttrs.append('qnDetailImgs')
    
    prodAttrs.append('headImgs')
    prodAttrs.append('detailImgs')
    prodAttrs.append('sourceUrl')
    
    # unique
    prodAttrs = list(set(prodAttrs))
    goodsAttrs = list(set(goodsAttrs))
    

class obj(object):
    pass

def pobj(d):
    print('\nobj:[%r]' % (d))
    for attr in goodsAttrs:
        if hasattr(d, attr):
            col = getattr(SkuCol, attr) if hasattr(SkuCol, attr) else 'None'
            logging.debug('\t%r(%r):%r' % (attr, col, getattr(d, attr)))
            
    print()
    for attr in prodAttrs:
        if hasattr(d, attr):
            col = getattr(SkuCol, attr) if hasattr(SkuCol, attr) else 'None'
            logging.debug('\t%r(%r):%r' % (attr, col, getattr(d, attr)))
            

def getColIndex(colName, offset = 0):
    colName = str.lower(colName).strip()
    rCol = colName[::-1]
    ret = 0
    base = ord('a') - 1
    retBase = 26
    retBaseIdx = 0
    for c in rCol:
        ret += (ord(c) - base) * (retBase ** retBaseIdx)
#         print "character: {0}, value={3} ,ret={1}, retBaseIdx={2}, index base={4}"\
#             .format(c, ret, retBaseIdx, (ord(c)-base), retBase ** retBaseIdx)
        retBaseIdx +=1
    return ret + offset - 1 # -1 for start position: 0


def getCellVal(sheet, rowIdx, colIdx):
    return sheet.cell_value(rowIdx, getColIndex(colIdx))


def toDecimalStr(val, precision):
    '''
    toDecimalStr('123.012345', '1') == '123'
    toDeciamlStr('123.012345', '1.00' == '123.01'
    toDeciamlStr('123.012345', '1.0000' == '123.0123'
    toDeciamlStr('123.012345', '1.00000' == '123.01235'
    '''
    try:
        return str(Decimal(val).quantize(Decimal(precision)))
    except:
        return val

def readMiaXls(fileName):
    book = xlrd.open_workbook(fileName)
    sheet = book.sheet_by_index(0)
    
    
    rowIdx = 1 # read from line 1
    dList = []
    print('sheet rows:[%r]' % (sheet.nrows))
    while rowIdx < sheet.nrows and rowIdx < 3:
        d = obj()
        
        d.prodSku = toDecimalStr(getCellVal(sheet, rowIdx, SkuCol.prodSku), '1')
        d.goodsPn = getCellVal(sheet, rowIdx, SkuCol.goodsPn)
        d.goodsName = getCellVal(sheet, rowIdx, SkuCol.goodsName)
        d.goodsTag = getCellVal(sheet, rowIdx, SkuCol.goodsTag)
        d.goodsType = getCellVal(sheet, rowIdx, SkuCol.goodsType)
        d.goodsStatus = getCellVal(sheet, rowIdx, SkuCol.goodsStatus)
        
        d.goodsVisibility = getCellVal(sheet, rowIdx, SkuCol.goodsVisibility)
        d.goodsCanSellWithoutStore = getCellVal(sheet, rowIdx, SkuCol.goodsCanSellWithoutStore)
        d.goodsActive = getCellVal(sheet, rowIdx, SkuCol.goodsActive)
        d.goodsTemplate = getCellVal(sheet, rowIdx, SkuCol.goodsTemplate)
        
        d.goodsLikeCnt = getCellVal(sheet, rowIdx, SkuCol.goodsLikeCnt)
        d.goodsSellCnt = getCellVal(sheet, rowIdx, SkuCol.goodsSellCnt)
        
        d.prodPn = getCellVal(sheet, rowIdx, SkuCol.prodPn)
        d.prodCategory = getCellVal(sheet, rowIdx, SkuCol.prodCategory)
        d.prodStatus = getCellVal(sheet, rowIdx, SkuCol.prodStatus)

        d.prodCost = toDecimalStr(getCellVal(sheet, rowIdx, SkuCol.prodCost), '1.00')
        d.prodMKPrice = toDecimalStr(getCellVal(sheet, rowIdx, SkuCol.prodMKPrice), '1.00')
        d.prodPrice = toDecimalStr(getCellVal(sheet, rowIdx, SkuCol.prodPrice), '1.00')
        d.prodFreight = toDecimalStr(getCellVal(sheet, rowIdx, SkuCol.prodFreight), '1.00')
        d.prodActive = getCellVal(sheet, rowIdx, SkuCol.prodActive)
        
        d.prodBrand = getCellVal(sheet, rowIdx, SkuCol.prodBrand)
        
        d.prodProfit = toDecimalStr(getCellVal(sheet, rowIdx, SkuCol.prodProfit), '1.00')
        d.prodProfitRate = toDecimalStr(getCellVal(sheet, rowIdx, SkuCol.prodProfitRate), '1.00')
        d.prodCpyProfit = toDecimalStr(getCellVal(sheet, rowIdx, SkuCol.prodCpyProfit), '1.00')
        d.prodCpyProfitRate = toDecimalStr(getCellVal(sheet, rowIdx, SkuCol.prodCpyProfitRate), '1.00')
        d.prodDistProfit = toDecimalStr(getCellVal(sheet, rowIdx, SkuCol.prodDistProfit), '1.00')
        d.prodDistProfitRate = toDecimalStr(getCellVal(sheet, rowIdx, SkuCol.prodDistProfitRate), '1.00')
        
        d.prodFeedbackRule = getCellVal(sheet, rowIdx, SkuCol.prodFeedbackRule)
        
        rowIdx = rowIdx + 1
        
        pobj(d)
        dList.append(d)
    return dList

from mia_html_parser import getSkuDetail
from mia_gen_sql import doPrepare, doWork
def crawlMiaData(d):
    d.headImgs, d.detailImgs, d.sourceUrl = getSkuDetail(d.prodSku)

def crawlD(dList):
    for d in dList:
        crawlMiaData(d)
        pobj(d)
    doWork(dList)
    logging.debug('###########after doWork()###############')
    for d in dList:
        pobj(d)
        
def initLogging():
    #formatStr = '|%(levelname)s|%(asctime)s|%(pathname)s:%(lineno)d(%(funcName)s)%(threadName)s-%(thread)d|-%(message)s'
    logging.basicConfig(
        #format=formatStr,
        #filename = logFile,
        level = logging.DEBUG)
    
def main():
    #print('col "A" index is:[%r]' % (getColIndex('A')))
    initLogging()
    doPrepare()
    ret = readMiaXls(skuFile)
    crawlD(ret)
    
    

if __name__ == '__main__':
    main()
    
    
