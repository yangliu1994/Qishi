
class Solution:
    def partition(self, s):
        res = []
        self.helper(s, [], res, 0)
        return res

    def helper(self, s, temp, res, i):
        if len(s) == i:
            res.append(temp[:])
            return
        for j in range(i, len(s)):
            if self.isPalindrome(s, i, j):
                temp.append(s[i:j+1])
                self.helper(s, temp, res, j+1)
                temp.pop()

    def isPalindrome(self, s, i, j):
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

sol = Solution()
print(sol.partition('aab'))
print(sol.partition('aabba'))
