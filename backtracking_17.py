
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        self.phone = {'2': ['a', 'b', 'c'],
                      '3': ['d', 'e', 'f'],
                      '4': ['g', 'h', 'i'],
                      '5': ['j', 'k', 'l'],
                      '6': ['m', 'n', 'o'],
                      '7': ['p', 'q', 'r', 's'],
                      '8': ['t', 'u', 'v'],
                      '9': ['w', 'x', 'y', 'z']}
        if not digits:
            return []
        res = []
        self.backtracking(digits, [], res)
        return res

    def backtracking(self, digits, temp, res):
        if not digits:
            res.append(''.join(temp))
            return
        for word in self.phone[digits[0]]:
            temp.append(word)
            self.backtracking(digits[1:], temp, res)
            temp.pop()