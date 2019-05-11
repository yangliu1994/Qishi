class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        res = 0
        dp = [[0 for _ in range(n)] for _ in range(m)]

        def dfs(i, j):
            if dp[i][j] > 0:
                return dp[i][j]
            temp = matrix[i][j]
            res_ = 0
            for row, col in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                if -1 < row < m and -1 < col < n and temp < matrix[row][col]:
                    res_ = max(res_, dfs(row, col))
            dp[i][j] = res_ + 1
            return res_ + 1

        for i in range(m):
            for j in range(n):
                res = max(res, dfs(i, j))
        return res