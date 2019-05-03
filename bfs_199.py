# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        queue = deque([root])
        res = []
        while queue:
            res.append(queue[-1].val)
            new = deque([])
            for node in queue:
                if node.left:
                    new.append(node.left)
                if node.right:
                    new.append(node.right)
            queue = new
        return res