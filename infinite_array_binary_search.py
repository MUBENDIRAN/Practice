arr = list(map(int,input().split()))
target = int(input())
left = 0
right = 1
while arr[right] < len(arr) and arr[right] < target:
    left = right 
    right = right * 2
    while left <= right :
        mid = (left + right) // 2
        if arr[mid] == target:
            print(mid)
            break
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
print(-1)