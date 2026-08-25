# 函数def的学习
# 1.简单的函数：输出固定的问候语
print('-'*20,'1.简单的函数：输出固定问候语','-'*20)
def greet():
    print("你好","今天天气不错",sep='\n')
# 调用函数
greet()

# 2.带参数的函数
# 形参与实参：形参为函数定义时使用的参数：函数名(形参)，实参为函数调用时使用的参数：函数体中的调用的参数
print('-'*20,'2.带参数的函数','-'*20)
def greet(username):  # 此处的name为形参
    print(f"{username}你好","今天天气不错",sep='\n')

# 调用函数
greet("Howard")  # 此处的name为实参

# 调用函数时，参数的顺序与数量要与定义保持一致
def make_caffee(coffee_type,size,suger,ice):
    coffee = {"咖啡类型":coffee_type,"杯子":size,"糖分":suger,"冰":ice}
    print(coffee)

make_caffee("美式","大杯","少糖","常温")

# 默认参数
def make_tee(tee_type='绿茶',suger=1):
    print(f"泡一杯{tee_type},甜度{suger}")
# 调用函数
make_tee()

# 可变参数
def sum_(*nums):  # *nums为可变参数，表示可以传入任意数量的参数，函数定义时使用*号，输入时为元组的形式
    num_sum = 0
    for iter_num in nums:
        num_sum += iter_num
    return num_sum
print(sum_(1,2,3,4,5))

# 可变键值对参数
def create_user(username,**user_info):
    print("用户名：",username)
    print("用户信息：",user_info,sep='\n')
create_user("Howard", age=18, sex="男", height=170)

# 3.函数返回值，工具的输出结果：return
def calc(a,b):
    sum_ab = a + b
    mul_ab = a * b
    return sum_ab,mul_ab

# 接收方式1：
result = calc(1,2)
print(result,type(result),sep=', ')

# 接收方式2：
sum_,mul_ = calc(1,2)
print(f"和：{sum_}",f"数据类型：{type(sum_)}",sep='\n')
print(f"积：{mul_}",f"数据类型：{type(mul_)}",sep='\n')