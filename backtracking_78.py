
class Solution:
    def subsets(self, nums):
        res = []
        self.helper(nums, [], res, 0)
        return res

    def helper(self, nums, temp, res, i):
        res.append(temp[:])
        for j in range(i, len(nums)):
            temp.append(nums[j])
            self.helper(nums, temp, res, j+1)
            temp.pop()

sol = Solution()
print(sol.subsets([1, 2, 3]))

