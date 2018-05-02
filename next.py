
# 迭代器 对象访问集合的一种形式，它从集合的第一个元素开始访问，直到所有的元素被访问结束
#它只能往前，不会后退。
#优点：不需事先准备好整个迭代过程。这个特点使它特别适合用于遍历巨大的无限的集合。不如几个G的文件。

#特点：访问者：不需要关心迭代器的内部结构，，仅需next方法去取下一个内容
# 不能是随机去某个集合中的值，只能从头到尾依次从头到尾访问
# 访问到一半不能往回退
# 便于循环比较大的数组集合，节省内存

names = iter(['a','2','3'])
print(names) #2.7  names.next()
print(names.__next__())   #a
print(names.__next__())  #2

#运用
f = open("test.log",encoding='utf-8')
f.read()
f.readlines()

for line in f:
    print(line)

#生成器 generator
#定义：一个函数调用是返回一个迭代器，那这个函数叫做生成器，如果函数中包含yield 语法，那这个函数就会变成生成器
def cash_money(amount):
    while amount>0:
        amount -= 100
        yield 100
        print("又来取钱啦")

atm = cash_money(500)   # 未执行，迭代器
print(type(atm))  # 迭代器
print(atm.__next__())
print(atm.__next__())
print('我去干一下其它事')  #程序执行到一半
print(atm.__next__())

