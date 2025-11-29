arr = list(map(int,input().split()))
left = 0
right = len(arr) - 1
first_bad = -1
while left <= right:
    mid = ( left + right) // 2
    if arr[mid] == 1:
        first_bad = mid
        right = mid - 1
    else:
        left = mid + 1
print(first_bad)