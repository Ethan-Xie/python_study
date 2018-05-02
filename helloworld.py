# print  hello world

print("hello world")

# input turn to number

# sex = input("please your sex")
sex = "xie"
if sex=="girl":
    print("your sex is girl")
elif sex=="man":
    print("your sex is boy")
else:
    print("don't know")


# 循环输入
#while True:

num1 = 1
input_num = int(input("input the guess num:"))
while input_num != num1:
    # 需要吧上面那个
    #if input_num == num1:
      #  print("bingo")
        #break
    if input_num > num1:
        print("the real numer is smaller.")
    else:
        print("the real num is bigger")

print("bingo")
