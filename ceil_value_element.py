arr = list(map(int,input().split()))
target = int(input())
left = 0
right = len(arr) - 1
ceil_val = -1
while left <= right:
    mid = (left + right) // 2
    if arr[mid] >= target:
        ceil_val = arr[mid]
        right = mid - 1
    else:
        left = mid + 1
print(ceil_val)