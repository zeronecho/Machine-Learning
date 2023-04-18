# 给你一个整数数组 salary ，数组里每个数都是 唯一 的，其中 salary[i] 是第 i 个员工的工资。
# 请你返回去掉最低工资和最高工资以后，剩下员工工资的平均值。

class Solution(object):
    def average(self, salary):
        """
        :type salary: List[int]
        :rtype: float
        """

        max_val = max(salary)
        min_val = min(salary)

        total_val = sum(salary)
        total_val2 = total_val - max_val - min_val

        length = len(salary)

        ans = float(total_val2) / float(length - 2)
        return ans
