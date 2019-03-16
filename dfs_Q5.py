
class Solution(object):
    def longestIncreasingPath(self, matrix):
        if not matrix or not matrix[0]:
            return 0
        res = 0
        n = len(matrix)
        m = len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        for i in range(n):
            for j in range(m):
                res = max(res, self.dfs(matrix, dp, i, j))
        return res

    def dfs(self, matrix, dp, i, j):
        if dp[i][j] != 0:
            return dp[i][j]
        for x, y in {(i-1, j), (i+1, j), (i, j-1), (i, j+1)}:
            if 0 <= x < len(matrix) and 0 <=y < len(matrix[0]):
                dp[i][j] = max(dp[i][j], self.dfs(matrix, dp, i, j))
        dp[i][j] = dp[i][j] + 1
        return dp[i][j]


class Solution2(object):
    def longestIncreasingPath(self, matrix):
        if not matrix or not matrix[0]:
            return 0
        res = 0
        n = len(matrix)
        m = len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        for i in range(n):
            for j in range(m):
                res = max(res, self.dfs(matrix, dp, i, j))
        return res

    def dfs(self, matrix, dp, i, j):
        if dp[i][j] != 0:
            return dp[i][j]
        for x, y in {(i-1, j), (i+1, j), (i, j-1), (i, j+1)}:
            if 0 <= x < len(matrix) and 0 <=y < len(matrix[0]):
                dp[i][j] = max(dp[i][j], self.dfs(matrix, dp, i, j))
        dp[i][j] = dp[i][j] + 1
        return dp[i][j]