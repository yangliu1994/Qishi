
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        self.helper(candidates, target, [], res)
        return res

    def helper(self, candidates, target, temp, res):
        if sum(temp) > target:
            return
        if sum(temp) == target:
            res.append(temp[:])
            return
        for i in range(len(candidates)):
            temp.append(candidates[i])
            self.helper(candidates[i:], target, temp, res)
            temp.pop()