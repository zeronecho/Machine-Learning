# 给定二叉树的根节点 root ，返回所有左叶子之和。

class Solution:

    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0

        # 递归函数，判断当前节点是否是左叶子节点，并返回左叶子节点的值
        def isLeftLeaf(node):
            if node.left and not node.left.left and not node.left.right:
                return node.left.val
            return 0

        # 递归遍历二叉树，累加左叶子节点的值
        def dfs(node):
            if not node:
                return 0
            left_leaf_sum = isLeftLeaf(node)  # 判断当前节点是否是左叶子节点
            return left_leaf_sum + dfs(node.left) + dfs(node.right)  # 递归遍历左子树和右子树

        return dfs(root)

    # # 官方题解
    # def sumOfLeftLeaves(self, root: TreeNode) -> int:
    #     isLeafNode = lambda node: not node.left and not node.right
    #
    #     def dfs(node: TreeNode) -> int:
    #         ans = 0
    #         if node.left:
    #             ans += node.left.val if isLeafNode(node.left) else dfs(node.left)
    #         if node.right and not isLeafNode(node.right):
    #             ans += dfs(node.right)
    #         return ans
    #
    #     return dfs(root) if root else 0

