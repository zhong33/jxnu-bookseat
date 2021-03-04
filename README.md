# 江西师范大学自习室抢座脚本

## 一、安装使用方法

```bash
git clone https://github.com/Yang-Zhongshan/jxnu-bookseat
cd jxnu-bookseat
pip3 install -r requirements.txt
python3 main.py
```

## 二、变量配置

按照要求填写好以下变量即可

```
num = 1             # 人数
roomId = "301"      # 房间号
duration = 15       # 使用时长（小时）
beginTime = 8       # 开始预约时间
username = ""       # 学号
password = ""       # 密码
```

## 三、系统接口

* 为方便大家更改，这里把用到的接口都给列了出来，参数看脚本即可
* 登录接口：`/api/1/login`
* 信息搜索接口：`/Seat/Index/searchSeats?LAB_JSON=1`
  * GET 是UID个人信息获取接口
  * POST 是座位获取接口
* 座位预定接口：`/Seat/Index/bookSeats?LAB_JSON=1`
* 预定信息接口：`/Seat/Index/myBookingList?LAB_JSON=1`

## 四、更新信息

#### 2021 - 03 - 04

发现BUG ：预定自习室不按照预期，似乎是会随机乱选，暂时没有找到问题所在

