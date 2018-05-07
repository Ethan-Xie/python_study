

import os

# 提供对操作系统进行调用的接口
os.getcwd() #获取当前目录，当前python脚本工作的目录路径
os.chdir("dirname")  #改变当前工作目录：相对于shell下的cd
os.curdir  #返回当前目录：（‘.’）
os.pardir  #获取当前目录的父目录字符串名（“..”）
os.makedirs('dirname1/dirname2')  #可生成多层递归目录
os.removedirs('dirname1')  #若目录为空，删除，并递归上一目录
os.mkdir('dirname')  #生成单级目录
os.listdir('dirname')   #列出目录下的所有文件和子目录
os.remove()   #删除一个文件
os.rename("oldname",'newname')  #重命名文件/目录
os.stat('path/filename')   # 获取文件/目录


os.sep    # 输出操作系统特定的路径分隔符，win下为"\\",Linux下为"/"
os.linesep    # 输出当前平台使用的行终止符，win下为"\t\n",Linux下为"\n"
os.pathsep    # 输出用于分割文件路径的字符串
os.name    # 输出字符串指示当前使用平台。win->'nt'; Linux->'posix'
os.system("bash command")  # 运行shell命令，直接显示
os.environ   #获取系统环境变量
path="/hello"
os.path.abspath(path)   #返回path规范化的绝对路径
os.path.split(path)   #将path分割成目录和文件名二元组返回
os.path.dirname(path)   #返回path的目录。其实就是os.path.split(path)的第一个元素
os.path.basename(path)   #返回path最后的文件名。如何path以／或\结尾，那么就会返回空值。即os.path.split(path)的第二个元素
os.path.exists(path)   #如果path存在，返回True；如果path不存在，返回False
os.path.isabs(path)   #如果path是绝对路径，返回True
os.path.isfile(path)   #如果path是一个存在的文件，返回True。否则返回False
os.path.isdir(path)   #如果path是一个存在的目录，则返回True。否则返回False
#os.path.join(path1[, path2[, ...]])   #将多个路径组合后返回，第一个绝对路径之前的参数将被忽略
os.path.getatime(path)   #返回path所指向的文件或者目录的最后存取时间
os.path.getmtime(path)   #返回path所指向的文件或者目录的最后修改时间

# a =os.system("dir").read()   可以在命令行中显示出来
# 直接打印a会 为0
os.popen("dir").read()

# shutil  高级文件，文件夾，压缩包，处理模块


#_*_coding:utf-8_*_
__author__ = 'Alex Li'

#import time
import  random
#生成随机验证码
checkcode = ''
for i in range(4):
    current = random.randrange(0,4)
    if current != i:
        temp = chr(random.randint(65,90))
    else:
        temp = random.randint(0,9)
    checkcode += str(temp)
print('checkcode')

# system
import sys
sys.argv           命令行参数List，第一个元素是程序本身路径
sys.exit(n)        退出程序，正常退出时exit(0)
sys.version        获取Python解释程序的版本信息
sys.maxint         最大的Int值
sys.path           返回模块的搜索路径，初始化时使用PYTHONPATH环境变量的值
sys.platform       返回操作系统平台名称
sys.stdout.write('please:')
val = sys.stdin.readline()[:-1]

# shelve模块是一个简单的k,v将内存数据通过文件持久化的模块，可以持久化任何pickle可支持的python数据格式
import shelve
d = shelve.open('shelve_test')  # 打开一个文件

class Test(object):
    def __init__(self, n):
        self.n = n

t = Test(123)
t2 = Test(123334)
name = ["alex", "rain", "test"]
d["test"] = name  # 持久化列表
d["t1"] = t  # 持久化类
d["t2"] = t2  #可以通过 t1 t2 获取  a.get("t1")
d.close()

# xml 处理模块
import xml.etree.cElementTree as ET
tree = ET.parse("xmltest.xml")
root = tree.getroot() # 根结点
print(root.tag)

# 遍历 xml 文档
for child in root:
    print(child.tag,child.attrib)
    for i in child:
        print(i.tag,i.text)

# print(time.clock()) #返回处理器时间,3.3开始已废弃 , 改成了time.process_time()测量处理器运算时间,不包括sleep时间,不稳定,mac上测不出来
# print(time.altzone)  #返回与utc时间的时间差,以秒计算\
# print(time.asctime()) #返回时间格式"Fri Aug 19 11:14:16 2016",
# print(time.localtime()) #返回本地时间 的struct time对象格式
# print(time.gmtime(time.time()-800000)) #返回utc时间的struc时间对象格式

# print(time.asctime(time.localtime())) #返回时间格式"Fri Aug 19 11:14:16 2016",
#print(time.ctime()) #返回Fri Aug 19 12:38:29 2016 格式, 同上



# 日期字符串 转成  时间戳
# string_2_struct = time.strptime("2016/05/22","%Y/%m/%d") #将 日期字符串 转成 struct时间对象格式
# print(string_2_struct)
# #
# struct_2_stamp = time.mktime(string_2_struct) #将struct时间对象转成时间戳
# print(struct_2_stamp)



#将时间戳转为字符串格式
# print(time.gmtime(time.time()-86640)) #将utc时间戳转换成struct_time格式
# print(time.strftime("%Y-%m-%d %H:%M:%S",time.gmtime()) ) #将utc struct_time格式转成指定的字符串格式





#时间加减
import datetime

# print(datetime.datetime.now()) #返回 2016-08-19 12:47:03.941925
#print(datetime.date.fromtimestamp(time.time()) )  # 时间戳直接转成日期格式 2016-08-19
# print(datetime.datetime.now() )
# print(datetime.datetime.now() + datetime.timedelta(3)) #当前时间+3天
# print(datetime.datetime.now() + datetime.timedelta(-3)) #当前时间-3天
# print(datetime.datetime.now() + datetime.timedelta(hours=3)) #当前时间+3小时
# print(datetime.datetime.now() + datetime.timedelta(minutes=30)) #当前时间+30分


#
# c_time  = datetime.datetime.now()
# print(c_time.replace(minute=3,hour=2)) #时间替换