
class Solution:
    def exist(self, board, word):
        if len(word) > len(board) * len(board[0]):
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if self.helper(board, i, j, word):
                        return True
        return False

    def helper(self, board, i, j, word):
        if not word:
            return True
        if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or board[i][j] != word[0]:
            return False
        a = word[0]
        board[i][j] = '#'
        res = self.helper(board, i+1, j, word[1:]) or \
            self.helper(board, i-1, j, word[1:]) or \
            self.helper(board, i, j+1, word[1:]) or \
            self.helper(board, i, j-1, word[1:])
        board[i][j] = a
        return res


sol = Solution()
print(
sol.exist([
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
], "ABCCED")
)

print(
sol.exist([
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
], "SEE")
)

print(
sol.exist([
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
], "ABCB")
)