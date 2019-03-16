
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def build(self, preorder, inorder):
        if inorder:
            root = TreeNode(preorder.pop(0))
            idx = inorder.index(root.val)
            root.left = self.build(preorder, inorder[:idx])
            root.right = self.build(preorder, inorder[idx + 1:])
            return root




sol = Solution()

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]


root = sol.build(preorder, inorder)
print(root.val)
print(root.left.val)
print(root.right.val)
print(root.right.left.val)
print(root.right.right.val)


