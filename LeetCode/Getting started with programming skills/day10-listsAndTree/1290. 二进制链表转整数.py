# https://leetcode.cn/problems/convert-binary-number-in-a-linked-list-to-integer/?envType=study-plan&id=programming-skills-beginner&plan=programming-skills&plan_progress=x5t930sg

# 给你一个单链表的引用结点 head。链表中每个结点的值不是 0 就是 1。已知此链表是一个整数数字的二进制表示形式。
#
# 请你返回该链表所表示数字的 十进制值 。

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        cur = head
        ans = 0
        while cur:
            ans = ans * 2 + cur.val
            cur = cur.next
        return ans

