# 元组的学习及其常见操作
# 1.认识元组
print('-'*20,'1.认识元组','-'*20)
# 1.1 元组的定义：元组是有序的、不可修改的“数据容器”，用()包裹，元素之间用逗号隔开，能存储整数、字符串、小数等任意类型的格式
# 1.2 格式：变量名 = (元素1,元素2,元素3,元素4,元素5,元素6,元素7,元素8,元素9,元素10)
print('='*15,'1.1 元组的定义','='*15)
tuple_chapter1 = (1,2,3,4,5,6)
print(tuple_chapter1,type(tuple_chapter1),sep=", ")
# 注意：若元组中只有1个元素，则必须用逗号隔开，否则会被Python解释为变量名
tuple_warning1 = (1)
print(tuple_warning1,type(tuple_warning1),sep=", ")
tuple_warning2 = (1,)
print(tuple_warning2,type(tuple_warning2),sep=", ")

# 1.3 元组的索引和切片(同列表)
print('='*15,'1.3 元组的索引和切片','='*15)
# 元组的索引
print(tuple_chapter1[0])
# 元组的切片
print(tuple_chapter1[0:5:3])
print(tuple_chapter1[-1:-6:-3])

# 1.4 元组的特性：不可修改

# 2.元组的常见操作
print('-'*20,'2.元组的常见操作','-'*20)
tuple_chapter2 = ('Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday')
print(tuple_chapter2)
# 2.1 成员判断
print('='*15,'2.1 成员判断','='*15)
print('Monday' in tuple_chapter2)
print('Tuesday' not in tuple_chapter2)
# 2.2 查找索引
print('='*15,'2.2 索引查找','='*15)
print(tuple_chapter2.index('Monday'))  # 索引查找，若不存在则报错
# 2.3 统计次数
print('='*15,'2.3 统计次数','='*15)
print(tuple_chapter2.count('Monday'))  # 统计次数，若不存在则返回0