arr = list(map(int,input().split()))
num = int(input())
left = 0
right = len(arr) - 1
while left < right:
    mid = (left + right) // 2
    if arr[mid] < num:
        right = arr[mid] + 1
    elif arr[mid] > num:
        left = arr[mid] - 1
    else:
        print(mid)
        break
print(-1)