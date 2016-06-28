# -*- coding: UTF-8 -*-

import pymysql
import logging


''''''
host = 'localhost'
user = 'root'
password = 'mysql'
db = 'mydb'
charset = 'utf8'
''''''

class DBObject(object):
    def __init__(self):
        self._connect = pymysql.connect(
            host = host,
            user = user,
            password = password,
            db = db,
            charset = charset,
            cursorclass = pymysql.cursors.DictCursor,
            autocommit = True, # if autocommit is False, we can't see other people updated data
        )

    def cursor(self):
        return self._connect.cursor()

    def commit(self):
        return self._connect.commit()

    def rollback(self):
        return self._connect.rollback()

    def connection(self):
        return self._connect

    def execute(self, sql):
        '''execute sql, get all result and close cursor, return result
        '''
        ret = None
        try:
            with self._connect.cursor() as cursor:
                cursor.execute(sql)
                ret = cursor.fetchall()
        finally:
            pass
        return ret


db = DBObject()


def translateD(d):
    d.marketTable = 1 if d.goodsStatus == '上架' else 0
    
    d.uptime = 0
    d.downtime = 0
    
    d.goodsVisibility = 'all' if d.goodsVisibility == u'均可' else 'search'
    
    d.goodsCanSellWithoutStore = 1 if d.goodsCanSellWithoutStore == u'是' else 0
    
    d.goodsActive = 1 if d.goodsActive == u'是' else 0
    
    d.tmpID = getGoodsTemplateID(d.goodsTemplate)
    d.typeID = getGoodsTypeID(d.goodsType)
    d.catID = getGoodsCatID(d.goodsTag)
    
    # product
    tmp = d.prodCategory.split('-')
    d.goodsSpecID = getGoodsSpecification(tmp[0])
    d.goodsSpecValueID = getGoodsSpecValueID(tmp[1])
    
    d.prodStatus = 1 if d.prodStatus == u'上架' else 0
    d.prodActive = 1 if d.prodActive == u'是' else 0
    
    d.feedbackID = getFeedbackID(d.prodFeedbackRule)
    
    d.defaultImgID = '1'
    d.goodsID = '1'
    d.prodID = '1'
    
    
GoodsCategory = dict()
def loadGoodsCategory():
    sql = ("select cat_id, name from goods_category")
    logging.debug(sql)
    ret = None
    with db.cursor() as cursor:
        cursor.execute(sql)
        ret = cursor.fetchall()
    
    for rec in ret:
        GoodsCategory[rec['name']] = rec['cat_id']
    logging.debug('GoodsCategory:[%r]' % (GoodsCategory))
    pass

def getGoodsCatID(goodsTag):
    if goodsTag in GoodsCategory:
        return GoodsCategory[goodsTag]
    return '0'

GoodsType = dict()
def loadGoodsType():
    sql = ("select type_id, name from goods_types")
    logging.debug(sql)
    ret = None
    with db.cursor() as cursor:
        cursor.execute(sql)
        ret = cursor.fetchall()
    
    for rec in ret:
        GoodsType[rec['name']] = rec['type_id']
    logging.debug('GoodsType:[%r]' % (GoodsType))
    pass

def getGoodsTypeID(goodsType):
    if goodsType in GoodsType:
        return GoodsType[goodsType]
    return '0'
    
GoodsTemplate = dict()
def loadGoodsTemplate():
    sql = ("select template_id, description from h5_template")
    logging.debug(sql)
    ret = None
    with db.cursor() as cursor:
        cursor.execute(sql)
        ret = cursor.fetchall()
    
    for rec in ret:
        GoodsTemplate[rec['description']] = rec['template_id']
    logging.debug('GoodsTemplate:[%r]' % (GoodsTemplate))
    pass

def getGoodsTemplateID(goodsTemplate):
    if goodsTemplate in GoodsTemplate:
        return GoodsTemplate[goodsTemplate]
    return '0'

GoodsSpecification = dict()
def loadGoodsSpecification():
    sql = ("select spec_id, name from goods_specification")
    logging.debug(sql)
    ret = None
    with db.cursor() as cursor:
        cursor.execute(sql)
        ret = cursor.fetchall()
    
    for rec in ret:
        GoodsSpecification[rec['name']] = rec['spec_id']
    logging.debug('GoodsSpecification:[%r]' % (GoodsSpecification))
    pass

def getGoodsSpecification(goodsSpec):
    if goodsSpec in GoodsSpecification:
        return GoodsSpecification[goodsSpec]
    return '0'

GoodsSpecValue = dict()
def loadGoodsSpecValue():
    sql = ("select spec_value_id, spec_value from goods_spec_values")
    logging.debug(sql)
    ret = None
    with db.cursor() as cursor:
        cursor.execute(sql)
        ret = cursor.fetchall()
    
    for rec in ret:
        GoodsSpecValue[rec['spec_value']] = rec['spec_value_id']
    logging.debug('GoodsSpecValue:[%r]' % (GoodsSpecValue))
    pass

def getGoodsSpecValueID(goodsSpecValue):
    if goodsSpecValue in GoodsSpecValue:
        return goodsSpecValue[goodsSpecValue]
    return '0'

FeedbackRelation = dict()
def loadFeedback():
    sql = ("select f_id, CONCAT(father_percent, '-', grand_percent, '-', ancestor_percent) as f_detail from goods_feedback")
    logging.debug(sql)
    ret = None
    with db.cursor() as cursor:
        cursor.execute(sql)
        ret = cursor.fetchall()
    
    for rec in ret:
        FeedbackRelation[rec['f_detail']] = rec['f_id']
    logging.debug('FeedbackRelation:[%r]' % (FeedbackRelation))
    pass

