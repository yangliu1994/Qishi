
def search(array, target):
    l1 = 0
    r1 = len(array) - 1
    while r1 > l1:
        m = l1 + int((r1 - l1) / 2)
        if array[m] < target:
            l1 = m + 1
        else:
            r1 = m
    l2 = 0
    r2 = len(array)
    while r2 > l2:
        m = l2 + int((r2 - l2) / 2)
        if array[m] <= target:
            l2 = m + 1
        else:
            r2 = m
    return list(range(l1, l2))

array = [5, 7, 7, 8, 8, 10]
target = 8

print(search(array, target))

array = [5, 7, 7, 8, 8, 8]
target = 8

print(search(array, target))


