#! /usr/bin/python3
#######################################################################
#     File Name           :     upload_file.py
#     Created By          :     Les1ie
#     Email               :     iansmith@qq.com
#     Creation Date       :     [2017-07-08 23:18]
#     Last Modified       :     [2017-07-09 01:32]
#     Description         :     upload file to qiniu 
#######################################################################

import sys

from qiniu import Auth, put_file, etag, urlsafe_base64_encode
import qiniu.config

filename = sys.argv[1]
access_key = ""
secret_key = ""

q = Auth(access_key, secret_key)
bucket_name = ""
bucket_url = ""

def upload_tempfile(bucket_name, filename):
    token = q.upload_token(bucket_name, filename, 10000)
    r = put_file(token, filename, filename)
    if "status_code:200" in str(r):
        print("success, url: ", bucket_url+filename)

upload_tempfile(bucket_name, filename)






