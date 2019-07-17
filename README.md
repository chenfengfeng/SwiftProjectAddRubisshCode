### SwiftProjectAddRubisshCode

> 本项目针对Swift项目，在项目中添加垃圾代码，添加垃圾类，修改项目指定文件夹下的图片加前缀并且在Conten.json中的filename添加前缀。



* CreateRandomSwiftFunc

​         本文件生成垃圾方法

* CreateRubbishClass

  本文件创建垃圾类。

  修改createFileDir方法中的projectDir（主目录）、subDirs（子目录集合），随机向目录中的子目录创建垃圾类，创建完成后需要收到把文件添加到工程中。

* AddRubishCodeInFile

  本文件是像现有类（BaseViewController 自定义的类）中添加垃圾代码。

  修改addRubbish方法中的projectDir（主目录）、subDirs（子目录集合），keyStr是关键字符串，即在搜索主目录下的子目录中集成自BaseViewController的类，并且包含关键字符串，在关键字符串前添加垃圾代码。

* ConvertImageInDir

  本文件是修改Xcode中的图片资源脚本。

  projectDir是图片文件夹位置，ignoreDirs忽略的子文件夹名称。

  prefix是添加的前缀，quality是图片压缩比例

  