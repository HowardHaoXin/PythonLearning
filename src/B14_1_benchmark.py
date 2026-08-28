# 算法性能批量测试
# 目的：不再手动输入数组，自动生成不同长度的随机数组，
#       批量比较「三重循环」与「排序+双指针」两种算法的运行时间

import random
import time


# 算法1：三重循环遍历所有三数组合，时间复杂度 O(n^3)
def triple_loop(nums):
    count = 0  # 用计数代替 print，避免打印 I/O 干扰计时
    len_nums = len(nums)
    for i in range(len_nums - 2):
        for j in range(i + 1, len_nums - 1):
            for k in range(j + 1, len_nums):
                if nums[i] + nums[j] + nums[k] == 0:
                    count += 1
    return count


# 算法2：先排序，再用左右双指针，时间复杂度 O(n^2)
def two_pointer(nums):
    count = 0
    nums = sorted(nums)  # 排序 O(n log n)
    len_nums = len(nums)
    for i in range(len_nums - 2):
        left = i + 1  # 左指针
        right = len_nums - 1  # 右指针
        while left < right:
            s = nums[i] + nums[left] + nums[right]
            if s == 0:
                count += 1
                left += 1
                right -= 1
            elif s < 0:
                left += 1
            else:
                right -= 1
    return count


# 生成指定长度的随机数组（整数范围 lo~hi，默认 -100~100）
def gen_array(length, lo=-100, hi=100):
    return [random.randint(lo, hi) for _ in range(length)]


# 计时函数：重复 repeat 次取平均，结果更稳定
def time_cost(func, nums, repeat=3):
    total = 0.0
    for _ in range(repeat):
        start = time.perf_counter()
        func(nums)
        total += time.perf_counter() - start
    return total / repeat


# 批量测试不同长度
print(f"{'长度':>6} | {'三重循环 O(n^3)':>18} | {'双指针 O(n^2)':>18}")
print("-" * 50)
for n in [50, 100, 150, 200]:  # 可自行增改长度；三重循环会随 n 迅速变慢
    nums = gen_array(n)
    t1 = time_cost(triple_loop, nums)
    t2 = time_cost(two_pointer, nums)
    print(f"{n:>6} | {t1:>15.6f}s | {t2:>15.6f}s")
