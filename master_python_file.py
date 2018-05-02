
# 如果执行这个命令：  python index.py
#  上面的命令会自动  __name__='__main__'
# 如果有其它的文件如 1.py 2.py  lib/3.py
#              __name__  1  2  3  lib.3

def f1():
    pass
def f2():
    pass


if(__name__ == '__main__'):
    f1()
    # 对于python，一切都是对象，对象基于类创建
    name ='alex'
    arr = [11, 22, 33]
    array=list
    #查看什么类型
    print(type(arr))

    #int 内部功能的介绍
    age=3
    print(age.bit_length())  #2 代表二进制，二位
    print(type(age))
    #内置函数的开始时间：
    age.__abs__()  #创建对象，并执行abs方法
    abs(2)
    age.__add__(100) #加法
    plus=11+12  #此方法也行  和上面一样的执行
    # cmp 比较两个数的大小

    #divmod     分页是用的到  pages.__divmod__(10)  结果为（9,5）

    print(plus)

    result=age.__eq__(19)  #false
    result=age.__float__()   #2.0 在内存中重新创建了一个float对象
    #floatdiv
    result=age.__floordiv__(2) # 取整数  余数不要
    result=print(7//6) #算术运算符" // "来表示整数除法，返回不大于结果的一个最大的整数，而" / " 则单纯的表示浮点数除法
    print(result)

    #float 类型
    #下次补

    #集合 ，列表 ，元祖


    #字符串  操作好重要
    str='Ethan'
    print(type(str))
    #print(dir(str))   #遍历所有方法
    result=str.__contains__('e')  #是否包含，下列如同  format 在里面是没有的
    result='e' in name
    result=name.casefold() # 大写变小写
    result=8*'x'
    result=name.center(20,'*') #********alex********
    result=name.count('d',0,10)  #0到10之间
    result=name.encode('gbk')
    result=name.endswith('e',0,4)  #结尾
    result=name.expandtabs()  #\t  转换为 tab空格
    result = name.find('l')  # 1
    str2="alex {0} hello"
    result=str2.format('sb') #alex sb hello

    li = ['a','b']
    result = " ".join(li)  #a b
    result = "".join(li) #ab

    result=name.partition('l')  #('a', 'l', 'ex')
    result=name.replace('a','o',1)  #olex
    #name.splitlines()
    #name.split('\n')
    #startswith  swapcase title translate
    print(result)

    # 字典  i[]  getItem delItem

    # 上下文管理剖析
    with open('test.log') as f :  #通过with管理上下文
        #f.write()
        print("into method")

    #list 的内部功能介绍
    li=list([1,2,3])
    li=list((1,2,3))
    #copy  count  extend(合并
    result = li.extend([11,22])  #列表
    result = li.extend((11, 22,))  # 元祖 ,最后加个逗号，潜规则
    li.insert(2,"6")
    li.remove(11)
    li.reverse()  # [22, 11, 22, 3, '6', 2, 1]
    ll = [11,22,34]
    #li = tuple(ll)
    print(li)

    # 字典
    dic = {'k1':'v1','k2':'v2'}
    dic = dict(k1='v1',k2='v2')  #两种定义方式都行
    new_dict = dic.fromkeys(['k1','k2'],'v1') #{'k1': 'v1', 'k2': 'v1'}
    result = dic.get('k1')  #v1
    result = dic.get('k3','alex')  #默认值 alex
    result = dic.keys()  #dict_keys(['k1', 'k2'])
    result = dic.items()  #dict_items([('k1', 'v1'), ('k2', 'v2')])
    result = dic.values()  #dict_values(['v1', 'v2'])

    #for v in dic.values()  print(v)
    #for k,v  in dic.items() print(k,v)
    result = dic.update('k2',60)


    print(new_dict)
    print(result)

    #列表 字典
    dic={}
    all_list = [11,22,33,44,55,66,77,88]
    for i in all_list:
        if i>66:
            if "k1" in dic.keys():
                dic['k1'].append(i)
            else:
                dic['k1'] = [i,]

        else:
            if "k2" in dic.keys():  #先判断有没有k2
                dic['k2'].append(i)
            else: # {'k2':[11,]}
                dic['k2'] = [i, ]








