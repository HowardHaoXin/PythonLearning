# 题目内容
"""
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。
你可以假设每种输入只会对应一个答案，并且你不能使用两次相同的元素。
你可以按任意顺序返回答案。

示例 1：
输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。

示例 2：
输入：nums = [3,2,4], target = 6
输出：[1,2]

示例 3：
输入：nums = [3,3], target = 6
输出：[0,1]
 
提示：
2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
只会存在一个有效答案
 
进阶：你可以想出一个时间复杂度小于 O(n2) 的算法吗？
"""
# 简单做法：遍历列表
# def sum_twoSum(nums:list[int], target: int):
#     len_list = len(nums)
#     for i in range(len_list - 1):
#         for j in range(i + 1 , len_list):
#             if nums[i] + nums[j] == target:
#                 return [i,j]

# 进阶算法
def sum_twoSum(nums:list[int], target:int):
    dict = {}  # 建立空字典，存储已经遍历过的值及其下标
    for i in range(len(nums)):
        temp = target - nums[i]   # 计算目标值与当前值的差值
        if temp in dict:   # 在字典中查找是否存在差值
            return [dict[temp],i]
        dict[nums[i]] = i

# 测试：
nums1 = [2, 7, 11, 15]
target1 = 9
nums2 = [3, 2, 4]
target2 = 6
nums3 = [3, 3]
target3 = 6
output1 = sum_twoSum(nums1, target1)
print(output1)
output2 = sum_twoSum(nums2, target2)
print(output2)
output3 = sum_twoSum(nums3, target3)
print(output3)