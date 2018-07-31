#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import random

import output as output
import pymysql
import time
import datetime
import qrcode
from PIL import Image
import sys

print("请输入需要生成二维码的数量：")
word = input()
# print(sys.argv[0])
print(word)


#初始化：标准机编号，01，
deviceNO = {
    'standard':'01',
    'smart':'02',
}

#二维码初始化
qr = qrcode.QRCode(version=5,error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=8,border=4)

#获取当前日期和时间
local_datetime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
print(local_datetime)

#设备ID生成规则：机型代码数字编号（01：标准立式机；02：智能立式机）+创建时间戳后8位+2位随机数+Device表自增ID

#获取当下时间戳
t = time.time()
time_stamp_8 = str(int(t))[0:8]
print(time_stamp_8)
# 2位随机数
num_2 = random.randint(10,99)
print(num_2)

#打开数据库连接

db = pymysql.connect("39.108.217.228","baymin","baymin1024!@#$%","waterever.water")

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

#插入记录数量
count = int(word);
#二维码数据数组
arr = []
while count > 0:
    # 使用 execute()  方法执行 SQL 查询

    sql_str = "select DeviceId from Device order by DeviceId desc limit 1 "
    cursor.execute(sql_str)
    deviceID = cursor.fetchall()
    # print("deviceID is %s", deviceID[0])
    deviceid = 0;
    for row in deviceID:
        deviceid = int(row[0])

    print("deviceid is ", deviceid + 1)

    deviceCode = deviceNO.get('standard') + time_stamp_8 + str(num_2) + str(deviceid + 1)
    print('devicecode is ', deviceCode)

    cursor.execute("INSERT INTO Device(DeviceID,DeviceCode,DateCreated) values('%s','%s','%s')" % (
    str(deviceid + 1), deviceCode, local_datetime))
    # 使用 fetchone() 方法获取单条数据.
    data = cursor.fetchall()
    # num = cursor.rowcount       #rowcount,只读属性，并返回执行execute()方法后影响的行数

    db.commit()

    count = count - 1

    arr.append(deviceCode)
# 关闭数据库连接
db.close()

qr = qrcode.QRCode(version=5, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=8, border=4)
# arr = ["A","B"]
for data in arr:
    # # 创建DeviceCode二维图
    # createQRImage(deviceCode)

    qr.clear()
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image()
    img = img.convert("RGBA")

    icon = Image.open("/Users/xianminchen/PycharmProjects/untitled1/icon.png")

    img_w, img_h = img.size
    factor = 4
    size_w = int(img_w / factor)
    size_h = int(img_h / factor)

    icon_w, icon_h = icon.size
    if icon_w > size_w:
        icon_w = size_w
    if icon_h > size_h:
        icon_h = size_h
    icon = icon.resize((icon_w, icon_h), Image.ANTIALIAS)

    w = int((img_w - icon_w) / 2)
    h = int((img_h - icon_h) / 2)
    icon = icon.convert("RGBA")
    img.paste(icon, (w, h), icon)
    # img.show()
    filename = data + ".png"
    img.save('/Users/xianminchen/PycharmProjects/untitled1/QRImages/' + filename)
    print(filename + "---" + data)