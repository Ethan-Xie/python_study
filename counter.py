
l = ['',]

# 不常用  import collections
# counter 模型  计数器
import collections
obj = collections.Counter('abbdbdkknfkdkffknf')

print(obj) #Counter({'k': 5, 'f': 4, 'b': 3, 'd': 3, 'n': 2, 'a': 1})
print(obj.most_common(4))   #前四位[('k', 5), ('f', 4), ('b', 3), ('d', 3)]

# 循环获取

# 循环获取
for k in obj.elements():
    print(k)
    for k,v in obj.items():
        print(k,v)

obj = collections.Counter(['11','11','11','11',])  # 列表也行 Counter({'11': 4})
print(obj)
obj.update(['eric','12']) #Counter({'11': 4, 'eric': 1, '12': 1})
print(obj)
obj.subtract(['eric','12']) #Counter({'11': 4, 'eric': 0, '12': 0})
obj.subtract(['eric','12']) # Counter({'11': 4, 'eric': -1, '12': -1})
print()

# 有序字典 有序方法
# 字典dic  'k1':'v1'  ‘k10’:'v10'
#  列表li  k1   ...   k10

dic={}
dic['k1']='v1'
dic['k2']='v2'
dic['k3']='v3'
dic['k4']=None
li=['k1','k2']
dic.setdefault('k4','66')
dic.update({'k4','66'})
for  i in li:
    print(dic[i])

# 默认字典 defaultdict
dic={'k1':[] }
dic['k1'].append('alex')

# 可命名元祖（）  [] {}

# 与上面对比
dic = collections.defaultdict(list)
dic['k1'] .append('alex')
print(dic)

# 昨晚 end

t =(11,22,33,44)

import  collections
#//创建类
MytupleClass = collections.namedtuple('MytupleClass',['x','y','z'])
print(help(MytupleClass))  # 提供的方法
# asdict 字典 x= y=
# replace 指定某个人
obj = MytupleClass(11,22,33)
print(obj.x)
print(obj.y)
print(obj.z)


# python 双向队列  deque
#单向队列  先进先出  双向队列
# 双向队列  appendleft  clear 清除   count 计数
# extend

d = collections.deque()
d.append('1')
d.append('12')
d.append('1')
print(d)  #deque(['1', '12', '1'])
print(d.count('1'))  # 2

d.extend(['aa','bb','cc'])
d.extendleft(['aa','bb','cc'])
print(d)   #deque(['1', '12', '1', 'aa', 'bb', 'cc'])
print(d.index('cc'))  #0 第零个位置
d.rotate(1)
print(d)  #循环走一个 位置

# d = collections.deque()
#单向队列
import queue
# 创建单向
q = queue.Queue()
q.put('123')
q.put('456')
# 相对应
res=q.get()  # 123
print(res)  # 1
print(q.qsize()) # 变为1


#next end

# python 深浅拷贝原理

# 内存地址
import copy
# 浅拷贝
#copy.copy()
#copy.deepcopy()  #深拷贝

# 基本类型：字符串 ，数字
a1=123123
a2=123123
a3=copy.deepcopy(a1)
a3=copy.copy(a1)
print(id(a1))   # 39122976
print(id(a2))   # 39122976
print(id(a3))   # 7272512  深浅拷贝都一样

# 其他，元祖，列表，字典

n1= {"k1":"wu","k2":123,"k3":["alex",456]}
n2=n1  #两者地址一样

n2=copy.copy(n1)  #两者地址不一样
print(id(n1))
print(id(n2))

print(id(n1['k3']))  # 里面的值 地址是一样的
print(id(n2['k3']))  #

# 应用
# 字典
dic ={
        "cpu":[80,],
        "mem":[80,],
        "disk":[80,]
      }

print(dic)
new_dic=copy.copy(dic)
new_dic['cpu'][0] = 50
print(dic)
print(new_dic)   # 浅拷贝 深拷贝

