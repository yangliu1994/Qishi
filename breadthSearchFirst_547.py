
def bsf(grid, friends, i):
    q = [i]
    friends[i] = True
    while q:
        t = q.pop(0)
        for j in range(len(grid)):
            if grid[t][j] != 1 or t == j or friends[j]:
                continue
            q.append(j)
            friends[j] = True


def friendCircles(grid):
    res = 0
    friends = [False for i in range(len(grid))]
    for i in range(len(grid)):
        if friends[i]:
            continue
        else:
            bsf(grid, friends, i)
            res += 1
    return res


print(friendCircles([[1,1,0],
[1,1,0],
[0,0,1]]))

print(friendCircles([[1,1,0],
[1,1,1],
[0,1,1]]))

print(friendCircles([[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]]))
