
# 使用yield 实现单线程的异步并发效果
import  time
def consumer(name):
    print("%s 准备吃包子啦！" %name)
    while True:
        baozi = yield  #接收值
        print("包子[%s]来了，被[%s]吃了！" %(baozi,name))


def producer(name):
    c = consumer("A")
    c2 = consumer("B")
    c.__next__()
    c2.__next__()
    print("老子开始做包子了")
    for i in range(1):  #0
        time.sleep(1)
        print("做了两个包子了")
        c.send(i)  #//给  yiled 送值
        c2.send(i)


producer("alex")   # 每分钟做两个包子，并同时分给两个人
"""
A 准备吃包子啦！
B 准备吃包子啦！
老子开始做包子了
做了两个包子了
包子[0]来了，被[A]吃了！
包子[0]来了，被[B]吃了！
做了两个包子了
包子[1]来了，被[A]吃了！
包子[1]来了，被[B]吃了！
"""

# python 装饰器
# tv=login(tv)
# tv("alex")
def w1(func):
    print("我在w1函数内")
    def inner():
        print("我在inner函数内")        #
        #2
        #3
        return func
    return inner

#@w1
def f1():
    print('我在f1函数内')

flag=w1(f1) # 执行w1函数
#print(flag)
flag=flag()  #执行inner 函数
flag()      ##执行f1 函数
'''
我在w1函数内
我在inner函数内
我在f1函数内
'''
#---------------next----------

print("开始@的用法说明")
@w1
def f2():
    print('我在f1函数内')
f2()
"""
@w1 :执行w1，把自己装饰的函数名当作参数，相对于w1(f2)
    show 函数重新定义，w1(show)返回值
    新show =
"""

#@w1(f1)  #如此是这样
def f3():
    print('我在f1函数内')

"""
@filter(before,after)
1. 执行filter(before,after)
2.@outer
3 新的
"""

#---------------递归   ----------
def calc(n):
    if n/2 >1:
        print(n)
        res=calc(n/2)
        print(n,res)
        return  res

calc(20)
"""
20
10.0
5.0
2.5
2.5 None
5.0 None
10.0 None
20 None
"""

# def 数列  第三位数=数2+数1
def func3(arg1,arg2):
    if arg1==0:
        print(arg1)
        print(arg2)
    arg3=arg1+arg2
    print(arg3)
    if arg3<110:
        func3(arg2,arg3)

func3(0,1)
"""
0
1
1
2
3
5
8

"""
# 二分查找法
data = list(range(1,100,3))
print(data)