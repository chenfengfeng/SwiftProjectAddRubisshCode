#!/usr/bin/env python
# _*_ coding:utf-8 _*_

# 创建垃圾代码
# 创建.swift文件

import random
import CreateRandomSwiftFunc

import os, sys

import string


# 属性类型
classArray = ['UIColor', 'UILabel', 'UITableView', 'UISlider', 'UIScrollView', 'UIView', 'UIButton']

#垃圾文件夹
rubbishFile = 'NewRubCode'

# 创建swift 文件
def createSwift(fileNmae, propertyNumber, methodArray):
    full_path = createFileDir() + fileNmae + '.swift'

    file = open(full_path, 'w')

    file.write(
        '//\n//  ' + fileNmae + '.swift\n//  LinkMall\n\n//  Created by geyl on 2019/7/7.\n//  Copyright © 2019年 OneThing Ltd. All rights reserved.\n//\n\n')

    file.write('import UIKit \n\n' + 'class ' + fileNmae + ': UIViewController {\n\n')

    propryNameArray = []

    for index in range(1, propertyNumber):
        propryNameArray.append(random.choice(classNameArray))

    propryNameArray = list(set(propryNameArray))

    for propertyName in propryNameArray:
        file.write('    public var ' + propertyName + ':' + random.choice(classArray) + '!\n')

    file.write('\n\n')

    file.write('    override func viewDidLoad() {\n        super.viewDidLoad()\n    }\n\n')

    for methodName in methodArray:
        file.write(CreateRandomSwiftFunc.codeStr(methodName))

    file.write('}')

    file.close()

    print('Done')

# 获取创建的文件目录
def createFileDir():
    # 工程目录
    projectDir = '/Users/justdoitge/Desktop/Work/WOZAIIOT/iOS/Customer/AlaazSmartHome/AlaazSmartHome'
    # 子文件夹 向这些文件夹中添加垃圾类
    subDirs = ['AddDevice', "Alarm", "Device", 'DeviceList', "Home", "Login", "Mine", "Smart"]
    i = random.randint(1, 15)
    index = i % 8
    subDir = subDirs[index]
    full_path = projectDir + '/' + subDir + '/'
    return full_path

# 创建swift 文件名
def createClassName():
    first = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    second = "abcdefghijklmnopqrstuvwxyz"

    index = 0

    array = []

    # 设置生成多少个类
    classNumber = 200
    for i in range(classNumber):

        final = (random.choice(first))
        # 字符串长度
        index = random.randint(10, 15)

        for i in range(index):
            final += (random.choice(second))

        final += (random.choice(first))

        for i in range(index):
            final += (random.choice(second))

        array.append(final)
    return array

def main():

    global classNameArray
    array = createClassName()

    classNameArray = list(set(array))

    for name in classNameArray:

        number = random.randint(10, 15)

        methodArray = []

        for i in range(30, 50):
            methodArray.append(random.choice(classNameArray))

        methodArray = list(set(methodArray))  # 数组去重

        createSwift(name + 'VController', number, methodArray)

if __name__ == '__main__':
    main()
