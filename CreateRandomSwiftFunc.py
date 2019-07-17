import random

# 产生一个satrtIndex到endIndex位长度的随机字符串
def getRandomStr(satrtIndex,endIndex):
    numbers = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    # random.choice()从列表中返回一个随机数
    final = (random.choice(numbers))
    # 从(50,100)列表中取出一个随机数
    index = random.randint(satrtIndex, endIndex)
    for i in range(index):
        final += (random.choice(numbers))
    return final



def addFunc(methodName):
    string = '    public func ' + methodName + 'TOVC() {\n\n       var realArr = Array<String>()\n'
    number = random.randint(5, 10)

    for i in range(1, number):
        start = random.randint(0, 10)
        end = random.randint(11,20)
        string += '       realArr.append("' + getRandomStr(start, end) + '")\n'

    string += '\n    }\n\n'
    return string

# 懒加载imgview
def addImageView(methodName):
    string = '    lazy var ' + methodName + 'Img'+ ': UIImageView = { \n'
    string += '        let img = UIImageView() \n'
    string += '        img.image = UIImage(named: "'  + getRandomStr(5, 8) + "_noicon" + '") \n'
    string += '        return img \n'
    string += '    }()\n\n'
    return string

# 懒加载Uilabel
def addUILabel(methodName):
    string = '    lazy var ' + methodName + 'Label'+ ': UILabel = { \n'
    string += '        let label = UILabel() \n'
    string += '        label.text = "' + getRandomStr(0, 5) + '_text" \n'
    string += '        return label \n'
    string += '    }()\n\n'
    return string

# 懒加载UIbutton
def addUIButton(methodName):
    string = '    lazy var ' + methodName + 'Button'+ ': UIButton = { \n'
    string += '        let button = UIButton(type: .custom) \n'
    string += '        return button \n'
    string += '    }()\n\n'
    return string

# 随机生成代码
def codeStr(methodName):
    i = random.randint(10, 15)
    index = i % 4
    if index == 0:
        return addFunc(methodName)
    elif index == 1:
        return addUILabel(methodName)
    elif index == 2:
        return addUIButton(methodName)
    else:
        return  addImageView(methodName)