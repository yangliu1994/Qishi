
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


def bsf(grid, a, b):
    q = [(a, b)]
    dirs = [-1, 0, 1, 0, -1]
    grid[a][b] = '+'
    while q:
        t = q.pop()
        for i in range(4):
            x = t[0] + dirs[i]
            y = t[1] + dirs[i+1]
            if x >= 0 and x < len(grid) and y >= 0 and y < len(grid[0]) and grid[x][y] == '1':
                q.append((x, y))
                grid[x][y] = '+'


def numIslands(grid):
    res = 0
    m = len(grid)
    if not grid:
        return 0
    n = len(grid[0])
    for i in range(m):
        for j in range(n):
            if grid[i][j] == '1':
                bsf(grid, i, j)
                res += 1
    return res


grid = [list('11110'), list('11010'), list('11000'), list('00000')]

print(numIslands(grid))

grid = [list('11000'), list('11000'), list('00100'), list('00011')]

print(numIslands(grid))


def bsf2(A, q, count, flag):
    dirs = [-1, 0, 1, 0, -1]
    while q:
        count += 1
        length = len(q)
        for i in range(length):
            t = q.pop(0)
            for k in range(4):
                x = t[0] + dirs[k]
                y = t[1] + dirs[k+1]
                if x >= 0 and x < len(A) and y >=0 and y < len(A[0]) and A[x][y] != -1:
                    if flag and A[x][y]:
                        return count
                    if flag and not A[x][y]:
                        q.append((x, y))
                        A[x][y] = -1
                    if not flag and A[x][y]:
                        q.append((x, y))
                        A[x][y] = -1
    return count



def shortestBridge(A):
    res = 0
    m = len(A)
    if not A:
        return res
    n = len(A[0])
    q = []
    for i in range(m):
        for j in range(n):
            if A[i][j] == 1:
                q.append((i, j))
                A[i][j] = -1
                break
        if q:
            break
    bsf2(A, q, res, False)
    res = 0
    for i in range(m):
        for j in range(n):
            if A[i][j] == -1:
                q.append((i, j))
    res = bsf2(A, q, res, True)
    return res - 1

print(shortestBridge([[0,1],[1,0]]))
print(shortestBridge([[0,1,0],[0,0,0],[0,0,1]]))
print(shortestBridge([[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]))


def bsf3(gh, ghin, visit, res):
    q = []
    length = len(ghin)
    for i in range(length):
        if ghin[i] == 0:
            res += 1
            if res == length:
                return res
            q.append(i)
            visit[i] = True
            for j in gh[i]:
                ghin[j] -= 1
    while q:
        t = q.pop(0)
        for i in gh[t]:
            if visit[i] or ghin[i] > 0:
                break
            res += 1
            if res == length:
                return res
            q.append(i)
            visit[i] = True
            for j in gh[i]:
                ghin[j] -= 1
    return res


def canFinish(numCourses, prerequisites):
    gh = [[] for i in range(numCourses)]
    ghin = [0 for i in range(numCourses)]
    for a in prerequisites:
        if a[0] == a[1]:
            return False
        gh[a[1]].append(a[0])
        ghin[a[0]] += 1
    visit = [False for i in range(numCourses)]
    res = 0
    res = bsf3(gh, ghin, visit, res)
    return res == numCourses


print(canFinish(2, [[1,0]] ))
print(canFinish(2, [[1,0],[0,1]]))


def shortestPathAllKeys(grid):
    m = len(grid)
    n = len(grid[0])
    map = [[[False for i in range(64)] for j in range(n)] for k in range(m)]
    q = []
    K = 0
    layer = 0
    dir = {-1, 0, 1, 0, -1}
    for i in range(m):
        for j in range(n):
            if grid[i][j] == '@':
                q.append((i * n + j, 0))
                map[i][j][0] = 1
            if grid[i][j] >= 'a' and grid[i][j] <= 'z':
                K += 1
    while q:
        num = len(q)
        for i in range(num):
            t = q.pop(0)
            a = int(t[0] / n)
            b = t[0] % n
            c = t[1]
            if c == 1 << K - 1:
                return layer
            for j in range(len(dir) - 1):
                x = a + dir[j]
                y = b + dir[j+1]
                z = c
                if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] == '#':
                    continue