# 函数的学习
def word(param,arg=999):
    print(param)
    n=123
    print(n+1)
    return  "return_val"   # 跳出函数，函数不能重名
    print("b")  # 不会输出

res = word('hello','args')
print(res)  # 如果没返回值，则为 none

# * 号的用法：  time:2018.3.25
def show(*arg):
    print(arg,type(arg)) #(1, 22, 33, 44, 67, 78) <class 'tuple'>

def show2(**arg):
    print(arg,type(arg)) #(1, 22, 33, 44, 67, 78) <class 'tuple'>

show(1,22,33,44,67,78)  #揉 成一个元组
show2(n1=98,n2=123)  #揉 成一个字典 {'n1': 98} <class 'dict'>  {'n1': 98, 'n2': 123} <class 'dict'>

def show3(*arg,**kwargs):
    print(arg,type(arg)) #(1, 2, 3) <class 'tuple'>

    print(kwargs, type(kwargs)) # {'n1': 98, 'n2': 123} <class 'dict'>

show3(1,2,3,n1=98,n2=123) #一个元祖，一个字典
l=[1,2,3,4]
d = {'n1':88,'alex':"hello"}
show3(*l,**d)  #自定义  (1, 2, 3, 4) <class 'tuple'>   {'n1': 88, 'alex': 'hello'} <class 'dict'>

# 动态参数，字符串格式化：  time:2018.3.26

s = "{0} is {1}"
l = ['alex',"sb"]
res=s.format('alex','ab')  #alex is ab
res = s.format(*l)  # a lex is sb

s1 = "{name} is {acter}"
res = s1.format(name="xiejisen",acter="nb")  #xiejisen is nb
t={'name':"xiejisen",'acter':"no1"}
res = s1.format(**t)  #xiejisen is no1
print(res)

# python lamnda 表达式
def func(a):
    a+=1
    return  a
res=func(4)  #5
l=[]  # l=list()
# 函数内容 a+1 并把结果return
funct = lambda a: a+1  # 和上面效果一致
res=funct(8)  #9
print(res)

# 内置函数； 2018.3.26

res=all([1,])   #全部为真，才为真
print(res)

res=any([1,""])   #一个为真，就为真
res=any([1,"",[],{},None,1]) #true
print(res)
class Fun:
    def __repr__(self):
        return 'xie'

f=Fun()
res=ascii(f)  #执行那个方法  如果是8的话，可以调用 int的repr 方法

res = bin(10)  #0b1010 二进制
res = bytearray("谢",encoding="utf-8")  #bytearray(b'\xe8\xb0\xa2')
print(res)

#内置函数    2018.3.27

f = lambda x:x+1
print(f(5))

l=[]
# l() 会报错
print(callable(l))  # 检测上面那个现象

# ord() chr()  是对应的  数字转成 字符

import  random
res = random.randint(1,99)
print(res)

#
li = ['x','j','s']  #列表，增加
for i in li:
    print(li) #循环三个

for i in li:
    print(i)

for i,item in enumerate(li,1):
    print(i,item)

print(eval("6*8"))

li = [1,3,4,]
new_li =map(lambda x:x+100,li)
print(list(new_li))  #[101, 103, 104]

def test1(x):
    if x>3:
        return True
    else:
        return False

new_li = filter(test1,li)  #只有true 是才通过
print(list(new_li))

format(7)  # int 中的__format__
hex(100)  # 16进制
max(11,22,33)
print(range(0,10000))
round(8.9)  #四舍五入
li[1:9]  #切片

# #内置函数    2018.3.28
print(dir())
print(vars())

f=open('test.log','r',encoding='utf-8')  #r+b 二进制  r+ 字符
#print(f.seek(1))   #获取指针 位置  起始指针，会报错
res = f.read(1)  #python 按字符去读  第
print(f.tell()) #获取文件中对的指针位置 3
# f.truncate()
f.close()
#print(f.tell())
print(res)

import json

dic=json.loads(s) #字符串 --》 字典  格式为'{"name":"xiejisen","age":26}'

#