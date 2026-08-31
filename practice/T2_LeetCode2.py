# 题目内容
"""
给你一个字符串数组，请你将 字母异位词 组合在一起。可以按任意顺序返回结果列表。
 
示例 1:
输入: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
输出: [["bat"],["nat","tan"],["ate","eat","tea"]]

解释：
在 strs 中没有字符串可以通过重新排列来形成 "bat"。
字符串 "nat" 和 "tan" 是字母异位词，因为它们可以重新排列以形成彼此。
字符串 "ate" ，"eat" 和 "tea" 是字母异位词，因为它们可以重新排列以形成彼此。

示例 2:
输入: strs = [""]
输出: [[""]]

示例 3:
输入: strs = ["a"]
输出: [["a"]]

提示：
1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] 仅包含小写字母
"""
# 实现思路：
# 异位词的本质为：组成字母几个字数量都相同。
# 核心为满足上述本质的映射到同一个key
# 使用sorted函数可以对字符串进行排序
def groupAnagrams(strs: list[str]):
    dict = {}
    for s in strs:
        sort_strs = "".join(sorted(s))
        if sort_strs in dict:
            dict[sort_strs].append(s)
        else:
            dict[sort_strs] = [s]
    return list(dict.values())




strs1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
strs2 = [""]
strs3 = ["a"]
output1 = groupAnagrams(strs1)
print(output1)
output2 = groupAnagrams(strs2)
print(output2)
output3 = groupAnagrams(strs3)
print(output3)

# strs = 'helloworld'
# print(tuple(strs))
# print(tuple(set(strs)))
# print(set(strs) == set(strs))
# print("".join(sorted(strs)))
