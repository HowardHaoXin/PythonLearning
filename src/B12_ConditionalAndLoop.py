# 条件语句与循环语句
# 一、条件语句
# 1.简单if语句：满足条件则执行
# A = int(input("A= "))
A = 11
if A%2 == 0:                    # 判断条件
    print(f"{A}是偶数")          # 执行代码块

# 2.比较运算符与逻辑运算符
# 2.1 比较运算符
"""
==          等于
!=          不等于
>           大于
<           小于
>=          大于等于
<=          小于等于
"""

# 2.2 逻辑运算符
"""
and         并且      逻辑与
or          或者      逻辑或
not         非        逻辑非
"""
# python中非0非空的数据当作条件使用时均会判断为Ture
# 登录验证
# username = input("请输入用户名：")
# password = input("请输入密码：")
username = 'bingbing'
password = '123456'
if username == 'bingbing' and password == '123456':
    print("登录成功")
else:
    print("登录失败，用户名或密码错误")

# 3.多分支判断
grade = 85.0
if grade>=80.0:
    print("成绩优秀")
elif grade>=60.0:
    print("成绩及格")
else:
    print("成绩不及格")

# 二、循环语句
# 1.while循环
count = 1
count_sum = 0
while count<=5:
    count_sum += count
    count += 1
print(count_sum)

# while循环嵌套
cols = 1
while cols<=3:
    rows = 1
    while rows<=6:
        print(f'第{cols}排第{rows}列',end='  ')
        rows += 1
    cols += 1
    print('\n')

# 2.for循环：for 变量 in 可迭代对象/次数序列:
s = 'bingbing'
for char in s:
    print(char,end='  ')
print('\n')

index_sum = 0
for index in range(10):    # range(stop):表示[0,stop-1]；range(start,stop):表示[start,stop-1]；range(start,stop,step):表示[start,stop-1]，步长为step
    # range(stop):表示[0,stop-1]
    # range(start,stop):表示[start,stop-1]，步长为1，与matlab中的start:stop-1含义一致
    # range(start,stop,step):表示[start,stop-1]，步长为step，与matlab中的start:step:stop-1含义一致
    index_sum += index
    print(index_sum,end='  ')