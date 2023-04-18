# 给你一个整数 n，请你帮忙计算并返回该整数「各位数字之积」与「各位数字之和」的差。

class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """

        # # 法一：
        # str_n = str(n)
        # digits = []
        # sum_n = 0
        # product_n = 1
        # for i in str_n:
        #     digits.append(int(i))
        #     sum_n += int(i)
        #     product_n *= int(i)
        # return product_n - sum_n

        # 官方题解
        add, mul = 0, 1
        while n > 0:
            digit = n % 10
            n //= 10
            add += digit
            mul *= digit
        return mul - add
