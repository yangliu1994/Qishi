# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []
        res = []

        def dfs(temp, node):
            temp += str(node.val)
            if not node.left and not node.right:
                res.append(temp)
            if node.left:
                dfs(temp + '->', node.left)
            if node.right:
                dfs(temp + '->', node.right)

        dfs('', root)
        return res