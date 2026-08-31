# 测试题
# 给一串数字，找出其中所有和为0的三个数，并输出这些组合

# 第一步，获取输入的内容并转换为数字
input_string = input("请输入一串数字，以空格分隔：")  # 获取输入数字
# print(input_string,type(input_string),sep=', ')
nums = tuple(map(int,input_string.split())) # 将输入的字符串按空格分隔，并转换为元组
# map函数的简单介绍

# print(nums, type(nums), sep=', ')

# 第二步，设计算法找出所有和为0的三个数
# 算法1：三重循环遍历三个数的组合
def triple_loop(nums):
    # 采用三重循环
    len_nums = len(nums)
    for i in range(len_nums - 2):
        for j in range(i + 1, len_nums - 1):
            for k in range(j + 1, len_nums):
                sum_temp = nums[i] + nums[j] + nums[k]
                if sum_temp == 0:
                    print(f"找到组合(算法1)：{nums[i]}+{nums[j]}+{nums[k]}=0")

# 算法2：排序+双指针法
def two_pointer(nums):
    # 先对数组排序
    nums = sorted(nums)
    # 采用双指针的方式实现
    len_nums = len(nums)
    for i in range(len_nums - 2):
        left = i + 1 # 左指针
        right = len_nums - 1 # 右指针
        while left <right:
            sum_temp = nums[i] + nums[left] + nums[right]
            if sum_temp == 0:
                print(f"找到组合(算法2)：{nums[i]}+{nums[left]}+{nums[right]}=0")
                left += 1
                right -= 1
            elif sum_temp < 0:
                left += 1
            else:
                right -= 1

triple_loop(nums) # 调用算法1
two_pointer(nums) # 调用算法2
                