# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        def dfs(node):
            left = dfs(node.left) if node.left else []
            right = dfs(node.right) if node.right else []
            return [node.val] + left + right

        return dfs(root)