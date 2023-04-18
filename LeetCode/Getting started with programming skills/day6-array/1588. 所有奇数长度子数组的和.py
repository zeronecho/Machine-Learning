# 给你一个正整数数组 arr ，请你计算所有可能的奇数长度子数组的和。
# 子数组 定义为原数组中的一个连续子序列。
# 请你返回 arr 中 所有奇数长度子数组的和 。

class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """

        result = 0
        for i in range(len(arr)):
            for j in range(i, len(arr), 2):
                result += sum(arr[i:j+1])
        return result
