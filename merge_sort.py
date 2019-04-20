
def merge_sort(arr):
    if len(arr) == 1:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    merge_sort(left)
    merge_sort(right)

    i = 0
    j = 0
    k = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
    if i < len(left):
        arr[k:len(arr)] = left[i:len(left)]
    else:
        arr[k:len(arr)] = right[j:len(right)]
    return arr

print(merge_sort([4, 2, 3, 1, 8, 2, 5, 3]))