def getFeedbackID(feedbackRelation):
    if str(feedbackRelation) in FeedbackRelation:
        return FeedbackRelation[feedbackRelation]
    return '0'


def genSql(d):
    
#     cursor = db.cursor()
#     cursor.execute('start transaction') # need this as connection autocommit is True
    # images
    sql = ("insert into images (domain_id, url) values (4, '%s')")
    
    sql = sql % (d.qnDefaultImg)
    logging.debug(sql)
#     cursor.execute(sql)
#     if cursor.rowcount > 0:
#         pass
#     else:
#         logging.debug('SQL failed:[%r]!!!' % (sql))
#         cursor.execute('rollback')
#         cursor.close()
#         return
#     
#     d.defaultImgID = cursor.lastrowid
    
    # goods
    sql = ("insert into goods (bn, short_name, rotation_images, description, cat_id, type_id, source_url,"
           " markettable, uptime, downtime, like_count, r_like_count, sale_count, r_sale_count, visible, "
           " nostore_sell, default_image_id, template_id, disable, sale_img ) values ("
           " '%s', '%s', '%s', '%s', %s, %s, '%s', "
           " %s, %s, %s, %s, %s, %s, %s, '%s', "
           " %s, %s, %s, %s, %s)"
           )
    sql = sql % (d.goodsPn, d.goodsName, d.goodsRotateImg, d.description, d.catID, d.typeID, d.sourceUrl,
                 d.marketTable, d.uptime, d.downtime, d.goodsLikeCnt, 0, d.goodsSellCnt, 0, d.goodsVisibility,
                 d.goodsCanSellWithoutStore, d.defaultImgID, d.tmpID, d.goodsActive, 159554)
    logging.debug(sql)
#     cursor.execute(sql)
#     if cursor.rowcount > 0:
#         pass
#     else:
#         logging.debug('SQL failed:[%r]!!!' % (sql))
#         cursor.execute('rollback')
#         cursor.close()
#         return    
#     
#     d.goodsID = cursor.lastrowid
    
    # products
    sql = ("insert into products (goods_id, pn, markettable, uptime, downtime, "
           " cost, mkprice, price, freight, is_default, disable, freeze) values ("
           " %s, '%s', %s, %s, %s, "
           " %s, %s, %s, %s, %s, %s, %s)")
    
    sql = sql % (d.goodsID, d.prodPn, d.prodStatus, d.uptime, d.downtime,
                 d.prodCost, d.prodMKPrice, d.prodPrice, d.prodFreight, 1, d.prodActive, d.prodSku) # 1 is for is_default
    logging.debug(sql)
#     cursor.execute(sql)
#     if cursor.rowcount > 0:
#         pass
#     else:
#         logging.debug('SQL failed:[%r]!!!' % (sql))
#         cursor.execute('rollback')
#         cursor.close()
#         return
#         
#     d.prodID = cursor.lastrowid
    
    # goods specification
    sql = ("insert into goods_spec_relation (goods_id, product_id, spec_id, spec_value_id) values ("
           " %s, %s, %s, %s)")
    
    sql = sql % (d.goodsID, d.prodID, d.goodsSpecID, d.goodsSpecValueID)
    logging.debug(sql)
#     cursor.execute(sql)
#     if cursor.rowcount > 0:
#         pass
#     else:
#         logging.debug('SQL failed:[%r]!!!' % (sql))
#         cursor.execute('rollback')
#         cursor.close()
#         return    
    
    # feedback relation
    sql = ("insert into goods_feedback_relation (f_id, rel_id) values (%s, %s)")
    sql = sql % (d.feedbackID, d.prodID)
    logging.debug(sql)
#     cursor.execute(sql)
#     if cursor.rowcount > 0:
#         pass
#     else:
#         logging.debug('SQL failed:[%r]!!!' % (sql))
#         cursor.execute('rollback')
#         cursor.close()
#         return
#         
#     cursor.execute('commit')
    
from uploadQNTools import uploadFile
def uploadQN(d):
    qnHeadImgs = []
    qnDetailImgs = []
    for headImg in d.headImgs:
        uri = uploadFile(headImg[1], d.prodSku)
        qnHeadImgs.append(uri)
    for detailImg in d.detailImgs:
        uri = uploadFile(detailImg[1], d.prodSku)
        qnDetailImgs.append(uri)
    
    d.goodsRotateImg = '<img alt="" src="%s"/>' % ('"/><img alt="" src="'.join(qnHeadImgs))
    d.description = '<img alt="" src="%s"/>' % ('"/><img alt="" src="'.join(qnDetailImgs))
    d.qnDefaultImg = qnHeadImgs[0]
    
def initLogging():
    #formatStr = '|%(levelname)s|%(asctime)s|%(pathname)s:%(lineno)d(%(funcName)s)%(threadName)s-%(thread)d|-%(message)s'
    logging.basicConfig(
        #format=formatStr,
        #filename = logFile,
        level = logging.DEBUG)

def doWork(dList):
    for d in dList:
        uploadQN(d)
        translateD(d)
        genSql(d)
        

def doPrepare():
    loadGoodsCategory()
    loadGoodsType()
    loadGoodsTemplate()
    loadGoodsSpecification()
    loadGoodsSpecValue()
    loadFeedback()  
    
def main():
    initLogging()
    doPrepare()
    
    pass
    

if __name__ == '__main__':
    main()
