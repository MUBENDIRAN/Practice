n = int(input())
left = 1
right = n
ans = 0
while left <= right:
    mid = (left + right) // 2
    if mid*mid == n:
        ans = mid
        break
    elif mid*mid < n:
        ans = mid
        left = mid + 1
    else:
        right = mid - 1
print(ans)
