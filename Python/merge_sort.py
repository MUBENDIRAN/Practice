arr = list(map(int,input().split()))
# we used function for code reuse of same arr for different loops (nested loops)
def merge_sort(arr):
    # since its less than one or one no need of sort so return the actual 
    if len(arr) <= 1:
        return arr
    # like binary search we divide the sequence into two as left and right
    mid = len(arr) // 2
    left = arr[ :mid]
    right = arr[mid: ]
    # we use two variable to store the sorted values 
    sorted_left = merge_sort(left)
    sorted_right = merge_sort(right)
    # this empty list is for storing the combined sorted 
    result = []
    # i for left the initial part sorting and j for right final part sorting 
    i = 0
    j = 0
    # while both the first iteration of i and j is less than the actual length loop continues
    while i < len(sorted_left) and j < len(sorted_right):
        # if initial is part element and final part element are compared and initial is small add to result and move the initial iteration 
        if sorted_left[i] < sorted_right[j]:
            result.append(sorted_left[i])
            i += 1
        else:
        # if not add the right side element and move the final part 
            result.append(sorted_right[j])
            j += 1
    # since result has already the sorted but not the exact we do sorting iteration on each variable previously assigned 
    while i < len(sorted_left):
        result.append(sorted_left[i])
        i += 1
    while j < len(sorted_right):
        result.append(sorted_right[j])
        j += 1
    return result
print(merge_sort(arr))
