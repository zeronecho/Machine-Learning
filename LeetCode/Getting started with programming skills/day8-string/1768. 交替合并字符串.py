# 给你两个字符串 word1 和 word2 。请你从 word1 开始，通过交替添加字母来合并字符串。如果一个字符串比另一个字符串长，就将多出来的字母追加到合并后字符串的末尾。
# 返回 合并后的字符串 。

class Solution:

    def mergeAlternately(self, word1: str, word2: str) -> str:
        i, j = 0, 0
        res = ''
        while i < len(word1) and j < len(word2):
            res += word1[i] + word2[j]
            i += 1
            j += 1
        if i < len(word1):
            res += word1[i:]
        if j < len(word2):
            res += word2[j:]
        return res

    # #官方题解：双指针问题 思路大致相同
    # def mergeAlternately(self, word1: str, word2: str) -> str:
    #     m, n = len(word1), len(word2)
    #     i = j = 0
    #
    #     ans = list()
    #     while i < m or j < n:
    #         if i < m:
    #             ans.append(word1[i])
    #             i += 1
    #         if j < n:
    #             ans.append(word2[j])
    #             j += 1
    #
    #     return "".join(ans)
