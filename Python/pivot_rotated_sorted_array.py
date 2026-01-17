arr = list(map(int,input().split()))
left = 0
right = len(arr) - 1
while left < right:
    mid = (left + right) // 2
    # if pivot element is in left move the right pointer
    if arr[mid] > arr[right]:
        left = mid + 1
    else:
    # if the pivot element is in right then right pointer be constant and move only left pointer
        right = mid
print(left)