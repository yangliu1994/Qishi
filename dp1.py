class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s[0]
        self.cache = {}
        i = 0
        j = len(s)
        a, b = self.dp(s, i, j)
        return s[a:b]

    def dp(self, s, i, j):
        if self.isPalindrome(s, i, j):
            return i, j
        a, b = self.dp(s, i + 1, j)
        c, d = self.dp(s, i, j + 1)
        return (a, b) if b - a > d - c else (c, d)

    def isPalindrome(self, s, i, j):
        print(i, j)
        if i >= j - 1:
            return True
        if (i, j) in self.cache:
            return self.cache[(i, j)]
        if i == j - 2:
            if s[i] == s[j - 1]:
                self.cache[(i, j)] = True
            else:
                self.cache[(i, j)] = False
            return s[i] == s[j - 1]
        if self.isPalindrome(s, i + 1, j - 1) and s[i] == s[j - 1]:
            self.cache[(i, j)] = True
            return True
        else:
            self.cache[(i, j)] = False
            return False

sol = Solution()
print(sol.longestPalindrome('babad'))