# 给你一个字符串 s，它由数字（'0' - '9'）和 '#' 组成。我们希望按下述规则将 s 映射为一些小写英文字符：#
# 字符（'a' - 'i'）分别用（'1' - '9'）表示。
# 字符（'j' - 'z'）分别用（'10#' - '26#'）表示。
# 返回映射之后形成的新字符串。题目数据保证映射始终唯一。

class Solution:

    # 逆序遍历
    def freqAlphabets(self, s: str) -> str:
        def get(st):
            return chr(int(st) + 96)

        i, ans = len(s) - 1, ""
        while i >= 0:
            if s[i] == '#':
                ans += get(s[i - 2:i])
                i -= 3
            else:
                ans += get(s[i])
                i -= 1
        return ans[::-1]

    # # 官方题解：顺序遍历
    # def freqAlphabets(self, s: str) -> str:
    #     def get(st):
    #         return chr(int(st) + 96)
    #
    #     i, ans = 0, ""
    #     while i < len(s):
    #         if i + 2 < len(s) and s[i + 2] == '#':
    #             ans += get(s[i : i + 2])
    #             i += 2
    #         else:
    #             ans += get(s[i])
    #         i += 1
    #     return ans

