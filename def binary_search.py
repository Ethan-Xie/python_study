
# 二分查找法

def binary_search(data_source,find_n):

    mid=int(len(data_source)/2)
    if(mid==1):
        if data_source[mid] == find_n:
            print("存在")
            return
        print("不存在")
        return
    if data_source[mid] >find_n:
        #切片：
        data_source=data_source[:mid]
        print("数据在左边[%d]"%mid)
        binary_search(data_source,find_n)
    elif  data_source[mid] <find_n:
        #切片：
        data_source=data_source[mid:]
        print("数据在右边[%d]"%mid)
        binary_search(data_source,find_n)
    #elif  data_source[mid] ==find_n:
     #   print("找到[%d]"%mid)
    else:
        print("存在")

if __name__=='__main__':
    data = list(range(1,100,3))
    #print(data)
    binary_search(data,63)


    # 二维数组
    a=[[col for col in range(4)] for row in range(4)]
    print(a)
    print(range(0,4))
    for i in a:
        print(i)
    print(a[0][1])
    b = [[col for col in range(4)] for row in range(4)]
    for r_index,row in enumerate(a):
        #print(row,r_index)
        for c_index in range(len(row)):
            #tmp=data[]0 0  1 0
            #print(c_index,r_index)
            #temp=a[c_index][r_index]
            #a[c_index][r_index]=  row[c_index]
            #b[r_index][c_index]=temp
            b[r_index][c_index] = a[c_index][r_index]
    for i in b:
        print(i)

    import re
    m=re.match("abc","abcd")
    m = re.match("[0-9]{1,4}", "51561")
    m = re.match(".*", "51561")
    m = re.match(".+", "51561")
    m = re.search("6", "51561")
    #m = re.sub("\d","@", "5s56gf1",count=2)  #@s@@gf@
    print(m)  # 匹配失败
    if m==None:  # if m:
        print(m)  # 匹配失败
    else:
        print(m.span())
        print(m.group())

    m = re.match("[0-9]{10}","515224"  ) #None
    m = re.findall("[0-9]{10}", "54ge5wewf54") #[]
    m = re.findall("[0-9]{2}", "15255") #['15', '25']
    m = re.findall(".*", "54ge5wewf54") #['54ge5wewf54', '']
    m = re.findall("[a-zA-Z]+","54dfsef451es#%^") #['dfsef', 'es']
    m = re.findall("%","54dfsef451es#%^") #['%']
    m = re.search("\d+","45dfesf")  #<_sre.SRE_Match object; span=(0, 2), match='45'>
    if m:
        print(m)
        #print(m.span())
        #print(m.group())
    else:
        print(m)
