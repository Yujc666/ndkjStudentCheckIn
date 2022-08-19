#!/usr/bin/python3
# -*- coding: utf-8 -*-
import requests
#import json
import config

def sctapi_send(key,title,desp):
    url = "https://sctapi.ftqq.com/" + key + ".send?title=" + title + "&desp=" + desp
    response = requests.post(url)

def wechat_send(corpid,corpsecret,agentid,content):
    url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=" + corpid + "&corpsecret=" + corpsecret
    token = (requests.get(url).json().get("access_token"))
    def send_message(content):
        data = '{"touser": "@all","msgtype": "text","agentid": "' + agentid + '","text": {"content": "'+ content + '"},"safe": 0}'
        url = "https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=" + token
        response = requests.post(url,data=data.encode('utf-8'))
    send_message(content)

def send(message:str):
    if config.sendWay == 1:
        sctapi_send(config.send_key,'打卡结果：',message)
    elif config.sendWay == 2 :
        wechat_send(config.corpid,config.corpsecret,config.agentid,message)
    else:
        print("未选择推送方式或者选项出现问题")