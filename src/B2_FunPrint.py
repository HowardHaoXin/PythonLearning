# 输出函数的使用
# 1.语法：print(*args, ..., sep=' ', end='\n', file=sys.stdout, flush=False)

# 1.1 *args：想要输出多少内容就输出多少内容
print()  # 输出零个值
print("hello world")  # 输出一个值
print("hello world", "hello world")  # 输出两个值
print(123)  # 输出一个数字
print(123,456)  # 输出两个数字

# 1.2 sep：指定不同输出内容之间的分隔符，默认为空格
print("hello world", "hello world", sep=", ")  # 输出两个值，中间用逗号分隔

# 1.3 end：指定输出结束符，默认为换行符，即\n
print("hello world", "hello world", sep=", ", end="###")
print("hello world", "hello world", sep=", ", end="")