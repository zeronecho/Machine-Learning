# https://leetcode.cn/problems/contains-duplicate/?envType=study-plan&id=programming-skills-beginner&plan=programming-skills&plan_progress=x5t930sg


# 给你一个整数数组 nums 。如果任一值在数组中出现 至少两次 ，返回 true ；如果数组中每个元素互不相同，返回 false 。

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num_set = set()
        for num in nums:
            if num in num_set:
                return True
            num_set.add(num)
        return False

# 这段代码使用了一个set数据结构来记录已经出现过的数字，如果某个数字已经在set中出现过了，则说明存在重复元素，返回True，否则将该数字添加到set中。
# 遍历完整个数组后都没有找到重复元素，则返回False。