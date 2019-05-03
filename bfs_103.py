# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res = []
        queue = [root]
        flag = 1
        while queue:
            vals = []
            new = []
            for node in queue:
                vals.append(node.val)
                if node.left:
                    new.append(node.left)
                if node.right:
                    new.append(node.right)
            if flag == 1:
                res.append(vals)
            else:
                res.append(vals[::-1])
            queue = new
            flag = -flag
        return res
