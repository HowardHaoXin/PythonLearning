# 列表的学习与使用
# 1.认识列表
print('-'*20,'1.认识列表','-'*20)
# 1.1 列表的定义
# 列表是有序的数据集合，用[]包裹，元素之间用逗号隔开，能存储整数、字符串、小数等任意类型的格式

# 1.2 格式：变量名 = [元素1,元素2,元素3,元素4,元素5,元素6,元素7,元素8,元素9,元素10]
print('='*15,'1.2 列表的格式','='*15)
list_string = ['a','b','c','d','e']
print(list_string,type(list_string),sep=", ")

# 1.3 列表的索引与切片
print('='*15,'1.3 列表的索引与切片','='*15)
# 索引：列表中每个元素都有索引，正序索引从0开始，倒序索引从-1开始
print(list_string[0],list_string[1],list_string[2],list_string[3],list_string[4],sep=", ")  # 正序索引
print(list_string[-1],list_string[-2],list_string[-3],list_string[-4],list_string[-5],sep=", ")  # 倒序索引
# 切片：从列表中截取某段内容，并返回为新的列表，语法：list[start:stop:step]
print(list_string[1:3])
print(list_string[-1:-4:-2])

# 1.4 列表的可修改特性
print('='*15,'1.4 列表的可修改特性','='*15)
# 语法：list[index] = new_value
list_string[0] = 'A'
print(list_string)

# 2. 列表的嵌套
print('-'*20,'2.列表的嵌套','-'*20)
grades = [[90,80,70],[80,90,80],[70,80,90]]
print(grades[0],type(grades[0]),sep=', ')  # 输出子列表
print(grades[0][0],type(grades[0][0]),sep=', ')  # 输出子列表中的元素

# 3. 列表常见的内建函数
print('-'*20,'3.列表常见的内建函数','-'*20)
# 3.1 添加元素
print('='*15,'3.1 添加元素','='*15)
list_chapter3 = [1,2,3]
print(list_chapter3)
list_chapter3.append(4)  # 列表末尾添加一个元素
print(list_chapter3)
list_chapter3.extend([5,6])  # 列表末尾添加多个元素，只能放进可迭代对象，并将可迭代对象拆分为元素逐一添加，可迭代对象定义：可以被遍历的对象
print(list_chapter3)
list_chapter3.insert(1,4)  # 在指定位置添加元素
print(list_chapter3)

# 3.2 查找元素
print('='*15,'3.2 查找元素','='*15)
print(list_chapter3.index(4))  # 查找指定元素在列表中第一次出现的索引
print(list_chapter3.count(4))  # 统计指定元素在列表中出现的次数

# 3.3 删除元素
print('='*15,'3.3 删除元素','='*15)
list_chapter3.remove(4)  # 删除列表中第一次出现的指定元素，若待删除的元素不存在，则会报错
print(list_chapter3)

# 3.4 排序与反转
print('='*15,'3.4 排序与反转','='*15)
list_chapter3.sort()  # 列表进行排序，默认为升序，字符串会根据首字符的ACSII码进行排序
print(list_chapter3)
list_chapter3.sort(reverse=True)  # 列表进行排序，指定降序
print(list_chapter3)
list_chapter3.reverse()  # 列表进行反转
print(list_chapter3)