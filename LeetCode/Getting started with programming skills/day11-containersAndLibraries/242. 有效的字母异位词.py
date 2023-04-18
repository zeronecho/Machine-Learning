# https://leetcode.cn/problems/valid-anagram/?envType=study-plan&id=programming-skills-beginner&plan=programming-skills&plan_progress=x5t930sg

# 给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。
#
# 注意：若 s 和 t 中每个字符出现的次数都相同，则称 s 和 t 互为字母异位词。

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        counter = {}
        for char in s:
            counter[char] = counter.get(char, 0) + 1
        for char in t:
            counter[char] = counter.get(char, 0) - 1
            if counter[char] < 0:
                return False
        return True

# 可以通过哈希表来实现，先统计字符串 s 中每个字符出现的次数，再遍历字符串 t，对于每个字符在哈希表中减去出现的次数.
# 如果哈希表中的计数器为负数，则说明 t 中出现了 s 中没有的字符，返回 False，否则返回 True。

# 这里使用了字典来记录字符出现的次数，counter.get(char, 0) 表示从字典中获取 char 对应的值，如果 char 不存在，则返回默认值 0。
# 第一个循环遍历 s，统计每个字符出现的次数；第二个循环遍历 t，对于每个字符在哈希表中减去出现的次数，如果出现负数，则说明 t 中出现了 s 中没有的字符，返回 False。
# 如果两个字符串长度不相等，则说明它们不可能是字母异位词，直接返回 False。