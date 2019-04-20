

print((2147483648+ 2 ** 31) % 2 ** 32 - 2 ** 31)

print(2 ** 31)

class Solution(object):
    def singleNumber(self, nums):
        one, two = 0, 0
        for x in nums:
            one, two, three = one ^ x, two | (one & x), two & x
            print(one, two, three)
            one, two = one & ~three, two & ~three
            print(one, two)
        return one

print(Solution().singleNumber([2, 3, 2, 2]))




# NOT

assert ~7 == -8
assert ~(-8) == 7

# AND

assert 1 & 1 == 1
assert 3 & 3 == 3
assert 100 & 100 == 100

assert 100 & 0 == 0

assert 6 & 2 == 2

# OR

assert 1 | 0 == 1
assert 100 | 0 == 100

assert 100 | 1 == 101

# XOR

assert 1 ^ 0 == 1
assert 0 ^ 1 == 1
assert 0 ^ 0 == 0
assert 1 ^ 1 == 0

assert 100 ^ 0 == 100
assert 0 ^ 100 == 100
assert 100 ^ 100 == 0

assert (100 ^ 1000 ^ 10000) == 10000 ^ 100 ^ 1000



