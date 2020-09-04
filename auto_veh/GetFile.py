import os
import shutil

'''提取不同目录下的相同文件到一个新建文件夹'''
j = 96
for i in range(20081013000600735200, 20081013000600735250):  # 遍历一个文件夹下的文件范围
    i = str(i)
    s = i.zfill(20)  # 保留三位有效位
    fir = s
    oldPath = 'D:/script_write/flows2/' + fir   # 读取文件夹需要提取的文件
    newPath = 'D:/script_write/0205/'
    imgName = '0205'
    if os.path.isdir(oldPath):      #判断是否有该目录

        file_list = os.listdir(oldPath)
        for allDir in file_list:
            if '0201' in str(allDir):
                # 如果图像名为0296 则将0296复制到'D:/script_write/picture/'
                imgPath = os.path.join(oldPath, imgName)
                newTargetPath = newPath +'环保检验合格标志背面' + str(j).zfill(4) + '.jpg'
                shutil.copyfile(imgPath, newTargetPath)#imgPath, newTargetPath都需是文件名,如果newTargetPath存在或无权限，会抛出异常
                j += 1
                # print(j)
            else:
                print(fir + "该目录不存在0205")

    else:
        continue