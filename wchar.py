# -*- coding:utf-8 -*-
import itchat
import requests

url = "http://www.tuling123.com/openapi/api"
# key = "ba20bfd1410e4b41a026ad9ef84946d2"
key = '720b8495c39f40ac92284c5d6b3d1dd7'

@itchat.msg_register("Text")
def text_reply(msg):
    return get_reply(msg["Text"])


def get_reply(msg):
    print(msg)
    repson = requests.post(url + "?key=" + key + "&info=" + msg).json()
    print(repson)
    return repson.get("text")


# itchat.auto_login(hotReload=True)
itchat.auto_login()

itchat.run()
