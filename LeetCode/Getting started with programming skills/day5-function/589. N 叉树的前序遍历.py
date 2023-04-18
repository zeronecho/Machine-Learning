
# 给定一个 n 叉树的根节点  root ，返回 其节点值的 前序遍历 。
# n 叉树 在输入中按层序遍历进行序列化表示，每组子节点由空值 null 分隔。



"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []

class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """

        if not root:
            return []
        res = [root.val]
        for child in root.children:
            res.extend(self.preorder(child))
        return res

# # 官方题解
# class Solution:
#     def preorder(self, root: 'Node') -> List[int]:
#         ans = []
#         def dfs(node: 'Node'):
#             if node is None:
#                 return
#             ans.append(node.val)
#             for ch in node.children:
#                 dfs(ch)
#         dfs(root)
#         return ans
