#!/usr/bin/env/python
# -*- coding:utf-8 -*-
# Author:gx
from pathlib import Path
import json

''' 提取不同目录下的json文件中的字段数据'''

srcDir = 'D:/script_write/flows' #json文件目录
dstDir = 'D:/script_write/jyjgbh.txt' # 存放数据
# readDir = 'D:/script_write/jyjgbh.txt'  # 读旧文件
writeDir = 'D:/script_write/test.txt'  # 新建文件


def parse_dir(root_dir):
    path = Path(root_dir)  #将字符串路径转换为 Path 对象
    all_json_file = list(path.glob('**/vehicle.json')) #对路径下所有内容进行模式匹配并以生成器方式返回
    parse_result = []
    for json_file in all_json_file:
        #获取所在目录名称
        # service_name = json_file.parent.stem
        with json_file.open('rb') as f:
            json_result = json.load(f) #将json格式的字符转换为dict，从文件中读取
        # json_result["service_name"] = service_name
        parse_result.append(json_result)
    return parse_result


def write_result_in_file(write_path, write_content):
    with open(write_path,'w') as f:
        f.writelines("jyjgbh\n")
        for dict_content in write_content:
            jyjgbh = dict_content['jyjgbh']
            # service_name = dict_content['service_name']
            f.writelines(jyjgbh +"\n")


#删除重复项
def del_rep():
    lines_seen = set()
    outfile = open(writeDir, "w")
    f = open(dstDir, "r")
    for line in f:
        if line not in lines_seen:
            outfile.write(line)
            lines_seen.add(line)
    outfile.close()
    print("success")


def main():
    parse_result = parse_dir(srcDir)
    print(parse_result)
    write_result_in_file(dstDir,parse_result)
    del_rep()

if __name__ == '__main__':
    main()



