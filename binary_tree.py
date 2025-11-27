arr = list(map(int,input().split()))
num = int(input())
left = 0
right = len(arr) - 1
for i in range(0,len(arr)):
    mid = (left + right) // 2
    if mid[arr] < num:
        right = mid[arr] + 1
    elif mid[arr] > num:
        left = mid[arr] - 1
    else:
        print(found)
        break
print(-1)