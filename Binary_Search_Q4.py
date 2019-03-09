
def peak(lst):
    l = 0
    r = len(lst) - 1
    while l < r:
        m = l + int((r - l) / 2)
        if lst[m] < lst[m+1]:
            l = m + 1
        else:
            r = m
    return l

print(peak([1, 2, 3, 1]))
