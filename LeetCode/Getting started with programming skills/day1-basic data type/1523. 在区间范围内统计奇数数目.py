# 1523. 在区间范围内统计奇数数目
# 给你两个非负整数 low 和 high 。请你返回 low 和 high 之间（包括二者）奇数的数目。

class Solution(object):
    def countOdds(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """
        if low % 2 == 0:
            low += 1
        if high % 2 == 0:
            high -= 1
        return (high - low) // 2 + 1