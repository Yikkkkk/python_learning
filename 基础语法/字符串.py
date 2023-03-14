#三种定义格式
name1 ="first"
name2 = 'second'
name3 = """third"""#支持换行输入字符串
#三个引号的格式，如果有变量去接收，则为字符串；否则为注释

"""
引号嵌套：
1.要包含双引号，则用单引号定义
2.转移字符 \
"""
print("\"test") 

#print可以拼接字符串，数字不能
print(name1 + name2)

#在字符串里面拼接,多个则用括号
message = "顺序是：%s,%s" % (name1,name2)
print(message)

#字符串格式化 f"{占位}
#适合对精度要求不高
num = 2006
print(f"我是{name2},今年{num}")

name = input("请输入你的名字：")
print(f"name:{name}")

