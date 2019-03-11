class Solution:
    def bsf(self, board, i, j):
        q = [(i, j)]
        change = [(i, j)]
        dirs = [-1, 0, 1, 0, -1]
        while q:
            t = q.pop(0)
            for k in range(4):
                x = t[0] + dirs[k]
                y = t[1] + dirs[k+1]
                if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]):
                    return
                if board[x][y] == 'O' and (x, y) not in change:
                    q.append((x, y))
                    change.append((x, y))
        for (x, y) in change:
            board[x][y] = 'X'

    def solve(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O':
                    self.bsf(board, i, j)