
def floodFill(image, sr, sc, newColor):
    q = [(sr, sc)]
    dirs = [-1, 0, 1, 0, -1]
    oldColor = image[sr][sc]
    if oldColor == newColor:
        return image
    image[sr][sc] = newColor
    while q:
        t = q.pop(0)
        for i in range(4):
            x = t[0] + dirs[i]
            y = t[1] + dirs[i+1]
            if x < 0 or x >= len(image) or y < 0 or y >= len(image[0]) or image[x][y] != oldColor:
                continue
            q.append((x, y))
            image[x][y] = newColor
    return image

image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1
sc = 1
newColor = 2
print(floodFill(image, sr, sc, newColor))

print(floodFill([[0,0,0],[0,1,1]], 1, 1, 1))