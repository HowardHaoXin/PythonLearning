# 输入函数input的使用与理解

# 1.核心作用：让程序获取用户在控制台输入的数据
# 2.语法：value = input([prompt])
# 参数：
# prompt：提示信息，会显示在控制台，提示用户输入什么，默认为None
# value：返回值，用户在控制台输入的数据，返回的数据类型为str
# 例如：
name = input("请输入你的名字：")
print(name,"你好呀！",sep=", ")
print(type(name))

# 3.数据转换
# 由于返回值的数据类型为str，因此在某些时候需要进行数据转换才能使用
# 例如：
num_int1 = int(input("请输入一个整数："))  # 将输入的数据转换为整数
num_int2 = int(input("请输入一个整数："))  # 将输入的数据转换为整数
num_int = num_int1 + num_int2
print(num_int,type(num_int),sep=", ")