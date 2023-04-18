# https://leetcode.cn/problems/middle-of-the-linked-list/?envType=study-plan&id=programming-skills-beginner&plan=programming-skills&plan_progress=x5t930sg

# 给你单链表的头结点 head ，请你找出并返回链表的中间结点。
#
# 如果有两个中间结点，则返回第二个中间结点。

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        A = [head]
        while A[-1].next:
            A.append(A[-1].next)
        return A[len(A) // 2]
