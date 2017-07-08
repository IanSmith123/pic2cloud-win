#! /usr/bin/env python
#######################################################################
#     File Name           :     upload_img.py
#     Created By          :     Les1ie
#     Email               :     iansmith@qq.com
#     Creation Date       :     [2017-07-08 23:49]
#     Last Modified       :     [2017-07-09 01:31]
#     Description         :     upload temp img 
#######################################################################
import sys
import time

from PIL import ImageGrab
from qiniu import Auth, put_file, etag, urlsafe_base64_encode
import qiniu.config

from win32clipboard import *
import win32con
import win32api

access_key = ""
secret_key = ""
bucket_name = ""
bucket_url = ""

q = Auth(access_key, secret_key)

def upload_img(bucket_name, filename):
    token = q.upload_token(bucket_name, filename, 9000000000000)
    r = put_file(token, filename, filename)
    if "status_code:200" in str(r):
        md_url = "![]("+bucket_url+filename+")"
        print("success,markdown url: ", md_url)
        return md_url

def save_img():
    pic = ImageGrab.grabclipboard()
    filename = time.strftime("%Y%m%d-%H%M%S", time.localtime())
    filename = filename+".png"
    print(filename)
    pic.save(filename)
    return filename

def set_clipboard(md_url):
    OpenClipboard()
    EmptyClipboard()
#    SetClipboardData(win32con.CF_TEXT, md_url)
    SetClipboardText(md_url)
    CloseClipboard()
    win32api.MessageBox(0, md_url, "Les1ie", 0x00001000)



if __name__ == "__main__":
    error = "error"
    try:
        filename = save_img()
        md_url = upload_img(bucket_name, filename)
        set_clipboard(md_url)
    except:
        set_clipboard(error)














