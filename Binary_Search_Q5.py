
def smallest(nums, k):
    def small(guess):
        count = 0
        for l, value_l in enumerate(nums[:-1]):
            for r, value_r in enumerate(nums[l+1:]):
                if value_r - value_l <= guess:
                    count += 1
                else:
                    break
        return count < k

    nums.sort()
    lo = 0
    hi = nums[-1] - nums[0]
    while lo < hi:
        m = lo + int((hi - lo) / 2)
        if small(m):
            lo = m + 1
        else:
            hi = m
    return lo


print(smallest([1,3,1], 1))
print(smallest([1,3,1], 2))
print(smallest([1,3,1], 3))

