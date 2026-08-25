# 变量的定义与赋值

# 1.变量是计算机内存中用于存储数据的命名空间，通俗来讲是带标签的快递盒
# 1.1 核心作用：数据标识、数据复用、动态修改

# 2.变量赋值
# 2.1 语法：变量名 = 值
answer = 42  # answer是变量名，42是变量值，= 是赋值运算符
k = answer  # 将一个变量储存的值赋给另一个变量
m = k + 1  # 支持表达式赋值

# 3.变量特性
# 3.1 动态特性
count = 2
print(count)
count = 3.14
print(count)
count = "hello world"
print(count)
# 3.2 序列赋值，语法：变量名1,变量名2,变量名3 = 值1,值2,值3
count1, count2, count3 = 1, 2, 3
print(count1)
print(count2)
print(count3)

# 4.变量命名
# 4.1 命名规则
# 1.变量名只能包含字母、数字、下划线
# 2.变量名不能以数字开头
# 3.变量名不能使用Python关键字
# 4. 严格区分大小写
# 4.2 命名建议
# 1.见命知义：变量名应该具有意义
'''
  2.多单词命名方式
  下划线分割：user_name
  大驼峰命名法：UserName
  小驼峰命名法：userNAME
'''

# 5.基本数据类型
# type(变量名)查看数据类型
# 5.1 数值类型
num_int = 123  # 整型
print(num_int)
print(type(num_int))

num_float = 3.14  # 浮点型
print(num_float)
print(type(num_float))

num_bool = True  # 布尔型
print(num_bool)
print(type(num_bool))

num_complex = 1 + 2j  # 复数
print(num_complex)
print(type(num_complex))

# 5.2 字符串类型
s1 = 'hello world'  # 单行字符串，使用单引号或双引号包裹
print(s1)
print(type(s1))

s2 = """
Hello world！
I am coming！"""  # 多行字符串，使用三对单引号/双引号包裹
print(s2)
print(type(s2))

s3 = None  # 空值，与0不同，0是一个数值，None是一个空值
print(s3)
print(type(s3))