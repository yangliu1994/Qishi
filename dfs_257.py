

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def binaryTreePaths(self, root):
        if not root:
            return []
        res = []
        self.dfs(root, '', res)
        return res

    def dfs(self, root, ls, res):
        if not root.left and not root.right:
            res.append(ls + str(root.val))
        if root.left:
            self.dfs(root.left, ls + str(root.val) + '->', res)
        if root.right:
            self.dfs(root.right, ls + str(root.val) + '->', res)

    def binaryTreePaths1(self, root):
        if not root:
            return []
        res, stack = [], [(root, '')]
        while stack:
            node, ls = stack.pop()
            if not node.left and not node.right:
                res.append(ls + str(node.val))
            else:
                if node.left:
                    stack.append((node.left, ls + str(node.val) + '->'))
                if node.right:
                    stack.append((node.right, ls + str(node.val) + '->'))
        return res


sol = Solution()

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print(sol.binaryTreePaths(root))
print(sol.binaryTreePaths1(root))
