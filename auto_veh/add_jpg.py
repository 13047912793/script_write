#!/usr/bin/env/python
# -*- coding:utf-8 -*-
# Author:gx

import os

'''批量增加不同目录下的图片后缀.jpg'''

path = 'D:/script_write/flows/'
for dirPath, dirName, fileName in os.walk(path):  #遍历一个目录内各个子目录和文件
    for files in fileName:
        if os.path.splitext(files)[1] not in ['.json', '.txt']:  #分离文件名和扩展名（后缀名）
            newFiles = files + '.jpg'
            # print(dirPath)
            old_name = os.path.abspath(os.path.join(dirPath, files ))
            new_name = os.path.abspath(os.path.join(dirPath, newFiles))
            os.renames(old_name, new_name)  #old_name 要修改的文件名或目录  new_name修改后的目录或文件名













