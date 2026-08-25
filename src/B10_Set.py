# 集合及其常见操作
# 1. 认识集合
print('-'*20,'1.认识集合','-'*20)
# 1.1 集合的定义：集合是无序的、无索引的、无重复的元素集合，用{}包裹，元素之间用逗号隔开，元素可以是任意类型。
# 1.2 格式：变量名 = {元素1,元素2,元素3,元素4,元素5,元素6,元素7,元素8,元素9,元素10}
print('='*15,'1.2 集合的格式','='*15)
set_chapter1 = {1,2,3,4,5,6,1,5,4,9}
print(set_chapter1,type(set_chapter1),sep=", ")
data = {}  # 空的花括号表示空字典，若想表示空集合，则采用变量名=set()
print(data,type(data),sep=', ')

# 2. 集合常见的内建函数
print('-'*20,'2.集合常见的内建函数','-'*20)
set_chapter2 = {1,2,3,4,5,6}
print(set_chapter2)
# 2.1 添加元素
print('='*15,'2.1 添加元素','='*15)
set_chapter2.add(7)  # 添加一个元素，add(单个元素)
print(set_chapter2)
set_chapter2.update([8,9,10])  # 添加多个元素，update(可迭代对象)
print(set_chapter2)
# 2.2 删除元素
print('='*15,'2.2 删除元素','='*15)
set_chapter2.remove(10)  # 删除指定元素，remove(单个元素)，元素不存在时会报错
print(set_chapter2)
set_chapter2.discard(9)  # 删除指定元素，discard(单个元素)，元素不存在时不会报错（推荐）
print(set_chapter2)
# clear()，清空集合

# 2.3 集合运算
print('='*15,'2.3 集合运算','='*15)
set_chapter3 = {1,2,3,4,5,6}
set_chapter4 = {4,5,6,7,8,9}
print(set_chapter3 & set_chapter4)  # 交集
print(set_chapter3.intersection(set_chapter4))  # 交集
print(set_chapter3 | set_chapter4)  # 并集
print(set_chapter3.union(set_chapter4))  # 并集