from collections import deque
from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        queue = deque([])
        for i in range(len(board)):
            if board[i][0] == 'O':
                queue.append((i, 0))
            if board[i][-1] == 'O':
                queue.append((i, len(board[0]) - 1))
        for i in range(1, len(board[0]) - 1):
            if board[0][i] == 'O':
                queue.append((0, i))
            if board[-1][i] == 'O':
                queue.append((len(board) - 1, i))
        while queue:
            row, col = queue.popleft()
            board[row][col] = 'D'
            for row_change, col_change in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                if -1 < row + row_change < len(board) and -1 < col + col_change < len(board[0]) and \
                        board[row + row_change][col + col_change] == 'O':
                    queue.append((row + row_change, col + col_change))
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'D':
                    board[i][j] = 'O'
