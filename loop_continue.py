
f = open("test.log","a") #w  r  追加a  w+没什么用。有bug

f.write("a\n")
f.write("b\n")


# f.write("this the second line\n")
#print(f.readlines())  #将每行变成数组
#print(f.read())  # 打印出原始的
# if “3” in line:  print "this is third line"
#for line in f:
#    print(line,)

# 记得关闭文件
f.close()

