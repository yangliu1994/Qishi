
class Solution:
    def solveNQueens(self, n):
        board = [['.'] * n for _ in range(n)]
        marks = [['1'] * n for _ in range(n)]
        res = []
        self.dfs(0, board, marks, res)
        return res

    def dfs(self, i, board, marks, res):
        if i == len(board):
            res.append([''.join(row) for row in board])
            return
        for j, _ in enumerate(board):
            if marks[i][j] == '1':
                board[i][j] = 'Q'
                marks0 = [row[:] for row in marks]
                self.update_marks(i, j, marks)
                self.dfs(i+1, board, marks, res)
                board[i][j] = '.'
                marks = marks0

    def update_marks(self, i, j, marks):
        for x in range(i+1, len(marks)):
            for y, _ in enumerate(marks):
                if y == j or abs(x - i) == abs(y - j):
                    marks[x][y] = '0'

sol = Solution()
print(sol.solveNQueens(4))




