# https://leetcode.cn/problems/sort-integers-by-the-number-of-1-bits/?envType=study-plan&id=programming-skills-beginner&plan=programming-skills&plan_progress=x5t930sg

# 给你一个整数数组 arr 。请你将数组中的元素按照其二进制表示中数字 1 的数目升序排序。
#
# 如果存在多个数字二进制中 1 的数目相同，则必须将它们按照数值大小升序排列。
#
# 请你返回排序后的数组。

class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def bit_count(n):
            count = 0
            while n:
                count += n & 1
                n >>= 1
            return count

        return sorted(arr, key=lambda x: (bit_count(x), x))

# 可以使用Python内置函数sorted()，并自定义排序规则来实现题目要求。
# 首先，定义一个函数bit_count，用于计算数字中1的个数，然后使用lambda表达式将排序规则指定为先按1的个数排序，再按数值大小排序。
# 最后，使用sorted()函数进行排序并返回结果即可。