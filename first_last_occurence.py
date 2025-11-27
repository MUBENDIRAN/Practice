arr = list(map(int,input().split()))
target = int(input())
left = 0 ; right = len(arr) - 1 ; first = -1
while left <= right:
    mid = (left + right ) // 2
    if arr[mid] == target:
        first = mid
        right = mid - 1
    elif arr[mid] > target:
        right = mid - 1
    else:
        left = mid + 1
left = 0 ; right = len(arr) - 1 ; last = -1
while left <= right:
    mid = (left + right) // 2
    if arr[mid] == target:
        last = mid
        left = mid + 1
    elif arr[mid] > target:
        right = mid - 1
    else:
        left = mid + 1
print(first,last)