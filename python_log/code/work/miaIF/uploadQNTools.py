# -*- coding: UTF-8 -*-
# 20160611

'''
'''
import logging
from qiniu import Auth, put_file, etag, urlsafe_base64_encode, BucketManager
import qiniu.config
import hashlib
import time
import os

## fake
access_key = ''
secret_key = ''

## true

## 三选一
defaultBucketUriBase = 'http://7xv97o.com1.z0.glb.clouddn.com'
#defaultBucketUriBase = 'http://7xv97o.com2.z0.glb.clouddn.com'
#defaultBucketUriBase = 'http://7xv97o.com2.z0.glb.qiniucdn.com'

defaultBucketName = 'cymmqr' # qiniubao保存时不区分大小写,(自动转小写), 你用大写访问 他说不存在!!!

defMiaImgPrefix = 'mia'  # mia file path: cymmqr/mia/skuID/xxxxxx

def uploadFile(filePath, skuID):
    q = Auth(access_key, secret_key)
    bucket_name = defaultBucketName
    key = ('%s/%s/%s%s') % (
            defMiaImgPrefix,
            skuID,
            hashlib.md5(filePath + str(time.time())).hexdigest(),
            os.path.splitext(filePath)[1]
            )

    token = q.upload_token(bucket_name, key)
    ret, info = put_file(token, key, filePath)
    logging.debug('upload qiniu ret:[%r]' % (ret))
    if 'key' not in ret:
        return None
    retFileUri = ('%s/%s') % (defaultBucketUriBase, key)
    logging.debug('upload qiniu file uri:[%r]' % (retFileUri))
    return retFileUri

def removeFile(key):
    q = Auth(access_key, secret_key)
    bucket_name = defaultBucketName
    bucket = BucketManager(q)

    ret, info = bucket.delete(bucket_name, key)
    logging.debug('remove qiniu file uri:[%r]' % (key))
    return key

def getKeyFromUri(uri):
    pos = uri.find(defaultBucketUriBase)
    if pos == -1:
        logging.debug('invalid qiniu CymmQR uri:[%r]' % (uri))
    key = uri[pos + len(defaultBucketUriBase) + 1] # +1 for '/'
    return key

def updateFile(filePath, uri):
    q = Auth(access_key, secret_key)
    bucket_name = defaultBucketName
    bucket = BucketManager(q)
    key = getKeyFromUri(uri)
    # delete
    ret, info = bucket.delete(bucket_name, key)
    # upload
    token = q.upload_token(bucket_name, key)
    ret, info = put_file(token, key, filePath)
    if 'key' not in ret:
        return None
    retFileUri = ('%s/%s') % (defaultBucketUriBase, key)
    logging.debug('upload qiniu file uri:[%r]' % (retFileUri))
    return retFileUri
