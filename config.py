#!/usr/bin/python3
# -*- coding: utf-8 -*-





##################打卡信息设置#################
#输入学号
studentid = ''
#输入密码
password = ''
#输入纬度
dimension = ''
#输入经度
longitude = ''
#健康状态(1为正常，2为异常)
healthStatus = '1'
#今日是否已做核算（1为是，2为否）
todayNuc = '1'
#十四天内是否经过中高风险地区（1为是，2为否）
isTravelHistory = '0'
#是否隔离（1为是，2为否）
isolation = '0'





##################推送设置#################
#选择你的推送方式（填入选项后的数字）：
sendWay = 0

#选项1：server酱
##填写server酱推送key
send_key = ''

#选项2：企业微信
##填写相关密钥
###企业id
corpid = ''
###secret
corpsecret = ''
###agentid
agentid = ''





import requests

url = 'https://ctsxx.gnway.org/xgxt-api/auth/mobileLogin'
headers = {"Host":"ctsxx.gnway.org","Connection":"keep-alive","Content-Length":"105","authorization":"","charset":"utf-8","User-Agent":"Mozilla/5.0 (Linux; Android 10; Redmi K30 Pro Build/QKQ1.191117.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.99 XWEB/3263 MMWEBSDK/20220303 Mobile Safari/537.36 MMWEBID/4518 MicroMessenger/8.0.21.2103(0x28001541) Process/appbrand0 WeChat/arm64 Weixin GPVersion/1 NetType/WIFI Language/zh_CN ABI/arm64 MiniProgramEnv/android","content-type":"application/json","Accept-Encoding":"gzip,compress,br,deflate","Referer":"https://servicewechat.com/wx1f9c0d3d1cad1cd7/21/page-frame.html"}
#获取token
def login(studentid,password):
    data = '{"username":"'+studentid+'","password":"'+password+'","roleName":"学生","openId":"oObP14iXWdWErW3h25XQ4tvYwvNM"}'
    x = requests.post(url,data=data.encode('utf-8'),headers=headers)
    x.close()
    return x.json()