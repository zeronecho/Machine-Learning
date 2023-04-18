# 给你长度相等的两个字符串 s1 和 s2 。一次 字符串交换 操作的步骤如下：选出某个字符串中的两个下标（不必不同），并交换这两个下标所对应的字符。
# 如果对 其中一个字符串 执行 最多一次字符串交换 就可以使两个字符串相等，返回 true ；否则，返回 false 。

class Solution(object):
    def areAlmostEqual(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if s1 == s2:
            return True

        if len(s1) != len(s2):
            return False

        # 找到两个字符串中不同字符的位置
        diff = []
        for i, (c1, c2) in enumerate(zip(s1, s2)):
            if c1 != c2:
                diff.append(i)
                if len(diff) > 2:
                    return False

        # 如果只有一处不同，不可能通过交换相同的字符来使两个字符串相同
        if len(diff) == 1:
            return False

        # 如果没有不同或者有两处不同，但可以通过交换来变成相同，则返回 True
        if len(diff) == 0 or len(diff) == 2 and s1[diff[0]] == s2[diff[1]] and s1[diff[1]] == s2[diff[0]]:
            return True

        return False

        # # 官方题解
        # def areAlmostEqual(self, s1: str, s2: str) -> bool:
        #     i = j = -1
        #     for idx, (x, y) in enumerate(zip(s1, s2)):
        #         if x != y:
        #             if i < 0:
        #                 i = idx
        #             elif j < 0:
        #                 j = idx
        #             else:
        #                 return False
        #     return i < 0 or j >= 0 and s1[i] == s2[j] and s1[j] == s2[i]

