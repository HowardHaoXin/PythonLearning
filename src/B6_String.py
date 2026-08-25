# 字符串的使用与理解
print("-"*20,"字符串运算符章节","-"*20,sep="")
# 1. 字符串运算符
print("="*15,"1.1 字符串拼接","="*15,sep="")
# 1.1 +：字符串拼接
st1 = "同志"
st2 = "你好呀！"
print(st1 + st2)

print("="*15,"1.2 字符串重复","="*15,sep="")
# 1.2 *：字符串重复
print(st1 * 3)

print("="*15,"1.3 in/not in","="*15,sep="")
# 1.3 in/not in：判断字符串中是否包含某字符
print("你" in st1)
print("你" not in st1)

print("-"*20,"索引与切片章节","-"*20,sep="")
# 2.索引与切片
# 索引：字符串中每个字符的索引分为正序与倒序
# 正序索引：从左到右依次为0,1,2,3,4,5,……
# 倒序索引：从右到左依次为-1,-2,-3,……
print("="*15,"2.1 索引","="*15,sep="")
name = 'Harword'
print(name[0],name[1],name[2],name[3],name[4],name[5],name[6],sep = ', ')
print(name[-1],name[-2],name[-3],name[-4],name[-5],name[-6],name[-7],sep = ', ')

# 切片：从字符串中截取某一段内容，并返回为新的字符串
# 语法：str[start:stop:step]
"""
参数详解
start：起始索引，默认为0
stop：结束索引，默认为字符串结尾
step：步长，默认为1
"""
print("="*15,"2.2 切片","="*15,sep="")
print(name[:])  # 默认起始索引为0
print(name[2:])  # 默认结束索引为字符串结尾
print(name[:5])
print(name[::2])
print(name[::-1])

print("-"*20,"转义字符章节","-"*20,sep="")
# 3.转义字符
# 转义字符以\开头，用来表示不能直接输入的特殊符号，如：换行、制表符等，相当于文字的特殊指令
# 常见转义字符：
print("hello world")
print("\thello world")  # 制表符，类似Tab键的功能用于对齐文本
print("这是第一行\n这是第二行\n这是第三行")  # 换行符，另起一行
print("D:\\use\\Simulation\\PythonLearning")  # 显示单个反斜杠，如文件路径
print("\'现象\"")  # 显示单引号/双引号，避免与字符串界定符冲突
print(r"D:\use\Simulation\PythonLearning")  # r表示原样输出字符串，即不进行转义

print("-"*20,"格式化字符串章节","-"*20,sep="")
# 4.格式化字符串
# 作用：将变量、数字或运算结果嵌入到字符串中，让输出更整齐，不需要使用+反复拼接，避免报错
# 实现方式：
# f-string，语法：字符串前加f或F，用{}包裹变量/表达式，如：f"{变量名}"
age = 18
age1 = 9
print("我的姓名是",name,"，我的年龄是",age,sep="")  # 可读性很差
print("我的姓名是"+name+"，我的年龄是"+str(age))
print(f"我的姓名是{name}，我的年龄是{age:2}")  # 格式化字符串
print(f"我的姓名是{name}，我的年龄是{age1:2}")  # 设置最小宽度，默认填充空格
print(f"我的姓名是{name}，我的年龄是{age1:02}")  # 设置最小宽度，并填充0
print(f"我的姓名是{name}，我的年龄是{age1:_>2}")  # 数值默认右对齐，字符串默认左对齐，修改对齐方式采用如：<表示左对齐，>表示右对齐，^表示居中
pi = 3.1415926535897932384626
print(f"圆周率是{pi:.10f}")  # 设置小数精度，保留小数点后十位小数，不足补0

print("-"*20,"字符串的常用内建函数章节","-"*20,sep="")
# 5.字符串的常用内建函数
print("="*15,"5.1 查找类函数","="*15,sep="")
# 5.1 查找类函数（找字符/统计次数）
st_test = " The weather is nice today\ndo you want to go for a walk together "
print(st_test.find("g"))  # 找字符，返回第一个匹配的字符的索引，找不到返回-1
print(st_test.find("nice"))  # 找字符串，返回第一个匹配的字符串的索引，找不到返回-1，这里返回第一个字母n的索引
print(st_test.index("g"))  # 找字符，返回第一个匹配的字符的索引，找不到会报错
print(st_test.count("e"))  # 统计字符出现的次数

print("="*15,"5.2 修改类函数","="*15,sep="")
# 5.2 修改类函数
print(st_test.replace(" ", "%"))  # 替换字符串中的字符
print(st_test.replace(" ", "%", 1))  # 替换字符串中的字符，只替换第一个匹配的字符
print(st_test.split())  # 分割字符串，返回列表，默认使用空白进行分割
print(st_test.split(" "))  # 分割字符串，返回列表，指定分割字符
print(st_test.split(" ",1))  # 分割字符串，返回列表，指定分割字符，指定分割次数
print(st_test.strip())  # 删除字符串头尾指定的字符（默认为空格）
print(st_test.upper())  # 转大写
print(st_test.lower())  # 转小写

print("="*15,"5.3 判断类函数","="*15,sep="")
# 5.3 判断类函数
print(st_test.startswith("T")) # 判断字符串是否以指定字符开头
print(st_test.endswith("t"))  # 判断字符串是否以指定字符结尾
print(st_test.isupper())  # 判断字符串是否全部大写
print(st_test.islower())  # 判断字符串是否全部小写

print("="*15,"5.4 编码和解码","="*15,sep="")
# 5.4 编码和解码
bytes_st = st_test.encode()
print(st_test.encode())
print(bytes_st.decode())