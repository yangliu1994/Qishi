
class Solution:
    def get_num(self, nums, k):
        left = min(nums)
        right = max(nums)
        less_equal_indices = set()
        flag = 'right'
        while left < right:
            m = int((left + right) / 2)
            self.count_less_equal(nums, m, less_equal_indices, flag)
            if len(less_equal_indices) < k:
                left = m + 1
                flag = 'right'
            else:
                right = m
                flag = 'left'
        return left

    def count_less_equal(self, nums, m, less_equal_indices, flag):
        if flag == 'right':
            for i, num in enumerate(nums):
                if i not in less_equal_indices and num <= m:
                    less_equal_indices.add(i)
        else:
            for i in less_equal_indices.copy():
                if nums[i] > m:
                    less_equal_indices.remove(i)

sol = Solution()
print(sol.get_num([5, 2, 4, 8, 1], 3))
