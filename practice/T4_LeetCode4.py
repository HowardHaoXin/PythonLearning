# 题目内容：
"""
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
请注意 ，必须在不复制数组的情况下原地对数组进行操作。

示例 1:
输入: nums = [0,1,0,3,12]
输出: [1,3,12,0,0]

示例 2:
输入: nums = [0]
输出: [0]
 
提示:
1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1
 
进阶：你能尽量减少完成的操作次数吗？
Do not return anything, modify nums in-place instead.
"""

# 实现思路1：
"""
Step1：建立两个指针，左指针遍历搜索0元素，右指针遍历搜索非0元素
Step2：当左指针指向0元素，右指针指向非0元素时，交换两个指针的值，左右指针均右移一位
Step3：若左右指针均指向0，右指针右移，若右指针指向0，右指针右移，若右指针达到搜索上限，则完成交换，否则返回Step2
Step4：返回修改后的数组
"""
# def moveZeroes(nums: list[int]):
#     left = 0
#     right = 1
#     while right < len(nums):
#         if nums[left] == 0:
#             if nums[right] != 0:
#                 nums[left], nums[right] = nums[right], nums[left]
#                 left += 1
#                 right += 1
#             else:
#                 right += 1
#         else:
#             left += 1
#             right += 1
#     # return nums

# 优化思路：
"""
优化判断逻辑，减少判断次数，从而优化性能
"""
def moveZeroes(nums: list[int]):
    left, right = 0, 0
    while right < len(nums):
        if nums[right] != 0:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
        right += 1

nums1 = [0,1,0,3,12]
moveZeroes(nums1)  
print(nums1)  # 输出: [1,3,12,0,0]
nums2 = [0]
moveZeroes(nums2)  
print(nums2)  # 输出: [0]