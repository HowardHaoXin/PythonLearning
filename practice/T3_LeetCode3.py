# 题目内容：
"""
给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。
请你设计并实现时间复杂度为 O(n) 的算法解决此问题。

示例 1：
输入：nums = [100,4,200,1,3,2]
输出：4
解释：最长数字连续序列是 [1, 2, 3, 4]。它的长度为 4。

示例 2：
输入：nums = [0,3,7,2,5,8,4,6,0,1]
输出：9

示例 3：
输入：nums = [1,0,1,2]
输出：3
 
提示：
0 <= nums.length <= 105
-109 <= nums[i] <= 109
"""

# 实现思路1：
"""
Step1：将数组进行去重，使用set()函数
Step2：将数组进行排序
Step3：遍历数组，判断当前元素与前一个元素的差值是否为1，如果是，则计数器加1，否则比较当前最大值与计数器的值，取最大值，并将计数器重置为1
Step4：返回最大值
"""
# def longestConsecutive(nums: list[int]):
#     if not nums:
#         return 0
#     nums = sorted(set(nums))
#     max_len = 1   # 初始化最长序列值
#     count = 1     # 初始化计数器
#     for i in range(1, len(nums)):
#         if nums[i] - nums[i - 1] == 1:
#             count += 1  # 更新计数器的值
#         else:
#             max_len = max(max_len, count)  # 更新最大值
#             count = 1    # 重置计数器
#     return max(max_len, count)   # 返回最大值，防止最后一个元素是最长序列的情况

# 实现思路2：利用集合的哈希特性
"""
Step1：将数组进行去重，使用set()函数
Step2：遍历集合，判断当前元素的前一个元素是否在集合中，如果不在，则说明当前元素是一个序列的起点
Step3：从当前元素开始，向后遍历，判断当前元素的下一个元素是否在集合中，如果在，则计数器加1，否则比较当前最大值与计数器的值，取最大值，并将计数器重置为1
Step4：返回最大值
"""
def longestConsecutive(nums: list[int]):
    if not nums:
        return 0
    nums_set = set(nums)
    max_len = 0  # 初始化最长序列值
    for num in nums_set:
        if num -1 not in nums_set: # 判断当前元素的前一个元素是否在集合中
            count = 1 # 初始化计数器
            while num + 1 in nums_set: # 判断当前元素的下一个元素是否在集合中
                num += 1  # 更新当前元素的值
                count += 1 # 更新计数器的值
            max_len = max(max_len, count) # 更新最大值
    return max_len # 返回最大值

nums1 = [100,4,200,1,3,2]
print(longestConsecutive(nums1))
nums2 = [0,3,7,2,5,8,4,6,0,1]
print(longestConsecutive(nums2))
nums3 = [1,0,1,2]
print(longestConsecutive(nums3))