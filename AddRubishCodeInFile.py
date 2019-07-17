# -*- coding: utf-8 -*-

# 向现有代码中添加垃圾代码

import os
import CreateRandomSwiftFunc
import random

# 获取文件中 static func createInstance( 的总数量
def GetMFileKeyStrCount(file_path,old_str):
    file_data = ""
    Ropen=open(file_path,'r')#读取文件
    # 只在ViewController中加
    isViewController = False
    isHaveKeyStr = False
    for line in Ropen:
        if "BaseViewController" in line:
            isViewController = True
        if old_str in line:#如果.h文件中的某一行里包含old_str,则往这一行添加一下语句
            isHaveKeyStr = True
        if isViewController == True and isHaveKeyStr == True:
            print('filePath------' + file_path)
            return  True
    return False

#.swift文件添加垃圾代码
def MFileAddCode(file_path,old_str):

    file_data = ""
    print('filePath------'+file_path)
    Ropen=open(file_path,'r')#读取文件
    flagCount = 0
    for line in Ropen:
        if old_str in line:
            # 在 'keyStr' 前面加上垃圾代码
            file_data += rubishCode()
            file_data += line
        else:
            file_data += line
    Ropen.close()
    Wopen=open(file_path,'w')
    Wopen.write(file_data)
    Wopen.close()

# 生产垃圾代码
def rubishCode():
    # 获取个随机数，从而生成几个类名
    methodArray = []
    number = random.randint(5, 10)
    for i in range(1, number):
        start = random.randint(0, 10)
        end = random.randint(11,20)
        methodName = CreateRandomSwiftFunc.getRandomStr(start, end)
        methodArray.append(methodName)

    methodArray = list(set(methodArray))  # 数组去重

    line = ''
    for name in methodArray:
        line += CreateRandomSwiftFunc.codeStr(name)
    return line

def addCode(file_path):
    global codeCount
    if '.swift' in file_path:  # file_dir+'/'+file含义是file_dir文件夹下的file文件
        # 在keyStr上添加垃圾代码
        if GetMFileKeyStrCount(file_path, keyStr) == True:
            MFileAddCode(file_path, keyStr)


# 循环递归遍历文件夹
def traverse(file_dir):
    fs = os.listdir(file_dir)
    for dir in fs:
        tmp_path = os.path.join(file_dir, dir)
        if not os.path.isdir(tmp_path):
            addCode(tmp_path)
        else:
            # 是文件夹,则递归调用
            traverse(tmp_path)


def addRubbish():
    global codeCount
    # 每个文件中添加的代码数量
    codeCount = 5
    # 主工程目录
    projectDir = '/Users/../Project/'
    # 要添加垃圾代码文件所在的文件夹路径
    subDirs = ['AddDevice', "Alarm", "Device", 'DeviceList', "Home", "Login", "Mine", "Smart"]
    # 全局替换的关键字符串
    global keyStr
    keyStr = 'static func createInstance('
    for dir in subDirs:
        file_dir = projectDir + dir
        traverse(file_dir)

def main():
    addRubbish()

if __name__ == '__main__':
    main()
