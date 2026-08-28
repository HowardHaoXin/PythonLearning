# 运算符的使用与理解
# 1.算数运算符(数值类型的数学运算)
addition = 4 + 5  # 加法
print(addition)
subtraction = 4 - 5  # 减法
print(subtraction)
multiplication = 4 * 5  # 乘法
print(multiplication)
division = 4 / 5  # 除法，结果为浮点数
print(division)
floor_division = 4 // 5  # 向下取整除法
print(floor_division)
modulus = 4 % 5  # 取余
print(modulus)
exponent = 4 ** 5  # 乘方，前者为底数，后者为指数
print(exponent)
# 若运算值中包含浮点数，则结果必为浮点数
# 算术运算符的优先级与数学运算一致

# 2.赋值运算符

# 简单赋值运算符
score = 98  # 给变量赋值
print(score,type(score))

# 复合赋值运算符（必须先给变量赋值才能使用）
score += 2  # 等价于 score = score + 2
print(score,type(score))
score -= 2  # 等价于 score = score - 2
print(score,type(score))
score *= 2  # 等价于 score = score * 2
print(score,type(score))
score /= 2  # 等价于 score = score / 2
print(score,type(score))
score //= 2  # 等价于 score = score // 2
print(score,type(score))
score %= 2  # 等价于 score = score % 2
print(score,type(score))
score **= 2  # 等价于 score = score ** 2
print(score,type(score))

# 赋值运算的使用与理解
# 赋值实际上是让变量指向某个内存中的对象，多个变量可以指向同一个对象
a = 10
b = a  # b 指向与 a 相同的整数对象 10
print(b)
a = 20  # 重新给 a 赋值为 20（新建整数对象），不影响 b 的指向
print(b)  # b 仍指向原来的 10，所以输出 10

lst1 = [1,2,3]
lst2 = lst1  # lst2 与 lst1 指向同一个列表对象
print(lst2)
lst1.append(4)  # 通过 lst1 修改列表（列表可变），lst2 看到的也是同一个对象
print(lst2)  # 因此输出 [1, 2, 3, 4]
# 二者结果不同的原因：整数是不可变类型，重新赋值会创建新对象，原对象不变；
# 而列表是可变类型，通过 lst1 修改的是对象本身，因此 lst2 也能看到变化。