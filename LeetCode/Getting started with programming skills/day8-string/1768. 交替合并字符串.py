# https://leetcode.cn/problems/merge-strings-alternately/?envType=study-plan&id=programming-skills-beginner&plan=programming-skills&plan_progress=x5t930sg

# 给你两个字符串 word1 和 word2 。请你从 word1 开始，通过交替添加字母来合并字符串。如果一个字符串比另一个字符串长，就将多出来的字母追加到合并后字符串的末尾。
# 返回 合并后的字符串 。

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        m, n = len(word1), len(word2)
        i = j = 0

        ans = list()
        while i < m or j < n:
            if i < m:
                ans.append(word1[i])
                i += 1
            if j < n:
                ans.append(word2[j])
                j += 1

        return "".join(ans)
