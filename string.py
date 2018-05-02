
arr=['xie','two','three']  #存多个信息

if 4 in arr:   # true  or false

arr1="hello"
arr.extend(arr1)
print(arr)  #['xie', 'two', 'three', 'h', 'e', 'l', 'l', 'o']
arr[1:2]   #截取序号为一的
arr[0:5:2]  #个两个切一个
arr.append('one')  #追加
arr.index('one')  #1
arr.count('one')   #3
arr.pop()   #最后一个
arr.remove("one")  # 把one这个值给去了
arr.reverse()
arr.sort()    #数字靠前
arr.insert(3,'four')

# 如果字母有两个一样的话
for i in range(arr.count('double')):
    arr.remove("double")

# 去除空白
name = input("name:").strip() # 默认去空格
age = input("age:")
job = input("job:")

print("\nname:"+name+"\nage:"+age+"\njob:"+job)
print("\nname:%s\nage:%s\njob:%s" %(name,age,job))

# continum的用法  break 跳出一个循环
for i in range(10):
    if i<5:
        continue
    print(i)