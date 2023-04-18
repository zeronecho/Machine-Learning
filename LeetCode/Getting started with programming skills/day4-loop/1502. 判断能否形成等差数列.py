# 给你一个数字数组 arr 。
# 如果一个数列中，任意相邻两项的差总等于同一个常数，那么这个数列就称为 等差数列 。
# 如果可以重新排列数组形成等差数列，请返回 true ；否则，返回 false 。

class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """

        # 法一
        sorted_arr = sorted(arr)
        diff = sorted_arr[1] - sorted_arr[0] # 计算公差
        for i in range(1, len(sorted_arr)):
            if sorted_arr[i] - sorted_arr[i-1] != diff:
                return False
        return True

        # # 官方题解：
        # def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        #     arr.sort()
        #     for i in range(1, len(arr) - 1):
        #         if arr[i] * 2 != arr[i - 1] + arr[i + 1]:
        #             return False
        #     return True

        # 注：第一种方法使用了差分的思想，计算公差，然后检查相邻两项的差是否为公差，而第二种方法则是直接计算中间项是否等于前后两项的平均数。
        # 第一种方法的时间复杂度为O(nlogn)，因为需要排序，而第二种方法的时间复杂度为O(n)，因为直接遍历数组。对于大规模数据的处理，O(nlogn)算法的效率更高。


