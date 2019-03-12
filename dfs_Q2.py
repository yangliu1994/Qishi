
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def paths(self, root, s):
        res = []
        current = [root.val]
        self.dfs(res, current, root, s)
        return res

    def dfs(self, res, current, root, s):
        if not root.left and not root.right:
            if sum(current) == s:
                res.append(current)
            return
        if root.left:
            self.dfs(res, current + [root.left.val], root.left, s)
        if root.right:
            self.dfs(res, current + [root.right.val], root.right, s)

sol = Solution()

root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(8)
root.left.left = TreeNode(11)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)
root.right.right.left = TreeNode(5)
root.right.right.right = TreeNode(1)

print(sol.paths(root, 22))
