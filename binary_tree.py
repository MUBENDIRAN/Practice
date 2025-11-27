arr = list(map(int,input().split()))
num = int(input())
left = 0
right = len(arr) - 1
while left < right:
    mid = (left + right) // 2
    if arr[mid] < num:
        right = mid + 1
    elif arr[mid] > num:
        left = mid - 1
    else:
        print(mid)
        break
else:
    print(-1)