# finding the peak means the values is which is greater than neighbouring values it can be more than one
arr = list(map(int,input().split()))
left = 0
right = len(arr) - 1
while left < right:
    mid = (left + right) // 2
    if arr[mid] < arr[mid + 1]:
    # If mid element is smaller 
        left = mid + 1
    else:
    # If mid element is lesser
        right = mid 
print(left)