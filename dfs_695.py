class Solution:
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        res = 0

        def dfs(i, j):
            grid[i][j] = 0
            temp = 1
            for row, col in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                if -1 < row < m and -1 < col < n and grid[row][col]:
                    temp += dfs(row, col)
            return temp

        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    res = max(res, dfs(i, j))
        return res
