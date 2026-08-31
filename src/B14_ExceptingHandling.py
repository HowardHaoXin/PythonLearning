# 异常处理的学习与理解
# 1.异常基础
print('-'*20,'1.异常基础','-'*20)
# 1.1 异常的定义：异常就是程序在运行过程中出现的错误，Python中异常是一个类，所有的异常都是继承自BaseException类
"""
1.2 常见异常类别
NameError: 变量名错误，用了没有定义的变量名
SyntaxError: 语法错误，代码不符合Python语法规范
IndexError: 索引错误，访问了不存在的索引
ZeroDivisionError: 除数为0的错误
KeyError: 字典中访问了不存在的键
IOError: 输入输出错误，文件不存在或无法访问
AttributeError: 对象没有该属性或方法
ValueError: 值错误，传入了不合法的参数值
TypeError: 类型错误，传入了不合法的参数类型
ImportError: 导入模块错误，模块不存在或无法导入
IndentationError: 缩进错误，代码缩进不符合Python规范
"""
# 1.3 异常处理方式一：通过traceback模块打印异常信息，返回异常处进行修改

# 2. 异常处理
# 对于无法避免的异常，如用户输入错误，我们可以用try-except语句来处理异常，避免程序崩溃，还能给出用户友好的提示信息
print('-'*20,'2.异常处理','-'*20)
# 2.1 异常处理方式二：异常捕获try-except语句
print('='*15,'2.1 异常处理','='*15)
"""
语法结构:
try:
    可能会发生异常的代码块
except [异常类型1 as 变量名]:
    异常处理代码块1
except [异常类型2 as 变量名]:
    异常处理代码块2
else:
    如果没有异常发生，执行的代码块
finally:
    无论是否发生异常，都会执行的代码块
"""
# 2.2 常用异常处理方式
print('='*15,'2.2 异常处理方式','='*15)
# 2.2.1 捕获所有异常(酌情使用)
"""
语法结构：
try:
    可能会发生异常的代码块
except Exception:
    异常处理代码块
"""
try:
    input_condition1 = input("请输入一个整数：")
    num1 = int(input_condition1)
    print(f"你输入的整数为：{num1}")
except Exception: # Exception是所有异常的基类，捕获所有非语法异常
    print("输入错误！请输入一个整数~")
# 2.2.2 捕获指定异常（推荐使用）
"""
语法结构：
分类型捕获：
try:
    可能会发生异常的代码块
except 异常类型1:
    异常处理代码块
except 异常类型2:
    异常处理代码块

捕获多个异常：
try:
    可能会发生异常的代码块
except (异常类型1, 异常类型2):
    异常处理代码块
"""
try:
    input_condition2 = input("请输入一个整数：")
    num2 = int(input_condition2)
    print(f"你输入的整数为：{num2}")
except (ValueError, NameError): # 捕获指定异常类型
    print("输入错误！可能是变量名未定义或输入格式不正确~")
except TypeError:
    print("输入错误！可能是类型不匹配~")
# 2.2.3 捕获异常并获取异常信息(便于定位问题)
"""
语法结构：
try:
    可能会发生异常的代码块
except 异常类型 as 变量名(通常为e):
    异常处理代码块
"""
try:
    input_condition3 = input("请输入一个整数：")
    num3 = int(input_condition3)
    print(f"你输入的整数为：{num3}")
except ValueError as e: # 捕获指定异常类型，并获取异常信息
    print("输入错误！可能是输入格式不正确~")
    print(f"异常信息：{e}")
# 2.2.4 else和finally的使用
"""
语法结构：
try:
    可能会发生异常的代码块
except 异常类型 as 变量名:
    异常处理代码块
else:
    如果没有异常发生，执行的代码块
finally:
    无论是否发生异常，都会执行的代码块
"""
try:
    input_condition4 = input("请输入一个整数：")
    num4 = int(input_condition4)
except ValueError as e:
    print("输入错误！可能是输入格式不正确~")
    print(f"异常信息：{e}")
else:
    print(f"你输入的整数为：{num4}")
finally:
    print("无论是否发生异常，都会执行的代码块~")

# 3.异常处理核心原则
"""
1) 优先捕获具体异常，不要用Exception捕获所有异常（可能掩盖未知错误），除非你确实需要捕获所有异常。
2) 不要滥用异常处理，语法错误要提前修正，无法靠异常处理来解决。
3) 处理逻辑要友好，给用户清晰的提示信息，避免程序崩溃。
4) finally用于释放资源或执行清理操作，确保程序的健壮性，如：关闭文件、断开网络连接等。
"""

# 4. 抛出自定义异常
print('-'*20,'4.自定义异常','-'*20)
# 4.1 自定义异常：“自己定义的错误类型”，专门应对业务场景的特殊错误
# 4.2 自定义异常实现步骤：
"""
Step1: 创建异常对象，语法：异常类型(异常的具体描述信息)
Step2: 使用raise关键字抛出异常对象，语法：raise 异常对象
例如：
Exception1 = Exception("余额不足！")
raise Exception1
"""
# 需求：模拟银行取款场景
# 定义账户余额与冻结状态
account1 = {"ID":"123456", "balance": 1000, "is_frozen": False}
def withdraw(withdraw_amount, account):
    # 作用：模拟银行取款操作
    # 基本逻辑：取款金额小于余额时，允许取款并改变账户余额，若取款金额大于余额，抛出异常：余额不足！，若账户被冻结，抛出异常：账户被冻结！
    # 参数声明：
    # withdraw_amount: 取款金额
    # account: 账户信息，字典类型，包含账户ID、余额、冻结状态
    # 返回值：无
    if account["is_frozen"]:
        raise Exception("账户已冻结！")
    
    if withdraw_amount > account["balance"]:
        raise Exception("余额不足")

    account["balance"] -= withdraw_amount
    print(f"当前余额{account["balance"]}")
withdraw(100, account1)