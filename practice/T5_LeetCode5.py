# 题目内容：
"""
给定一个长度为 n 的整数数组 height 。有 n 条垂线，第 i 条线的两个端点是 (i, 0) 和 (i, height[i]) 。
找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
返回容器可以储存的最大水量。
说明：你不能倾斜容器。

示例 1：
输入：[1,8,6,2,5,4,8,3,7]
输出：49 
解释：图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。

示例 2：
输入：height = [1,1]
输出：1
"""

# 实现思路：
"""
本质为：求(right - left) * min(height[left], height[right])的最大值，其中 left 和 right 分别为左右两条线的索引。
Step1：设置左右各一个指针，分别指向数组的两端，计算当前面积，并更新最大面积。
Step2：移动指针，移动较短的那条线的指针，因为移动较长的线不会增加面积。
"""

def  maxArea(height: list[int]):
    left, right = 0, len(height) - 1
    max_area = 0
    while left < right:
        area = (right - left) * min(height[left], height[right])
        max_area = max(max_area, area)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_area

height1 = [1,8,6,2,5,4,8,3,7]
print(maxArea(height1))  # 输出：49
height2 = [1,1]
print(maxArea(height2))  # 输出：1