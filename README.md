# studentCheckIn

**水平有限，代码容错率低，为保障能正常运行，请严格按照教程进行部署**

### 1.获取推送key

> ​		*这一步是为信息推送功能准备所需材料，如果你已经有server酱或者企业微信应用，或者不需要推送功能，可跳过本步骤。*

​		要使用server酱进行推送，需先注册[server酱](https://sct.ftqq.com/)，之后按照提示获取send_key即可。

### 2. 创建云函数

> ​		进入使用的云函数网页，不同服务商配置界面稍有不同，这里以[阿里云](https://fcnext.console.aliyun.com/cn-hangzhou/services)为例。

**1.在服务列表选择创建服务**

![图片.png](https://s2.loli.net/2022/08/20/GPOrvC8WUjmw6Eu.png)

输入名称，描述，其他默认，点击确定

![图片.png](https://s2.loli.net/2022/08/20/uWF7X3C5nm1rTqt.png)

**2.在创建的服务中，点击创建函数**

![图片.png](https://s2.loli.net/2022/08/20/XBMfKksYwLVtFEa.png)

输入函数名称

![图片.png](https://s2.loli.net/2022/08/20/H2XiZu5QCfhylKY.png)

其他默认不要改动，到页面底部点击创建

**3.底部 终端 中输入以下代码后按回车，安装支持库**

```
pip3 install requests --upgrade -t .
```

![图片.png](https://s2.loli.net/2022/08/20/xv7yF8bJKwdoHes.png)

**4.将仓库文件中index.py中的代码添加（复制）到云函数的index.py文件中，其中原有代码无需改动**

![图片.png](https://s2.loli.net/2022/08/20/hrR12PcDxg84LAv.png)

**5.再将config.py、push.py文件复制到云函数中**

![图片.png](https://s2.loli.net/2022/08/20/dcxQvLRuVH4A1sz.png)

### 3.打卡资料配置

**1.打卡账号设置**

​		在云函数的config.py文件中，找到”打卡信息设置“代码段，依次填入以下内容（填到等号后面的单引号内）

- 学号

- 密码

![图片.png](https://s2.loli.net/2022/08/20/dcxQvLRuVH4A1sz.png)

**2.打卡地点设置**

​		位置同上，填入打卡地点经纬度[获取经纬度](https://lbs.qq.com/getPoint/#J)

**3.健康状况设置**

 	   默认为正常，如需修改，按照代码注释提示修改

### 4.推送通道配置

> 用于推送打卡结果，建议使用，防止程序出现问题造成打卡中断

**1.选择通道**

​		在config文件中找到”推送设置“代码段，在sendWay的等号后面输入选项，例：

```
#不推送
sendWay = 0
#server酱推送
sendWay = 1
#企业微信推送
sendWay = 2
#不支持多通道推送
```

**2.配置推送key**

​		根据所选推送方式，填写send_key或者corpid、corpsecret、agentid。

### 5.部署并测试

​		点击代码框上方“部署代码”或者“保存并部署”，部署成功后，点击“测试”。是否成功，可依据：小程序中未打卡状态是否变为已打卡、是否收到结果推送。如果失败，联系邮箱邮箱yujc666@com可能获取帮助。

![图片.png](https://s2.loli.net/2022/08/20/fn31wGeSlxF2DUR.png)

### 6.设置定时触发

​		**1.点击“触发器管理”**

![图片.png](https://s2.loli.net/2022/08/20/MfHgrm3PyZB1uLc.png)

**2.点击“创建触发器”**

![图片.png](https://s2.loli.net/2022/08/20/MfHgrm3PyZB1uLc.png)

**3.设置触发事件**

在弹出栏中，填写触发器名称，触发方式选择指定时间，指定时间框选择每日自动打卡时间，其他留空，点击“确定”完成创建。

![image-20220820151835629](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20220820151835629.png)

### 7.完成

**建议每天按时查看推送结果，防止出现问题导致当日未打卡。** 仅供学习交流，请勿商用。

**如果所在地发送改变，如返校或者返乡，请及时更改config.py中的经纬度，或者在自动打卡前手动打卡** 

**如果不再需要自动打卡，可直接删除云函数，简单粗暴。**

**万事开头难，不断尝试总能成功**

