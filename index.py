#!/usr/bin/python3
# -*- coding: utf-8 -*-

import requests
import config
import push

resp = config.login(config.studentid,config.password)
token = resp["token"]
url = 'https://ctsxx.gnway.org/xgxt-api/api/clockIn/clockInList'
data = '{"dimension":"' + config.dimension + '","longitude":"' + config.longitude + '","studentId":"' + config.studentid + '","addressRemark":"","bodyTemperature":"","todayNuc":"' + config.todayNuc + '","isTravelHistory":"' + config.isTravelHistory + '","healthStatus":"' + config.healthStatus + '","isolation":"' + config.isolation + '","clockInTime":"","clockInAddress":"","studentName":"","isTravelHistory2":"' + config.isTravelHistory2 + '","isResponsible":"1"}'
headers = {
    "Host":"ctsxx.gnway.org",
    "Connection":"keep-alive",
    "Content-Length":"371",
    "authorization":token,
    "charset":"utf-8",
    "User-Agent":"Mozilla/5.0 (Linux; Android 10; Redmi K30 Pro Build/QKQ1.191117.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.99 XWEB/3263 MMWEBSDK/20220303 Mobile Safari/537.36 MMWEBID/4518 MicroMessenger/8.0.21.2103(0x28001541) Process/appbrand0 WeChat/arm64 Weixin GPVersion/1 NetType/WIFI Language/zh_CN ABI/arm64 MiniProgramEnv/android",
    "content-type":"application/json",
    "Accept-Encoding":"gzip,compress,br,deflate",
    "Referer":"https://servicewechat.com/wx1f9c0d3d1cad1cd7/25/page-frame.html"}

def main():
    response = requests.post(url,data=data.encode('utf-8'),headers=headers)
    if response.text == 'true':
        message = resp['user']['user']['nickName'] + resp['user']['user']['username'] + ' 打卡成功！'
        push.send(message)
    else:
        message = resp['user']['user']['nickName'] + resp['user']['user']['username'] + ' 打卡失败！' + errorReason()
        push.send(message)
    print (response.text)


def errorReason():
    url = 'https://ctsxx.gnway.org/xgxt-api/api/clockIn/clockInList/isClockIn?xh=' + config.studentid
    headers = {"authorization":token}
    if requests.get(url , headers = headers).text == '1':
        message = ' 今日已打卡！'
    else:
        message = ' 未知错误'
    return message
main()

