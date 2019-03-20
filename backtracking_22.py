
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        self.helper(n, n, [], res)
        return res
    def helper(self, n, m, temp, res):
        if n == 0:
            res.append(''.join(temp) + ')' * m)
            return
        temp.append('(')
        self.helper(n-1, m, temp, res)
        temp.pop()
        if n < m:
            temp.append(')')
            self.helper(n, m-1, temp, res)
            temp.pop()
