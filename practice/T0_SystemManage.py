# 函数版学员管理系统的设计
# ======================================================================================================================
# 1.系统核心说明
# --------------------------------------------
# 1.1 功能清单：
""""""
"""
1.添加学员信息（学号、姓名、手机号，学号不重复）
2.删除学员信息（按学号删除信息）
3.修改学员信息
4.查询学员信息
5.显示所有学员
6.退出系统（二次确认，防止误操作）
"""
# --------------------------------------------
# 1.2 数据存储方式
# 采用“列表+字典”的方式存储学员信息
    # 全局列表info存储所有学员数据，所有函数共用
    # 每个学员是一个字典，{id：学号，name：姓名，tel：手机号}
info = []  # 全局列表，存储所有学员信息
# ======================================================================================================================
# 附录：系统功能实现所需要的函数
# 1.显示学员管理系统的界面信息
def show_menu():
    print("="*35)
    print(" "*10,"学员管理系统 v1.0")
    print("1.添加学员信息",
          "2.删除学员信息",
          "3.修改学员信息",
          "4.查找学员信息",
          "5.显示所有学员信息",
          "6.退出系统",sep='\n')
    print("="*35)

# 2. 添加学员信息
def add_info():
    # 获取用户输入信息
    id_new = input("请输入学号：")
    name_new = input("请输入姓名：")
    tel_new = input("请输入联系电话：")

    # 判断是否已存在该学号
    for student in info:
        if student['id'] == id_new:
            print("该学号已经存在，无法重复添加")
            return  # 函数返回，结束当前函数，不执行后续代码

    # 保存到字典中
    student_dict = {
        'id': id_new,
        'name': name_new,
        'tel': tel_new
    }

    # 保存到全局列表中
    info.append(student_dict)
    # print(student_dict)  # 打印字典，用于测试
    # print(info)  # 打印列表，用于测试

# 3.删除学员信息
def delete_info():
    id_student = input("请输入要删除学员的学号：")
    # 判断学员是否存在
    for student in info:
        if student['id'] == id_student:
            name_temp = student['name']
            info.remove(student)
            print(f"已删除姓名为{name_temp},学号为{id_student}的学员信息")
            return  # 退出函数，避免错误执行
    print("学员不存在！")

# 4.修改学员信息
def modify_info():
    id_student = input("请输入要修改学员的学号：")

    # 判断学员是否存在
    for student in info:
        if student['id'] == id_student:
            while True:
                key_temp = input('请选择要更改的信息（id：学号；name：姓名；tel：联系电话；none：不修改）：')
                if key_temp == "none":
                    return  # 结束该函数
                else:
                    student[key_temp] = input(f"请输入新的{key_temp}：")
                    print("修改成功！")
                    judgement = input('是否继续修改该学员信息（y/n）')
                    if judgement == "n":
                        return  # 结束该函数
    print("学员不存在！")

# 5.查找学员信息
def search_info():
    while True:
        id_student = input("请输入要查找学员的学号：")
        for student in info:
            if student['id'] == id_student:
                print("该学员的信息如下：")
                print(f"学号：{student['id']}",
                      f"姓名：{student['name']}",
                      f"联系电话：{student['tel']}",
                      sep='\n')
                judgement = input("是否继续查找学员（y/n）")
                if judgement == 'n':
                    return

    print("未找到该学员！")

# 6.显示所有学员信息
def show_all_info():
    # 格式化表头信息
    print("="*35)
    print("学号\t\t姓名\t\t联系电话")
    print("-"*35)
    for student in info:
        print(f"{student['id']}\t\t{student['name']}\t\t{student['tel']}")
    print("="*35)

# ======================================================================================================================
# 2.分布实现：从基础框架到完整功能
# --------------------------------------------
# 2.1 第一步：搭建系统框架
while True:
    # 显示学员管理系统的系统菜单
    show_menu()

    # 获取用户输入功能序号
    user_num = input("请输入功能对应序号(1-6)：")

    # 根据序号执行对应功能：if--elif--else
    if user_num == "1":
        print("你选择了添加学员信息功能")
        # 调用添加学员信息函数
        add_info()
    elif user_num == "2":
        print("你选择了删除学员信息功能")
        # 调用删除学员信息函数
        delete_info()
    elif user_num == "3":
        print("你选择了修改学员信息功能")
        # 调用修改学员信息函数
        modify_info()
    elif user_num == "4":
        print("你选择了查找学员信息功能")
        # 调用查找学员信息函数
        search_info()
    elif user_num == "5":
        print("你选择了显示所有学员信息功能")
        # 调用显示所有学员信息函数
        show_all_info()
    elif user_num == "6":
        exit_config = input("你确定要退出系统吗（y/n）？")
        if exit_config == "y":
            print("退出成功，欢迎下次再来！")
            break   # 终止循环以退出系统
    else:
        print("没有对应功能，请重新选择系统存在的功能")
# --------------------------------------------
# 2.1 第二步：添加系统的各个功能
# 功能采用函数实现，放在附录中
# ======================================================================================================================