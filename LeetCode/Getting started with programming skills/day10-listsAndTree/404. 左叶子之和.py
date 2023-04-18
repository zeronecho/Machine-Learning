# https://leetcode.cn/problems/sum-of-left-leaves/?envType=study-plan&id=programming-skills-beginner&plan=programming-skills&plan_progress=x5t930sg

# 给定二叉树的根节点 root ，返回所有左叶子之和。


class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        isLeafNode = lambda node: not node.left and not node.right

        def dfs(node: TreeNode) -> int:
            ans = 0
            if node.left:
                ans += node.left.val if isLeafNode(node.left) else dfs(node.left)
            if node.right and not isLeafNode(node.right):
                ans += dfs(node.right)
            return ans

        return dfs(root) if root else 0

