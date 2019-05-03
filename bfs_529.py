from typing import List
from collections import deque
class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
            return board
        queue = deque([click])
        while queue:
            row, col = queue.popleft()
            count = 0
            new = deque([])
            for row_change, col_change in ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)):
                if -1 < row+row_change < len(board) and -1 < col+col_change < len(board[0]) and (row+row_change, col+col_change) not in queue:
                    if board[row+row_change][col+col_change] == 'M':
                        count += 1
                    elif count == 0 and board[row+row_change][col+col_change] == 'E':
                        new.append((row+row_change, col+col_change))
            if count > 0:
                board[row][col] = str(count)
            else:
                board[row][col] = 'B'
                queue += new
        return board
