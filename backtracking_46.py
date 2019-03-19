
class Solution:
    def permute(self, nums):
        res = []
        self.helper(nums, [], res)
        return res

    def helper(self, nums, temp, res):
        if len(nums) == len(temp):
            res.append(temp[:])
            return res
        for num in nums:
            if num in temp:
                continue
            temp.append(num)
            self.helper(nums, temp, res)
            temp.pop()

sol = Solution()
print(sol.permute([1, 2, 3]))
