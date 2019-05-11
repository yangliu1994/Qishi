class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])

        def dfs(visited, i, j, w):
            if len(w) == 1:
                return True
            visited.add((i, j))
            for row, col in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                if -1 < row < m and -1 < col < n and (row, col) not in visited and board[row][col] == w[1] and dfs(
                        visited.copy(), row, col, w[1:]):
                    return True
            return False

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and dfs(set(), i, j, word):
                    return True
        return False