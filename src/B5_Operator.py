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