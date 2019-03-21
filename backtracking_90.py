class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        self.helper(nums, [], res, 0)
        return res

    def helper(self, nums, temp, res, i):
        if temp not in res:
            res.append(temp[:])
        for j in range(i, len(nums)):
            temp.append(nums[j])
            self.helper(nums, temp, res, j + 1)
            temp.pop()
        return