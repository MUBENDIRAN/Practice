arr = list(map(int,input().split()))
left = 0
right = len(arr) - 1
while left < right:
    mid = (left + right) // 2
    # if array is sorted in one side
    if arr[mid] < arr[right]:
        # move the left pointer if minimum is in right more then mid 
        left = mid + 1
    else:
        # if not middle is constant in right pointer
        right = mid
print(arr[left])
