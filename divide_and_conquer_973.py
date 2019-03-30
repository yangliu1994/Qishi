class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        distances = [p[0] ** 2 + p[1] ** 2 for p in points]
        res = self.get_num(distances, K)
        return [points[i] for i in res]

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
        for i, num in enumerate(nums):
            if i not in less_equal_indices and num <= left:
                less_equal_indices.add(i)
        return less_equal_indices

    def count_less_equal(self, nums, m, less_equal_indices, flag):
        if flag == 'right':
            for i, num in enumerate(nums):
                if i not in less_equal_indices and num <= m:
                    less_equal_indices.add(i)
        else:
            for i in less_equal_indices.copy():
                if nums[i] > m:
                    less_equal_indices.remove(i)