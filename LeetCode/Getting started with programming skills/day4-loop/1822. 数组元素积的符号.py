# 已知函数 signFunc(x) 将会根据 x 的正负返回特定值：
# 如果 x 是正数，返回 1 。
# 如果 x 是负数，返回 -1 。
# 如果 x 是等于 0 ，返回 0 。
# 给你一个整数数组 nums 。令 product 为数组 nums 中所有元素值的乘积。返回 signFunc(product) 。
class Solution(object):
    def arraySign(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 我的方法
        count = 0
        sorted_nums = sorted(nums)
        for i in range(len(sorted_nums)):
            if sorted_nums[i] == 0:
                return 0
            elif sorted_nums[i] < 0:
                count += 1
            elif sorted_nums[i] > 0:
                break
        if count % 2 != 0:
            return -1
        else:
            return 1

        # # 官方题解
        # sign = 1
        # for num in nums:
        #     if num == 0:
        #         return 0
        #     if num < 0:
        #         sign = -sign
        # return sign

