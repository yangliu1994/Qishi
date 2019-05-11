# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, s: int) -> List[List[int]]:
        if not root:
            return []
        res = []

        def dfs(node, temp):
            temp.append(node.val)
            if not node.left and not node.right and sum(temp) == s:
                res.append(temp[:])
            if node.left:
                dfs(node.left, temp[:])
            if node.right:
                dfs(node.right, temp[:])

        dfs(root, [])
        return res
