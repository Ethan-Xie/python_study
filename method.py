
#set集合  在redis 中也有这个数据类型

arr=[]
arr2=list()

arr3 = set()
arr3.add('alex')
arr3.add('alex')  #{'alex'}
arr3.add('test')
#set(['alex','eric','tony'])  自动转换，自动去重
s3=arr3.difference(['eric','hello','test']) #相对于前面不同的，将会显示  {'alex'} 不会剔除原来的arr3

#s4=arr3.difference_update(['test','hello'])   #s4为none  arr3变为 alex

# intersection  去交集,新建一个set
# intersection_update()  交集，修改原来的set
# isdisjoint()   如果没有交集，返回true
# issubset  是否有子集
# issuperset   是否是父集
# pop  移除
# remove  symmetric_difference_update()  改原来的数据。差集
# union 更新   update  更新

#cmdb  新汇报数据   原来加入：新加入    原来有：更新


print(arr3)  # {'alex', 'test'}
ret = arr3.pop()  #不需要参数  拿出参数  取
# print(ret) 没有返回值
# arr3.remove('test')  #删除
print(arr3)
print(s3)


#//set 集合2
s1 = set([11,22,33])
s2 = set([22,44])
res = s1.difference(s2) # 以s1为基准  {33, 11}
res = s1.symmetric_difference(s2)  # 全部 {33, 11, 44}
print(res)

