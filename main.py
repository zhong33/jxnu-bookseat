# -*- coding:utf-8 -*- 
import requests
import time

class User(object):
    def __init__(self, username, password, beginTime, duration, num, category_id, content_id):
        self.num = num
        self.username = username
        self.password = password
        self.duration = duration
        self.beginTime = beginTime
        self.content_id = content_id
        self.category_id = category_id
        self.session = requests.session()
        self.baseurl = "https://jxnu.huitu.zhishulib.com"
        self.headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Safari/537.36"}

    def login(self):
        url = self.baseurl + "/api/1/login"
        data = {"login_name" : self.username, "password":self.password, "code":"ffbd865eac7819dd0a1c31e6e094c10b", "str":"frSfG6mXFAHbtGp1", "org_id":"142", "_ApplicationId":"lab4", "_JavaScriptKey":"lab4", "_ClientVersion":"js_xxx", "_InstallationId":"16868084-6faa-25e2-6fde-97a73d4b5e09"}
        res = self.session.post(url, json=data, headers=self.headers)
        if (res.status_code == 200):
            print("[+] 登录成功！")
        else:
            print("登录失败，账号或密码错误！")

    def searchSeats(self):
        url1 = self.baseurl + "/Seat/Index/searchSeats?LAB_JSON=1"
        url2 = self.baseurl + "/Seat/Index/searchSeats?space_category[category_id]=%d&space_category[content_id]=%s&LAB_JSON=1"%(self.category_id,self.content_id)
        data = {"beginTime":self.beginTime, "duration":self.duration, "num":self.num, "space_category%5Bcategory_id%5D":self.category_id, "space_category%5Bcontent_id%5D":self.content_id}
        res2 = self.session.get(url2, headers=self.headers).json()
        res1 = self.session.post(url1, data=data, headers=self.headers).json()
        self.seat = res1["data"]["bestPairSeats"]["seats"][0]["id"]
        self.uid = res2["data"]["uid"]

    def bookSeats(self):
        url = self.baseurl + "/Seat/Index/bookSeats?LAB_JSON=1"
        data = {"beginTime":self.beginTime, "duration":self.duration, "seats[0]":self.seat, "seatBookers[0]":self.uid}
        res = self.session.post(url, data=data, headers=self.headers).json()
        if (res["CODE"] == "ok"):
            print("[+] 预约中......")
        else:
            print("[+] 预约失败")

    def getInfo(self):
        url = self.baseurl + "/Seat/Index/myBookingList?LAB_JSON=1"
        res = self.session.get(url, headers=self.headers).json()
        bookTime = int(res["content"]["defaultItems"][0]["time"])
        beginTime = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(bookTime))
        endTime = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(bookTime + int(res["content"]["defaultItems"][0]["duration"])))
        seatNum = res["content"]["defaultItems"][0]["seatNum"]
        roomName = res["content"]["defaultItems"][0]["roomName"]
        print("[+] 已为您成功预约" + roomName + "(" + roomId + ") " + seatNum  + "号座位，预约时间为" + beginTime + " ~ "  + endTime + "，请及时签到哦！")

def calcBeginTime(beginTime):
    hour = time.localtime().tm_hour
    if (hour >= 22):
        tomorrowZero = int(time.mktime(time.strptime(time.strftime("%Y-%m-%d", time.localtime(int(time.time()))), "%Y-%m-%d"))) + 86400
        return tomorrowZero + beginTime*3600
    else:
        todayZreo = int(time.mktime(time.strptime(time.strftime("%Y-%m-%d", time.localtime(int(time.time()))), "%Y-%m-%d")))
        return todayZreo + beginTime*3600

def calcDuration(duration):
    return 3600 * duration

def calcRoomId(roomId):
    room = {"201":"36", "202":"35", "301":"31", "302":"37", "604":"60", "406":"59", "402":"58"}
    return room[roomId]

if __name__ == '__main__':
    num = 1             # 人数
    roomId = "301"      # 房间号
    duration = 15       # 使用时长（小时）
    beginTime = 8       # 开始预约时间
    username = ""       # 学号
    password = ""       # 密码
    category_id = 591
    User = User(username,password,calcBeginTime(beginTime),calcDuration(duration),num,category_id,calcRoomId(roomId))
    User.login()
    User.searchSeats()
    User.bookSeats()
    User.getInfo()