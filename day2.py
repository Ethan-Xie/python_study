# 控制循环次数
#while True:

num1 = 1
guess_count=0
input_num=-1
while input_num != num1 and guess_count <3:
    input_num = int(input("input the guess num:"))
    if input_num < num1:
        print("the real numer is smaller.")
    else:
        print("the real num is bigger")

    guess_count += 1

print("bingo")