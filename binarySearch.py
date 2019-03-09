
def binarySearch(lst, x):
    l = 0
    r = len(lst) - 1
    while l <= r:
        m = l + int((r - l) / 2)
        if lst[m] == x:
            return m
        elif lst[m] < x:
            l = m + 1
        else:
            r = m - 1
    return -1

print(binarySearch([1, 2, 3], 3))
print(binarySearch([1, 2, 3, 4, 5], 3))
print(binarySearch([1, 2, 3, 4, 5], 2.5))

def my_upper_bound(lst, x):
    l = 0
    r = len(lst) - 1
    while l < r:
        m = l + int((r - l) / 2)
        if lst[m] <= x:
            l = m + 1
        else:
            r = m
    return l

print(my_upper_bound([1, 2, 3], 3))
print(my_upper_bound([1, 2, 3, 3, 4, 5], 3))
print(my_upper_bound([1, 2, 3, 4, 5], 2.5))


def my_lower_bound(lst, x):
    l = 0
    r = len(lst) - 1
    while l < r:
        m = l + int((r - l) / 2)
        if lst[m] < x:
            l = m + 1
        else:
            r = m
    return l

print(my_lower_bound([1, 2, 3], 3))
print(my_lower_bound([1, 2, 3, 3, 4, 5], 3))
print(my_lower_bound([1, 2, 3, 4, 5], 2.5))


def firstBadVersion(lst):
    l = 0
    r = len(lst) - 1
    while l < r:
        m = l + int((r - l) / 2)
        if lst[m]:
            l = m + 1
        else:
            r = m
    return l

print(firstBadVersion([True, True, True, True, False, False]))

def searchInsert(nums, target):
    if not nums:
        return -1
    l = 0
    r = len(nums)
    while l < r:
        m = l + int((r - l) / 2)
        if nums[m] == target:
            return m
        elif nums[m] < target:
            l = m + 1
        else:
            r = m
    return l

print(searchInsert([1,3,5,6], 5))
print(searchInsert([1,3,5,6], 2))
print(searchInsert([1,3,5,6], 7))
print(searchInsert([1,3,5,6], 0))

def mySqrt(x):
    l = 0
    r = x
    while l < r:
        m = l + int((r - l) / 2)
        if m * m == x:
            return m
        elif m * m < x:
            l = m + 1
        else:
            r = m
    return l - 1

print('mySqrt')
print(mySqrt(8))
print(mySqrt(10))
print(mySqrt(15))

def findDuplicate(nums):
    l = 0
    r = len(nums) + 1
    while l < r:
        m = l + int((r - l) / 2)
        count = 0
        for num in nums:
            if num < m:
                count += 1
        if count < m:
            l = m + 1
        else:
            r = m
    return l - 1

print('Duplicates')
print(findDuplicate([4, 3, 3, 1, 2]))
print(findDuplicate([4, 2, 3, 3, 3, 6, 5]))


def lowerEqualCount(nums, target):
    l = 0
    r = len(nums)
    while l < r:
        m = l + int((r - l) / 2)
        if nums[m] <= target:
            l = m + 1
        else:
            r = m
    return l

def kthSmallest(matrix, k):
    n = len(matrix)
    l = matrix[0][0]
    r = matrix[n-1][n-1]
    while l < r:
        m = l + int((r - l) / 2)
        count = 0
        for row in matrix:
            count += lowerEqualCount(row, m)
        if count < k:
            l = m + 1
        else:
            r = m
    return l


matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
]
k = 8

print('k-th')
print(kthSmallest(matrix, k))

matrix = [
[1, 2, 2],
[2, 3, 4]
]
print(kthSmallest(matrix, 2))
print(kthSmallest(matrix, 3))
print(kthSmallest(matrix, 4))


