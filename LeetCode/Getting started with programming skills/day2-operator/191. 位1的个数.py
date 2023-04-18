# 编写一个函数，输入是一个无符号整数（以二进制串的形式），返回其二进制表达式中数字位数为 '1' 的个数（也被称为汉明重量）。

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """

        # # 法一
        # count = 0
        # digits = [int(d) for d in str(bin(n))[2:]]
        # for digit in digits:
        #     if digit == 1:
        #         count += 1
        # return count

        # 法二
        count = 0
        while n>0:
            if n&1 == 1:
                count += 1
            n>>=1
        return count


