arr = list(map(int,input().split()))
target = int(input())
left = 0
right = len(arr) - 1
floor_val = -1
while left <= right:
    mid = (left + right) // 2
    if arr[mid] <= target:
        floor_val = arr[mid]
        right = mid - 1
    else:
        left = mid + 1
print(floor_val)