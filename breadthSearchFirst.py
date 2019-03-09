
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def levelOrder(root):
    res = []
    if not root:
        return res
    q = []
    q.append(root)
    while q:
        length = len(q)
        level = []
        for i in range(length):
            t = q[0]
            q.pop(0)
            level.append(t.val)
            if t.left:
                q.append(t.left)
            if t.right:
                q.append(t.right)
        res.append(level)
    return res

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print(levelOrder(root))
