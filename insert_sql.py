#!/usr/bin/env/python
# -*- coding:utf-8 -*-
# Author:gx
from pathlib import Path
import json
import pymysql.cursors
"""数据库批量插入数据"""
connect = pymysql.Connect(
        host='192.168.9.141',
        port=3306,
        user='root',
        passwd='abc123!%!',
        db='vehicle_insp',
        charset='utf8'
    )
cursor = connect.cursor()

srcDir = 'D:/python_project/liuzhou' #json文件目录
path = Path(srcDir)  #将字符串路径转换为 Path 对象
all_json_file = list(path.glob('**/vehicle.json')) #对路径下所有内容进行模式匹配并以生成器方式返回
parse_result = []
for json_file in all_json_file:
    with json_file.open('rb') as f:
        json_result = json.load(f) #将json格式的字符转换为dict，从文件中读取
        # json_result["service_name"] = service_name
        parse_result.append(json_result)
lsts = []
for item in parse_result:
    for key in item:
        jyjgbh = item["jyjgbh"]
        lsts.append(jyjgbh)
jy = set(lsts)
# print(jy)
for i in jy :
    sql = "INSERT INTO organization_v2 (parent_id, jyjgbh, name, province, city, district, jian_yan_enabled) VALUES ( '%s', '%s', '%s', '%s','%s', '%s', '%s')"
    data = ('100139', '{}'.format(i), '柳州组织', '110000,北京', '110100,北京市', '110114,昌平区', '1')
    cursor.execute(sql % data)
    connect.commit()
    print('成功插入', cursor.rowcount, '条数据')















