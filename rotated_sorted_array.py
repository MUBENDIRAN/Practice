arr = list(map(int,input().split()))
target = int(input())
left = 0
right = len(arr) - 1
while left <= right:
    if arr[mid] == target:
        print(mid)
        break
    elif arr[left] <= arr[mid]:
        if arr[left] <= target < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1
    else:
        if arr[mid] < target <= arr[right]:
            left = mid + 1
        else:
            right = mid - 1
