def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = arr[ :mid]
    right = arr[mid: ]
    sorted_left = merge_sort(left)
    sorted_right = merge_sort(right)
    result = []
    i = 0
    j = 0
    while i < len(sorted_left) and j < len(sorted_right):
        if sorted_left[i] < sorted_right[j]:
            result.append(sorted_left[i])
            i += 1
        else:
            result.append(sorted_right[j])
            j += 1
    while i < len(sorted_left):
        result.append(sorted_left[i])
        i += 1
    while j < len(sorted_right):
        result.append(sorted_right[i])
        j += 1
    return result

