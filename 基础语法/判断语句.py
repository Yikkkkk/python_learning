#bool类型

# 注意缩进，python通过缩进来判断归属关系
# if，else 语句后面有引号

age = 19
if(age > 18):
    print(f"{age}大于18岁！")


#猜数字 1-100 呜呜呜终于写出来了
import random
i=0
flag =0
number = random.randint(1,100)
while flag==0:
    i+=1
    num = int(input("请输入数字："))
    if num<number:
        print("太小了！")
    elif num>number:
        print("太大了！")
    elif num==number:
        print(f"猜对了！你使用了{i}次猜测")
        flag=1


#print输出不换行
print("hello ",end = "")
print("world",end = "")



