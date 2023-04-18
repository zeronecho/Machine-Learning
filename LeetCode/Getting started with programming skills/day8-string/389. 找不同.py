# https://leetcode.cn/problems/find-the-difference/?envType=study-plan&id=programming-skills-beginner&plan=programming-skills&plan_progress=x5t930sg

# 给定两个字符串 s 和 t ，它们只包含小写字母。
# 字符串 t 由字符串 s 随机重排，然后在随机位置添加一个字母。
# 请找出在 t 中被添加的字母。

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        count = [0] * 26
        for ch in s:
            count[ord(ch) - ord('a')] += 1
        for ch in t:
            count[ord(ch) - ord('a')] -= 1
            if count[ord(ch) - ord('a')] < 0:
                return ch

# 可以通过计算每个字符在字符串 t 和字符串 s 中出现的次数，然后比较它们的差异来找到被添加的字母。
# 具体地，可以用一个列表 count 记录字符串 s 中每个字符出现的次数，然后遍历字符串 t 中的每个字符，将 count 中对应字符的计数器减去 1。最后，count 中剩下的计数器就对应着被添加的字符。
# 在上面的代码中，ord(ch) - ord('a') 的值代表字符 ch 对应的在列表 count 中的索引。第一个循环用于计算 s 中每个字符出现的次数，第二个循环用于更新 count 列表并找到被添加的字符。