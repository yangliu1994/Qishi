
# Given a list of sorted characters letters containing only lowercase letters,
# and given a target letter target, find the smallest element in the list that is larger than the given target.
#
# Letters also wrap around. For example, if the target is target = 'z' and letters = ['a', 'b'], the answer is 'a'.

def smallest_greater(letters, target):
    if letters[-1] <= target:
        return letters[0]
    l = 0
    r = len(letters) - 1
    while l < r:
        m = l + int((r - l) / 2)
        if letters[m] <= target:
            l = m + 1
        else:
            r = m
    return letters[l]

letters = ["c", "f", "j"]
target = "a"
print(smallest_greater(letters, target))


letters = ["c", "f", "j"]
target = "c"
print(smallest_greater(letters, target))


letters = ["c", "f", "j"]
target = "d"
print(smallest_greater(letters, target))

letters = ["c", "f", "j"]
target = "g"
print(smallest_greater(letters, target))

letters = ["c", "f", "j"]
target = "j"
print(smallest_greater(letters, target))

letters = ["c", "f", "j"]
target = "k"
print(smallest_greater(letters, target))
