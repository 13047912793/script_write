#!/usr/bin/env/python
# -*- coding:utf-8 -*-
# Author:gx

import os

'''批量修改目录名'''
i = 1
path = 'D:/script_write/flows/'
for dirPath, dirName, fileName in os.walk(path):  #遍历一个目录内各个子目录和文件
    for names in dirName:
        # print(names)
        old_name = os.path.abspath(os.path.join(dirPath, names ))
        # print(old_name)
        new_name = os.path.abspath(os.path.join(dirPath, str(i).zfill(3)))
        os.renames(old_name, new_name)  #old_name 要修改的文件名或目录  new_name修改后的目录或文件名
        i = i + 1

