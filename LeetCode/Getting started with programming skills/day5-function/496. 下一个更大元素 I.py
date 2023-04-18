# nums1 中数字 x 的 下一个更大元素 是指 x 在 nums2 中对应位置 右侧 的 第一个 比 x 大的元素。
# 给你两个 没有重复元素 的数组 nums1 和 nums2 ，下标从 0 开始计数，其中nums1 是 nums2 的子集。
# 对于每个 0 <= i < nums1.length ，找出满足 nums1[i] == nums2[j] 的下标 j ，并且在 nums2 确定 nums2[j] 的 下一个更大元素 。如果不存在下一个更大元素，那么本次查询的答案是 -1 。
# 返回一个长度为 nums1.length 的数组 ans 作为答案，满足 ans[i] 是如上所述的 下一个更大元素 。

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        m, n = len(nums1), len(nums2)
        res = [0] * m
        for i in range(m):
            j = nums2.index(nums1[i])
            k = j + 1
            while k < n and nums2[k] < nums2[j]:
                k += 1
            res[i] = nums2[k] if k < n else -1
        return res

    # # 法二：使用单调栈+哈希表
    # def nextGreaterElement(self, nums1, nums2):
    #     stack = []
    #     next_greater = {}
    #     for num in nums2:
    #         while stack and num > stack[-1]:
    #             next_greater[stack.pop()] = num
    #         stack.append(num)
    #     return [next_greater.get(num, -1) for num in nums1]

    # # 力扣官方题解法二：使用单调栈+哈希表
    # class Solution:
    #     def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
    #         res = {}
    #         stack = []
    #         for num in reversed(nums2):
    #             while stack and num >= stack[-1]:
    #                 stack.pop()
    #             res[num] = stack[-1] if stack else -1
    #             stack.append(num)
    #         return [res[num] for num in nums1]

