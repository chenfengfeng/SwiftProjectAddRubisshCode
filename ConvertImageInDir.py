#!/usr/bin/env python
# _*_ coding:utf-8 _*_

# 当前文件夹下的图片转换，Xcode 中的图片压缩，换名，并且修改json中的文件名
# 创建.swift文件

import os
import PIL.Image as Image
import json

projectDir = '/Users/../Resources/Assets.xcassets'
# 屏蔽的文件夹
# 子文件夹 向这些文件夹中添加垃圾类
ignoreDirs = ['AppIcon.appiconset', "welcome_splash.imageset"]

# 所有图片添加的前缀，包括在json文件中filename添加的前缀
prefix = 'Prefix_'

# 图片压缩比例
quality = 90

# 所有图片路径
imgPaths = []

# 所有json文件路径
jsonPaths = []

# 获取所有文件夹
def searchDirFile(dir):
    listfile = os.listdir(dir)
    filepath = dir
    global imgPaths
    for file in listfile:  # 把目录下的文件都赋值给line这个参数
        if os.path.isdir(filepath + "/" + file):
            if file in ignoreDirs:
                break
            else:
                searchDirFile(filepath + '/' + file)
        else:
            fileAllPath = os.path.join(filepath, file)
            if file.endswith(".png"):
                imgPaths.append(fileAllPath)
                print(fileAllPath)
            if file.endswith("Contents.json"):
                jsonPaths.append(fileAllPath)
                print(fileAllPath)

# 压缩图片
def compareImage(filePath):
    img = Image.open(filePath)
    img.save(filePath, quality= quality)
    return

# 修改文件名
def changeImageName(fileAllPath):
    # 获取文件名和后缀
    (filepath, tempfilename) = os.path.split(fileAllPath);
    (shotname, extension) = os.path.splitext(tempfilename);
    newName = prefix + shotname
    newPath = filepath + "/" + newName + extension
    os.rename(fileAllPath, newPath)
    return

# 处理图片
def dealImages():
    for file in imgPaths:
        compareImage(file)
        changeImageName(file)


# 修改json文件中fileName
def dealJson():
    for file in jsonPaths:
        f = open(file, encoding='utf-8')
        dic = json.load(f)
        if 'images' in dic.keys():
            images = []
            imageData = dic['images']
            for image in imageData:
                if 'filename' in image.keys() and not image['filename'] is None:
                    filename = image['filename']
                    filename = prefix + filename
                    image['filename'] = filename
                    images.append(image)
                else:
                    images.append(image)

            print(images)
            dic['images'] = images
        newFile =  open(file, mode = 'w')
        jsonStr = json.dumps(dic,indent=4)
        newFile.write(jsonStr)


if __name__ == '__main__':
    searchDirFile(projectDir)
    dealImages()
    dealJson()